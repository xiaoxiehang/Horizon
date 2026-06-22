#!/bin/bash
# Horizon 自动更新脚本
# 解决：分支切换、数据同步、GitHub Pages 更新

set -e

cd /workspace/Horizon

# 1. 确保在 daily-digest 分支
git checkout daily-digest

# 2. 加载环境变量
export ANTHROPIC_API_KEY="sk-sp-c8d4b3c18c954076bee30716cc4a6209"

# 3. 抓取新闻并生成中文摘要
echo "🔄 抓取新闻..."
uv run horizon --hours 24

# 4. 构建 HTML
echo "🔨 构建 HTML..."
python3 build.py

# 5. 提交到 daily-digest
echo "📤 提交到 daily-digest..."
git add -A
git commit -m "每日更新: $(date +%Y-%m-%d)" || echo "无新内容"
git push origin daily-digest

# 6. 切换到 gh-pages 分支
echo "🔄 切换到 gh-pages..."
git checkout gh-pages

# 7. 从 daily-digest 复制最新文件
git show daily-digest:docs/index.html > docs/index.html
git show daily-digest:docs/_posts/$(ls -t data/summaries/ | grep "zh.md" | head -1 | sed 's/horizon-//' | sed 's/-zh.md//')-summary-zh.md > docs/_posts/$(ls -t data/summaries/ | grep "zh.md" | head -1 | sed 's/horizon-//' | sed 's/-zh.md//')-summary-zh.md 2>/dev/null || true

# 8. 复制根目录
cp docs/index.html index.html

# 9. 提交到 gh-pages
echo "📤 提交到 gh-pages..."
git add -A
git commit -m "每日更新: $(date +%Y-%m-%d)" || echo "无新内容"
git push origin gh-pages

# 10. 切回 daily-digest
git checkout daily-digest

echo "✅ 完成！"
