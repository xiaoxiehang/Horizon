#!/usr/bin/env python3
"""Horizon daily news aggregation and deployment script."""
import os
import sys
import subprocess
import time
import json
import re
from datetime import datetime
from pathlib import Path
from urllib import request as urlrequest
from urllib.error import URLError

HORIZON_DIR = Path("/workspace/Horizon")
TODAY = datetime.now().strftime("%Y-%m-%d")
DINGTALK_WEBHOOK = "https://oapi.dingtalk.com/robot/send?access_token=4e8d31201fc7247def8c6be2eb82ec69ab15fff003d27920a4bc8536ec96c6e8"

def run(cmd, cwd=None, check=True, capture=True):
    """Run a shell command."""
    print(f">>> {cmd}")
    result = subprocess.run(
        cmd, shell=True, cwd=cwd or HORIZON_DIR,
        capture_output=capture, text=True
    )
    if capture:
        if result.stdout:
            print(result.stdout[-2000:] if len(result.stdout) > 2000 else result.stdout)
        if result.stderr:
            print(f"STDERR: {result.stderr[-1000:] if len(result.stderr) > 1000 else result.stderr}")
    if check and result.returncode != 0:
        print(f"Command failed with code {result.returncode}")
    return result

def step1_fetch_news():
    """Step 1: Fetch news from last 24 hours."""
    print("=" * 60)
    print("STEP 1: Fetching news (--hours 24)")
    print("=" * 60)
    result = run("uv run horizon --hours 24", check=False)
    if result.returncode != 0:
        print("Step 1 failed, but continuing with build...")
    return result.returncode == 0

def step2_build():
    """Step 2: Build Chinese pages."""
    print("=" * 60)
    print("STEP 2: Building Chinese pages (build.py)")
    print("=" * 60)
    result = run("uv run python build.py", check=False)
    if result.returncode != 0:
        print("Build failed! Checking for errors...")
        return False
    # Verify output exists
    index_file = HORIZON_DIR / "docs" / "index.html"
    if index_file.exists():
        print(f"✓ Build successful: {index_file} exists ({index_file.stat().st_size} bytes)")
        return True
    else:
        print("✗ docs/index.html not found after build")
        return False

def step3_deploy():
    """Step 3: Push to gh-pages branch."""
    print("=" * 60)
    print("STEP 3: Deploying to gh-pages")
    print("=" * 60)

    # Get current branch
    result = run("git rev-parse --abbrev-ref HEAD", check=False)
    current_branch = result.stdout.strip() if result.stdout else "daily-digest"
    print(f"Current branch: {current_branch}")

    # Checkout gh-pages
    run("git checkout gh-pages", check=False)

    # Copy index.html
    run("cp docs/index.html index.html", check=False)

    # Check for changes
    result = run("git status --porcelain", check=False)
    if not result.stdout.strip():
        print("No changes to commit")
        # Go back
        run(f"git checkout {current_branch}", check=False)
        return True

    # Commit
    run(f'git add . && git commit -m "每日更新"', check=False)

    # Push with retries
    for attempt in range(1, 6):
        print(f"Push attempt {attempt}/5...")
        result = run("git push origin gh-pages 2>&1", check=False)
        output = (result.stdout or "") + (result.stderr or "")
        if result.returncode == 0 or "Everything up-to-date" in output:
            print("✓ 推送成功")
            break
        else:
            print(f"✗ 推送失败，第 {attempt} 次重试...")
            if attempt < 5:
                time.sleep(30)
    else:
        print("All 5 push attempts failed")

    # Return to original branch
    run(f"git checkout {current_branch}", check=False)
    return True

def step4_dingtalk_notify():
    """Step 4: Send DingTalk notification."""
    print("=" * 60)
    print("STEP 4: Sending DingTalk notification")
    print("=" * 60)

    # Find today's Chinese summary
    # Try multiple possible locations
    possible_paths = [
        HORIZON_DIR / "data" / "summaries" / f"horizon-{TODAY}-zh.md",
        HORIZON_DIR / "_posts" / f"{TODAY}-summary-zh.md",
        HORIZON_DIR / "docs" / f"horizon-{TODAY}-zh.md",
    ]

    summary_file = None
    for p in possible_paths:
        if p.exists():
            summary_file = p
            break

    if not summary_file:
        # Try to find any recent zh summary
        import glob
        patterns = [
            str(HORIZON_DIR / "data/summaries/horizon-*-zh.md"),
            str(HORIZON_DIR / "_posts/*-summary-zh.md"),
        ]
        for pat in patterns:
            files = sorted(glob.glob(pat))
            if files:
                summary_file = Path(files[-1])
                break

    if not summary_file:
        print("No summary file found, sending generic notification")
        send_dingtalk("## 发布 | Horizon 每日速递\n\n今日暂无新闻更新\n\n[🔗 查看完整日报](https://xiaoxiehang.github.io/Horizon/)")
        return False

    print(f"Reading summary: {summary_file}")
    content = summary_file.read_text(encoding="utf-8")

    # Extract Chinese titles and links
    # Match patterns like: - [标题](链接) or ## Title followed by [link]
    # Common markdown patterns
    lines = content.split("\n")
    items = []

    for line in lines:
        # Match markdown links: [text](url)
        matches = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', line)
        for title, url in matches:
            # Only keep titles containing Chinese characters
            if re.search(r'[\u4e00-\u9fff]', title):
                # Clean up title
                title = title.strip()
                url = url.strip()
                if title and url and len(title) > 2:
                    items.append((title, url))

    # Deduplicate
    seen = set()
    unique_items = []
    for title, url in items:
        if title not in seen:
            seen.add(title)
            unique_items.append((title, url))

    # Limit to 20
    items = unique_items[:20]
    print(f"Found {len(items)} Chinese news items")

    if not items:
        text = "## 发布 | Horizon 每日速递\n\n今日新闻已更新\n\n[🔗 查看完整日报](https://xiaoxiehang.github.io/Horizon/)"
    else:
        text = "## 发布 | Horizon 每日速递\n\n"
        for title, url in items:
            text += f"- [{title}]({url})\n"
        text += "\n[🔗 查看完整日报](https://xiaoxiehang.github.io/Horizon/)"

    # Check size limit (DingTalk 20KB)
    if len(text.encode("utf-8")) > 18000:
        # Trim to fewer items
        while len(text.encode("utf-8")) > 18000 and len(items) > 1:
            items.pop()
            text = "## 发布 | Horizon 每日速递\n\n"
            for title, url in items:
                text += f"- [{title}]({url})\n"
            text += "\n[🔗 查看完整日报](https://xiaoxiehang.github.io/Horizon/)"
        print(f"Trimmed to {len(items)} items to fit under 20KB")

    send_dingtalk(text)
    return True

def send_dingtalk(text):
    """Send markdown message to DingTalk."""
    payload = {
        "msgtype": "markdown",
        "markdown": {
            "title": "发布 | Horizon 每日速递",
            "text": text
        }
    }
    data = json.dumps(payload).encode("utf-8")
    req = urlrequest.Request(
        DINGTALK_WEBHOOK,
        data=data,
        headers={"Content-Type": "application/json"}
    )
    try:
        with urlrequest.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            print(f"DingTalk response: {result}")
            if result.get("errcode") == 0:
                print("✓ DingTalk notification sent successfully")
            else:
                print(f"✗ DingTalk error: {result}")
    except URLError as e:
        print(f"✗ Failed to send DingTalk: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

def main():
    print(f"Horizon Daily News Aggregation - {TODAY}")
    print(f"Directory: {HORIZON_DIR}")
    print()

    os.chdir(HORIZON_DIR)

    results = {}
    results["fetch"] = step1_fetch_news()
    results["build"] = step2_build()
    results["deploy"] = step3_deploy()
    results["notify"] = step4_dingtalk_notify()

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for step, success in results.items():
        status = "✓" if success else "✗"
        print(f"  {status} {step}")

    return all(results.values())

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
