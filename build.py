#!/usr/bin/env python3
"""Build static HTML from Horizon markdown summary."""
import re
from pathlib import Path
from datetime import datetime

def parse_markdown(md_file):
    """Parse Horizon markdown summary into structured data."""
    content = Path(md_file).read_text(encoding='utf-8')
    
    # Detect language
    is_zh = '每日速递' in content or '已分析' in content
    
    # Extract date
    if is_zh:
        date_match = re.search(r'# Horizon 每日速递 - (\d{4}-\d{2}-\d{2})', content)
    else:
        date_match = re.search(r'# Horizon Daily - (\d{4}-\d{2}-\d{2})', content)
    date_str = date_match.group(1) if date_match else datetime.now().strftime('%Y-%m-%d')
    
    # Parse news items - support both Chinese and English formats
    items = []
    
    # Pattern for Chinese format: ## [标题](url) ⭐️ X.X/10
    # Followed by content, then source info, then **背景**: or **Tags**:
    item_pattern = re.compile(
        r'<a id="item-\d+"></a>\s*\n'
        r'## \[(.+?)\]\((.+?)\)(?:\s*⭐️ [\d.]+/10)?\n\n'  # Title and URL (score optional)
        r'(.+?)\n\n'  # Summary
        r'(?:rss|hackernews) · .+? · .+?'  # Source info line
        r'(?:\s*·\s*\[社区讨论\]\(.+?\))?\n\n'  # Optional community discussion link
        r'(?:\*\*背景\*\*: (.+?)\n\n)?'  # Optional background
        r'(?:<details>.*?</details>\n\n)?'  # Optional details
        r'(?:\*\*社区讨论\*\*: .+?\n\n)?'  # Optional community discussion
        r'(?:\*\*标签\*\*: `.+?`|\*\*Tags\*\*: `.+?`)',  # Tags (Chinese or English)
        re.DOTALL
    )
    
    for match in item_pattern.finditer(content):
        title, url, summary, background = match.groups()
        
        # Skip if title is mostly English (no Chinese characters)
        has_chinese = bool(re.search(r'[\u4e00-\u9fff]', title))
        if not has_chinese:
            continue
        
        # Clean summary (first paragraph only, max 280 chars)
        summary_clean = summary.split('\n\n')[0].strip()
        if len(summary_clean) > 280:
            summary_clean = summary_clean[:277] + '...'
        
        items.append({
            'title': title,
            'url': url,
            'summary': summary_clean,
        })
    
    # Sort by score (keep original order now since no score)
    return {
        'date': date_str,
        'items': items
    }

def build_html(data, output_file):
    """Generate HTML with news list as main content."""
    # Build news items HTML
    items_html = []
    for item in data['items']:
        item_html = f'''    <article class="news-item">
      <h3><a href="{item['url']}" target="_blank">{item['title']}</a></h3>
      <p class="content">{item['summary']}</p>
    </article>'''
        items_html.append(item_html)
    
    news_items = '\n'.join(items_html)
    
    # Build complete HTML
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Horizon 每日速递</title>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      background: #fafafa;
      color: #1a1a1a;
      line-height: 1.6;
      padding: 20px;
      max-width: 900px;
      margin: 0 auto;
    }}
    header {{
      margin-bottom: 30px;
      padding-bottom: 20px;
      border-bottom: 1px solid #eee;
    }}
    header h1 {{
      font-size: 1.8em;
      font-weight: 600;
      margin-bottom: 5px;
    }}
    header .date {{
      color: #666;
      font-size: 0.9em;
    }}
    .news-list {{
      display: grid;
      gap: 16px;
      margin-bottom: 60px;
    }}
    .news-item {{
      background: white;
      padding: 20px 24px;
      border-radius: 10px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.06);
      transition: transform 0.15s, box-shadow 0.15s;
    }}
    .news-item:hover {{
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }}
    .news-item h3 {{
      font-size: 1.05em;
      font-weight: 500;
      line-height: 1.5;
      margin-bottom: 10px;
    }}
    .news-item h3 a {{
      color: #1a1a1a;
      text-decoration: none;
    }}
    .news-item h3 a:hover {{
      color: #0070f3;
    }}
    .content {{
      color: #555;
      font-size: 0.9em;
      line-height: 1.7;
    }}
    footer {{
      text-align: center;
      padding: 30px 0;
      border-top: 1px solid #eee;
      color: #999;
      font-size: 0.8em;
    }}
    footer a {{
      color: #666;
      text-decoration: none;
    }}
    footer a:hover {{
      text-decoration: underline;
    }}
  </style>
</head>
<body>
  <header>
    <h1>Horizon 每日速递</h1>
    <div class="date">{data['date']}</div>
  </header>

  <main class="news-list">
{news_items}
  </main>

  <footer>
    <div>Powered by <a href="https://github.com/xiaoxiehang/Horizon">Horizon</a></div>
  </footer>
</body>
</html>'''
    
    # Write output
    Path(output_file).write_text(html, encoding='utf-8')
    print(f'✅ Generated: {output_file}')
    print(f"   Date: {data['date']}")
    print(f"   Items: {len(data['items'])}")

def main():
    # Find latest summary file (prefer Chinese)
    summaries_dir = Path('data/summaries')
    if not summaries_dir.exists():
        print('❌ No summaries directory found')
        return
    
    # First try Chinese summary
    summary_files = sorted(summaries_dir.glob('horizon-*-zh.md'), reverse=True)
    if not summary_files:
        # Fall back to English
        summary_files = sorted(summaries_dir.glob('horizon-*-en.md'), reverse=True)
    if not summary_files:
        print('❌ No summary files found')
        return
    
    latest = summary_files[0]
    print(f'📄 Processing: {latest}')
    
    # Parse and build
    data = parse_markdown(latest)
    build_html(data, 'docs/index.html')

if __name__ == '__main__':
    main()
