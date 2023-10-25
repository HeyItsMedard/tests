from datetime import datetime
import os
import json

json_file_path = 'file_stats.json'

if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as json_file:
        previous_stats = json.load(json_file)
else:
    previous_stats = {}

entries = os.scandir()
current_stats = {}

for entry in entries:
    entry_stat = entry.stat()
    current_stats[entry.name] = {
        "size": entry_stat.st_size,
        "last_modified": datetime.fromtimestamp(entry_stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
    }

changes = []

for name, current_stat in current_stats.items():
    previous_stat = previous_stats.get(name)
    if previous_stat is None:
        changes.append(f"New entry: {name}")
    elif current_stat != previous_stat:
        size_diff = current_stat["size"] - previous_stat["size"]
        change_desc = (
            f"Modified entry: {name} "
            f"+{size_diff} bytes" if size_diff > 0 else
            f"Modified entry: {name} "
            f"{size_diff} bytes" if size_diff < 0 else
            f"Modified entry: {name} (no size change)"
        )
        changes.append(change_desc)

for name in previous_stats.keys():
    if name not in current_stats:
        changes.append(f"Deleted entry: {name}")

if changes:
    print("Changes since last run:")
    for change in changes:
        print(change)

with open(json_file_path, 'w') as json_file:
    json.dump(current_stats, json_file, indent=4)

print(f"Data written to {json_file_path}")
"""
0. feladat:
Futtasd a fenti programot és nézd meg a kimenetét.

1. feladat:
A fájlok adataiból készíts egy JSON kimutatást.

2. feladat:
A kimutatás fájlba írása előtt, ha már létezik egy régebbi kimutatás, a program írja ki
az azóta történt módosításokat, pl.:
    Changes since last run:
    Modified entry: file_stats.json +64 bytes
    Modified entry: hf2_fajlok.py +7 bytes
    New entry: test_folder
    Deleted entry: folder_test
"""
