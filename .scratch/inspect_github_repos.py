import urllib.request
import json

repos_to_check = [
    'Agentic-Sales-Consultant',
    'EQOVE',
    'Layah.tools',
    'TextSweep',
    'DOMPilot',
    'PostCheck',
    'Stickerz',
    'compensation-intelligence-system',
    'proof_of_existence',
    'TradingSimulator',
    'Shayde'
]

for repo in repos_to_check:
    url = f"https://api.github.com/repos/utkarsh-2006/{repo}/contents"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            contents = json.loads(resp.read().decode())
            files = [item['name'] for item in contents]
            print(f"=== {repo} ===")
            print(f"Files: {', '.join(files[:15])}")
            # If README.md exists, let's fetch first few lines
            if 'README.md' in files or 'readme.md' in files:
                rm_name = 'README.md' if 'README.md' in files else 'readme.md'
                rm_url = f"https://raw.githubusercontent.com/utkarsh-2006/{repo}/main/{rm_name}"
                try:
                    with urllib.request.urlopen(urllib.request.Request(rm_url, headers={'User-Agent': 'Mozilla/5.0'})) as rm_resp:
                        rm_text = rm_resp.read().decode('utf-8', errors='ignore')
                        first_lines = '\n'.join(rm_text.splitlines()[:5])
                        print(f"README preview:\n{first_lines}")
                except Exception as e:
                    # try master branch
                    rm_url_m = f"https://raw.githubusercontent.com/utkarsh-2006/{repo}/master/{rm_name}"
                    try:
                        with urllib.request.urlopen(urllib.request.Request(rm_url_m, headers={'User-Agent': 'Mozilla/5.0'})) as rm_resp:
                            rm_text = rm_resp.read().decode('utf-8', errors='ignore')
                            first_lines = '\n'.join(rm_text.splitlines()[:5])
                            print(f"README preview (master):\n{first_lines}")
                    except Exception as e2:
                        print(f"Could not read README: {e2}")
            else:
                print("No README found.")
    except Exception as e:
        print(f"=== {repo} === Error: {e}")
    print()
