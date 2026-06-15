#!/usr/bin/env python3
"""Build static HTML from Horizon markdown summary."""
import re
import sys
from pathlib import Path
from datetime import datetime

def parse_markdown(md_file):
    """Parse Horizon markdown summary into structured data."""
    content = Path(md_file).read_text(encoding='utf-8')
    
    # Extract date
    date_match = re.search(r'# Horizon Daily - (\d{4}-\d{2}-\d{2})', content)
    date_str = date_match.group(1) if date_match else datetime.now().strftime('%Y-%m-%d')
    
    # Extract total items
    total_match = re.search(r'From (\d+) items', content)
    total_items = int(total_match.group(1)) if total_match else 0
    
    # Extract selected items
    selected_match = re.search(r'(\d+) important content pieces were selected', content)
    selected_items = int(selected_match.group(1)) if selected_match else 0
    
    # Parse news items
    items = []
    item_pattern = re.compile(
        r'<a id="item-\d+"></a>\s*\n'
        r'## \[(.+?)\]\((.+?)\) ⭐️ ([\d.]+)/10\n\n'
        r'(.+?)\n\n'
        r'(rss|hackernews) · (.+?) · (.+?)\n\n'
        r'\*\*Background\*\*: (.+?)\n\n'
        r'(?:<details>.*?</details>\n\n)?'
        r'\*\*Tags\*\*: `(.+?)`',
        re.DOTALL
    )
    
    for match in item_pattern.finditer(content):
        title, url, score, summary, source_type, source_name, time_str, background, tags_str = match.groups()
        
        # Extract tags
        tags = re.findall(r'#(\w[\w\s\-]*\w|\w+)', tags_str)
        
        # Clean summary (first paragraph only, max 280 chars)
        summary_clean = summary.split('\n\n')[0].strip()
        if len(summary_clean) > 280:
            summary_clean = summary_clean[:277] + '...'
        
        items.append({
            'title': title,
            'url': url,
            'score': float(score),
            'summary': summary_clean,
            'source': source_name,
            'time': time_str,
            'tags': tags[:4]
        })
    
    # Sort by score
    items.sort(key=lambda x: x['score'], reverse=True)
    
    return {
        'date': date_str,
        'total_items': total_items,
        'selected_items': selected_items,
        'items': items
    }

def build_html(data, template_file, output_file):
    """Generate HTML from template and data."""
    template = Path(template_file).read_text(encoding='utf-8')
    
    # Build news items HTML
    items_html = []
    for item in data['items']:
        tags_html = ''.join(f'<span class="tag">#{tag}</span>' for tag in item['tags'])
        item_html = f'''
      <a class="news-card" href="{item['url']}" target="_blank" rel="noopener">
        <div class="card-header">
          <span class="card-title">{item['title']}</span>
          <span class="score-badge">⭐️ {item['score']}/10</span>
        </div>
        <p class="card-summary">{item['summary']}</p>
        <div class="card-meta">
          <div class="tags">
            {tags_html}
          </div>
          <span class="source"><span class="source-dot"></span>{item['source']} · {item['time']}</span>
        </div>
      </a>'''
        items_html.append(item_html)
    
    news_items = '\n'.join(items_html)
    
    # Replace placeholders
    html = template.replace('{{DATE}}', data['date'])
    html = html.replace('{{TOTAL_ITEMS}}', str(data['total_items']))
    html = html.replace('{{SELECTED_ITEMS}}', str(data['selected_items']))
    html = html.replace('<!-- NEWS_ITEMS_PLACEHOLDER -->', news_items)
    
    # Write output
    Path(output_file).write_text(html, encoding='utf-8')
    print(f'✅ Generated: {output_file}')
    print(f"   Date: {data['date']}")
    print(f"   Items: {data['selected_items']}/{data['total_items']}")

def main():
    # Find latest summary file
    summaries_dir = Path('data/summaries')
    if not summaries_dir.exists():
        print('❌ No summaries directory found')
        sys.exit(1)
    
    summary_files = sorted(summaries_dir.glob('horizon-*-en.md'), reverse=True)
    if not summary_files:
        print('❌ No summary files found')
        sys.exit(1)
    
    latest = summary_files[0]
    print(f'📄 Processing: {latest}')
    
    # Parse and build
    data = parse_markdown(latest)
    build_html(data, 'docs/index.html', 'docs/index.html')

if __name__ == '__main__':
    main()
