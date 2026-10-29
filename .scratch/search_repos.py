import os

target_names = ['compensation-intelligence-system', 'TradingSimulator', 'proof_of_existence', 'proof-of-existence']
found = {}

for root, dirs, files in os.walk("D:/Utkarsh"):
    # Avoid deep walks in node_modules or .git
    dirs[:] = [d for d in dirs if d not in ('node_modules', '.git', '.next', 'dist', 'build', '.dart_tool')]
    for d in dirs:
        for t in target_names:
            if t.lower() in d.lower():
                found[d] = os.path.join(root, d)

print("Found targets:", found)
