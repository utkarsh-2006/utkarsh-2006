import markdown
import os
import re
import base64
from playwright.sync_api import sync_playwright

readme_path = "D:/Utkarsh/self projects/github profile/README.md"
assets_dir = "D:/Utkarsh/self projects/github profile/assets"
out_dir = "C:/Users/HP/.gemini/antigravity/brain/aaeffa02-cb79-4436-a965-5a5be0d29bb7/previews"
os.makedirs(out_dir, exist_ok=True)

with open(readme_path, "r", encoding="utf-8") as f:
    md_content = f.read()

# Replace local image paths with base64 data URIs so they load reliably without web security restrictions
def replace_asset(match):
    src = match.group(1)
    filename = os.path.basename(src)
    full_path = os.path.join(assets_dir, filename)
    if os.path.exists(full_path):
        with open(full_path, "rb") as af:
            b64 = base64.b64encode(af.read()).decode("utf-8")
            return f'src="data:image/svg+xml;base64,{b64}"'
    return match.group(0)

md_content_b64 = re.sub(r'src=["\'](?:\./)?assets/([^"\']+)["\']', replace_asset, md_content)

html_body = markdown.markdown(
    md_content_b64,
    extensions=['tables', 'fenced_code', 'nl2br']
)

full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{
    background-color: #0d1117;
    color: #e6edf3;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    margin: 0;
    padding: 24px;
    display: flex;
    justify-content: center;
  }}
  .markdown-body {{
    background-color: #0d1117;
    color: #e6edf3;
    max-width: 960px;
    width: 100%;
    font-size: 14px;
    line-height: 1.6;
    word-wrap: break-word;
  }}
  .markdown-body a {{ color: #58a6ff; text-decoration: none; }}
  .markdown-body a:hover {{ text-decoration: underline; }}
  .markdown-body img {{ max-width: 100%; box-sizing: border-box; }}
  .markdown-body code {{
    background-color: rgba(110,118,129,0.4);
    padding: 0.2em 0.4em;
    border-radius: 6px;
    font-size: 85%;
    font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
  }}
  .markdown-body pre {{
    background-color: #161b22;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 16px;
    overflow: auto;
  }}
  .markdown-body pre code {{ background-color: transparent; padding: 0; }}
  .markdown-body blockquote {{
    margin: 0 0 16px;
    padding: 0 1em;
    color: #8b949e;
    border-left: 0.25em solid #30363d;
  }}
  .markdown-body hr {{
    height: 1px;
    background-color: #30363d;
    border: none;
    margin: 24px 0;
  }}
  .markdown-body table {{
    border-spacing: 0;
    border-collapse: collapse;
    width: 100%;
    margin-top: 16px;
    margin-bottom: 16px;
  }}
  .markdown-body table th, .markdown-body table td {{
    padding: 8px 12px;
    border: 1px solid #30363d;
  }}
  .markdown-body table tr:nth-child(2n) {{
    background-color: #161b22;
  }}
  .markdown-body table th {{
    font-weight: 600;
    background-color: #161b22;
    text-align: left;
  }}
  .markdown-body h1, .markdown-body h2, .markdown-body h3, .markdown-body h4 {{
    margin-top: 24px;
    margin-bottom: 16px;
    font-weight: 600;
    line-height: 1.25;
    color: #f0f6fc;
  }}
  .markdown-body h3 {{
    border-bottom: 1px solid #21262d;
    padding-bottom: 0.3em;
  }}
</style>
</head>
<body>
<div class="markdown-body">
{html_body}
</div>
</body>
</html>
"""

temp_html = "D:/Utkarsh/self projects/github profile/.scratch/preview.html"
with open(temp_html, "w", encoding="utf-8") as f:
    f.write(full_html)

desktop_png = os.path.join(out_dir, "portfolio_audit_desktop.png")
mobile_png = os.path.join(out_dir, "portfolio_audit_mobile.png")

with sync_playwright() as p:
    browser = p.chromium.launch()
    
    # Desktop
    page = browser.new_page(viewport={"width": 1100, "height": 1200})
    page.goto(f"file:///{temp_html.replace(os.sep, '/')}")
    page.wait_for_load_state("networkidle")
    page.screenshot(path=desktop_png, full_page=True)
    print(f"Captured Desktop: {desktop_png}")
    
    # Mobile
    page_mob = browser.new_page(viewport={"width": 440, "height": 900})
    page_mob.goto(f"file:///{temp_html.replace(os.sep, '/')}")
    page_mob.wait_for_load_state("networkidle")
    page_mob.screenshot(path=mobile_png, full_page=True)
    print(f"Captured Mobile: {mobile_png}")
    
    browser.close()

print("Rendering complete!")
