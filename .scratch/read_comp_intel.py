import urllib.request

def fetch(path):
    url = f"https://raw.githubusercontent.com/utkarsh-2006/compensation-intelligence-system/main/{path}"
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
            return resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return f"Error: {e}"

print("=== package.json ===")
print(fetch('package.json')[:500])

print("\n=== prisma/schema.prisma ===")
print(fetch('prisma/schema.prisma')[:500])
