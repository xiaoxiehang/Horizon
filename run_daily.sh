#!/bin/bash
# Horizon Daily - 自动化运行脚本
set -e

echo "🚀 Starting Horizon Daily..."
cd /workspace/Horizon

# 1. 运行 Horizon 生成新闻
echo "📰 Fetching news..."
uv run horizon --hours 24

# 2. 找到最新的 summary 文件
LATEST_SUMMARY=$(ls -t data/summaries/horizon-*-en.md | head -1)
if [ -z "$LATEST_SUMMARY" ]; then
    echo "❌ No summary file found"
    exit 1
fi

echo "📄 Found: $LATEST_SUMMARY"

# 3. 构建静态 HTML
echo "🔨 Building static site..."
python build.py "$LATEST_SUMMARY" docs/index.html

# 4. 提交并推送到 GitHub
echo "📤 Pushing to GitHub..."
git add docs/index.html data/summaries/
DATE=$(date +%Y-%m-%d)
git commit -m "🌅 Daily digest: $DATE" || echo "No changes to commit"
git push origin daily-digest

# 5. 提取摘要用于钉钉通知
SELECTED=$(grep -o '[0-9]\+ important' "$LATEST_SUMMARY" | grep -o '[0-9]\+')
TOTAL=$(grep -o 'From [0-9]\+ items' "$LATEST_SUMMARY" | grep -o '[0-9]\+')

echo "✅ Done! $SELECTED/$TOTAL items selected"
echo "🔗 https://xiaoxiehang.github.io/Horizon/"

# 6. 输出通知内容（供 cron job 使用）
cat <<EOF
---
📊 Horizon Daily 已完成
- 日期: $DATE
- 精选: $SELECTED/$TOTAL 条新闻
- 链接: https://xiaoxiehang.github.io/Horizon/
EOF
