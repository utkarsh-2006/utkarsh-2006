import urllib.request
import json

def fetch_file(repo, path):
    url = f"https://raw.githubusercontent.com/utkarsh-2006/{repo}/main/{path}"
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
            return resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        # try master
        url_m = f"https://raw.githubusercontent.com/utkarsh-2006/{repo}/master/{path}"
        try:
            with urllib.request.urlopen(urllib.request.Request(url_m, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
                return resp.read().decode('utf-8', errors='ignore')
        except Exception as e2:
            return f"Error: {e2}"

print("=== TradingSimulator: TradeLab_MVP_Build_Plan.md ===")
text = fetch_file('TradingSimulator', 'TradeLab_MVP_Build_Plan.md')
print(text[:500] if text else "None")

print("\n=== proof_of_existence: package.json in proof-of-existence-ui ===")
text = fetch_file('proof_of_existence', 'proof-of-existence-ui/package.json')
print(text[:400] if text else "None")

print("\n=== compensation-intelligence-system: CLAUDE.md or AGENTS.md ===")
text = fetch_file('compensation-intelligence-system', 'CLAUDE.md')
print(text[:500] if text else "None")
