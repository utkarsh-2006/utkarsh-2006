import urllib.request
import json
import os

url = 'https://api.github.com/users/utkarsh-2006/repos?per_page=100'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        repos = json.loads(resp.read().decode())
    print(f"Total public repos: {len(repos)}\n")
    for r in sorted(repos, key=lambda x: x['name'].lower()):
        name = r['name']
        desc = r['description'] or "(No description)"
        lang = r['language'] or "None"
        hp = r.get('homepage') or "(No homepage)"
        topics = r.get('topics') or []
        stars = r.get('stargazers_count', 0)
        forks = r.get('forks_count', 0)
        print(f"[{name}]")
        print(f"  URL: {r['html_url']}")
        print(f"  Desc: {desc}")
        print(f"  Lang: {lang} | Topics: {topics} | Homepage: {hp}")
        print(f"  Stars: {stars} | Forks: {forks}")
        print()
except Exception as e:
    print("Error:", e)
