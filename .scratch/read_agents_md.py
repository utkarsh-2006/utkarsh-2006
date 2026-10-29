import urllib.request

url = "https://raw.githubusercontent.com/utkarsh-2006/compensation-intelligence-system/main/AGENTS.md"
try:
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
        print(resp.read().decode('utf-8', errors='ignore')[:600])
except Exception as e:
    print("Error:", e)
