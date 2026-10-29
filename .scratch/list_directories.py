import os

print("--- D:\\Utkarsh root items ---")
for item in os.listdir("D:/Utkarsh"):
    p = os.path.join("D:/Utkarsh", item)
    if os.path.isdir(p):
        print(f"DIR: {item}")
    else:
        print(f"FILE: {item}")

print("\n--- D:\\Utkarsh\\self projects items ---")
for item in os.listdir("D:/Utkarsh/self projects"):
    p = os.path.join("D:/Utkarsh/self projects", item)
    if os.path.isdir(p):
        print(f"DIR: {item}")
    else:
        print(f"FILE: {item}")

print("\n--- D:\\Utkarsh\\BrowserLab items ---")
if os.path.exists("D:/Utkarsh/BrowserLab"):
    for item in os.listdir("D:/Utkarsh/BrowserLab"):
        print(f"BrowserLab item: {item}")
