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

# Replace local image paths with base64 data URIs so they load reliably
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

# Light mode template implementing the approved palette:
# Background: #FAF9F6
# Primary text: #10233F
# Accent: #306FE5
# Secondary text: #657187
# Borders: #D4D9E2
light_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GitHub Profile Preview — Light Mode</title>
<style>
  * {{
    box-sizing: border-box;
  }}
  body {{
    background-color: #FAF9F6;
    color: #10233F;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    margin: 0;
    padding: 32px 20px;
    display: flex;
    justify-content: center;
    -webkit-font-smoothing: antialiased;
  }}
  .markdown-body {{
    background-color: #FAF9F6;
    color: #10233F;
    max-width: 920px;
    width: 100%;
    font-size: 14.5px;
    line-height: 1.65;
    word-wrap: break-word;
  }}
  .markdown-body a {{
    color: #306FE5;
    text-decoration: none;
    font-weight: 500;
  }}
  .markdown-body a:hover {{
    text-decoration: underline;
  }}
  .markdown-body img {{
    max-width: 100%;
    height: auto;
    display: inline-block;
    box-sizing: border-box;
  }}
  .markdown-body code {{
    background-color: #EEF2F6;
    color: #10233F;
    padding: 0.2em 0.45em;
    border-radius: 4px;
    font-size: 86%;
    font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
    border: 1px solid #D4D9E2;
  }}
  .markdown-body pre {{
    background-color: #F4F6F9;
    border: 1px solid #D4D9E2;
    border-radius: 6px;
    padding: 16px;
    overflow: auto;
    font-size: 13px;
    line-height: 1.5;
  }}
  .markdown-body pre code {{
    background-color: transparent;
    border: none;
    padding: 0;
    color: #10233F;
  }}
  .markdown-body blockquote {{
    margin: 16px 0;
    padding: 12px 18px;
    color: #657187;
    background-color: rgba(48, 111, 229, 0.03);
    border-left: 3px solid #306FE5;
    border-radius: 0 4px 4px 0;
    font-style: italic;
  }}
  .markdown-body hr {{
    height: 1px;
    background-color: #D4D9E2;
    border: none;
    margin: 28px 0;
  }}
  .markdown-body table {{
    border-spacing: 0;
    border-collapse: collapse;
    width: 100%;
    margin-top: 18px;
    margin-bottom: 24px;
    font-size: 13.5px;
  }}
  .markdown-body table th, .markdown-body table td {{
    padding: 10px 14px;
    border: 1px solid #D4D9E2;
    text-align: left;
    vertical-align: top;
  }}
  .markdown-body table th {{
    font-weight: 600;
    background-color: #EDF1F7;
    color: #10233F;
  }}
  .markdown-body table tr:nth-child(2n) {{
    background-color: #F5F7FA;
  }}
  .markdown-body h1, .markdown-body h2, .markdown-body h3, .markdown-body h4 {{
    margin-top: 28px;
    margin-bottom: 14px;
    font-weight: 600;
    line-height: 1.3;
    color: #10233F;
  }}
  .markdown-body h3 {{
    border-bottom: 1px solid #D4D9E2;
    padding-bottom: 0.35em;
    font-size: 16px;
    letter-spacing: 0.03em;
  }}
  .markdown-body h4 {{
    font-size: 15px;
    color: #10233F;
  }}
  .markdown-body sub {{
    color: #657187;
  }}
  .markdown-body p {{
    margin-top: 0;
    margin-bottom: 16px;
  }}
  .markdown-body ul {{
    padding-left: 20px;
    margin-bottom: 16px;
  }}
  .markdown-body li {{
    margin-bottom: 6px;
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

temp_html = "D:/Utkarsh/self projects/github profile/.scratch/preview_light.html"
with open(temp_html, "w", encoding="utf-8") as f:
    f.write(light_html)

desktop_png = os.path.join(out_dir, "portfolio_audit_desktop.png")
mobile_png = os.path.join(out_dir, "portfolio_audit_mobile.png")
verified_desktop_png = os.path.join(out_dir, "verified_readme_desktop.png")
verified_mobile_png = os.path.join(out_dir, "verified_readme_mobile.png")

with sync_playwright() as p:
    browser = p.chromium.launch()
    
    # Desktop Light Mode
    page = browser.new_page(
        viewport={"width": 1100, "height": 1200},
        color_scheme="light"
    )
    page.goto(f"file:///{temp_html.replace(os.sep, '/')}")
    page.wait_for_load_state("networkidle")
    page.screenshot(path=desktop_png, full_page=True)
    page.screenshot(path=verified_desktop_png, full_page=True)
    print(f"Captured Desktop Light: {desktop_png}")
    
    # Mobile Light Mode
    page_mob = browser.new_page(
        viewport={"width": 440, "height": 900},
        color_scheme="light"
    )
    page_mob.goto(f"file:///{temp_html.replace(os.sep, '/')}")
    page_mob.wait_for_load_state("networkidle")
    page_mob.screenshot(path=mobile_png, full_page=True)
    page_mob.screenshot(path=verified_mobile_png, full_page=True)
    print(f"Captured Mobile Light: {mobile_png}")
    
    browser.close()

print("Light mode rendering complete!")
