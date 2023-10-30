import os
import pickle
from datetime import datetime

# entries = os.scandir()
# stats = {entry.name: entry.stat() for entry in entries}
# print("Name".ljust(20), "Size".rjust(9), "Last modified")
# print("-" * 60)
# for name, stat in stats.items():
#     print(f"{name:20}", f"{stat.st_size:9}", datetime.fromtimestamp(stat.st_mtime))
# print()

class DirEntry:
    def __init__(self, size, mtime):
        self.st_size = size
        self.st_mtime = mtime

pickle_file_path = 'file_stats.pkl'

if os.path.exists(pickle_file_path):
    with open(pickle_file_path, 'rb') as f:
        previous_stats = pickle.load(f)
else:
    previous_stats = {}

entries = os.scandir()
current_stats = {}

for entry in entries:
    entry_stat = entry.stat()
    current_stats[entry.name] = DirEntry(entry_stat.st_size, entry_stat.st_mtime)

changes = []

for name, current_stat in current_stats.items():
    previous_stat = previous_stats.get(name)
    if previous_stat is None:
        changes.append(f"New entry: {name}")
    elif current_stat.st_size != previous_stat.st_size or current_stat.st_mtime != previous_stat.st_mtime:
        size_diff = current_stat.st_size - previous_stat.st_size
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

try:
    with open(pickle_file_path, 'wb') as f:
        pickle.dump(current_stats, f)
    print(f"Data written to {pickle_file_path}")
except TypeError:
    pass # minden rendben

# entries = os.scandir()
# stats = {entry.name: entry.stat() for entry in entries}
# print("Name".ljust(20), "Size".rjust(9), "Last modified")
# print("-" * 60)
# for name, stat in stats.items():
#     print(f"{name:20}", f"{stat.st_size:9}", datetime.fromtimestamp(stat.st_mtime))
# print()

"""
A feladat ugyanaz, mint az előző, csak most JSON helyett pickle segítségével mentsd
fájlba a teljes `stats` dictet.

Látható, hogy az így kapott fájl nagyobb, de több információt is tartalmaz, mint a JSON.
Készíts egy osztályt, amit a DirEntry.stat() eredményével inicializálva csak a szükséges
`st_size` és `st_mtime` attribútumokat tárolja el.
Módosítsd a `stats` dictet úgy, hogy ennek az osztálynak a példányait tárolja.
Az ebből készült pickle fájl már kisebb lesz a JSON-nél.
"""
