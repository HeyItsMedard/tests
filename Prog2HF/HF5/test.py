import os
import json
import matplotlib.pyplot as plt
from collections import Counter # for easier counting of values

artists = 'albums'

get_year_count = {}

unique_names = set()
first_names = []

band_sizes = Counter()
album_sizes = Counter()

band_album_counts = Counter()
band_album_years = {}

for band_name in os.listdir(artists):
    band_directory = os.path.join(artists, band_name)
    if os.path.isdir(band_directory):
        band_album_counts[band_name] = 0 #4
        band_album_years[band_name] = [] #5
        for filename in os.listdir(band_directory):
            if filename.endswith(".json"):
                album_path = os.path.join(band_directory, filename)
                with open(album_path, "r") as f:
                    try:
                        album = json.load(f)
                        #1.
                        get_year_count[album["year"]] = get_year_count.get(album["year"], 0) + 1
                        #2.
                        for name in album["personnel"]:
                            first_name = name.split()[0]
                            if name not in unique_names:
                                unique_names.add(name)
                                first_names.append(first_name)
                        #3.
                        band_size = len(album["personnel"])
                        band_sizes[band_size] += 1
                        track_count = len(album["tracks"])
                        album_sizes[track_count] += 1
                        #4., 5.
                        if "year" in album:
                            band_album_counts[band_name] += 1
                            band_album_years[band_name].append(album["year"])
                    except:
                        pass # errors are better off ignored
        
# Task 1
years = list(get_year_count.keys())
years.sort()
sorted_years = {i: get_year_count[i] for i in years}

plt.figure(figsize=(5, 4))
plt.plot(sorted_years.keys(), sorted_years.values(), marker='o')
plt.tight_layout()
plt.savefig('task1_yearly_albums.png')

# Task 2
name_counts = Counter(first_names)

filtered_names = [(name, count) for name, count in name_counts.items() if count >= 10]

filtered_names.sort(key=lambda x: x[1], reverse=False)

names = [name for name, _ in filtered_names]
counts = [count for _, count in filtered_names]

plt.figure(figsize=(5, 4))
plt.barh(names, counts)
plt.title('Most Common First Name in Rock Bands')
plt.tight_layout()
plt.savefig('task2_common_fnames.png')

# Task 3
band_sizes_combined = Counter()

for size, count in band_sizes.items():
    if size >= 8:
        band_sizes_combined["8+"] += count
    else:
        band_sizes_combined[str(size)] += count  # string conversion for labeling

album_sizes_combined = Counter()

for size, count in album_sizes.items():
    if size >= 16:
        album_sizes_combined["16+"] += count
    else:
        album_sizes_combined[str(size)] += count

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

axes[0].pie(band_sizes_combined.values(), labels=band_sizes_combined.keys(), startangle=90)
axes[0].set_title('Band Sizes', fontsize=20)

axes[1].pie(album_sizes_combined.values(), labels=album_sizes_combined.keys(), startangle=90)
axes[1].set_title('Album Sizes', fontsize=20)

plt.tight_layout()
plt.savefig('task3_pie_charts.png')

# Task 4
filtered_bands = {band: count for band, count in band_album_counts.items() if count >= 5}

plt.figure(figsize=(10, 6))
plt.barh(list(filtered_bands.keys()), list(filtered_bands.values()))
plt.title('Number of Albums Released by Bands')
plt.tight_layout()
plt.savefig('task4_albums.png')

# Task 5
plt.figure(figsize=(12, 6))
for band_name in filtered_bands:
    years_list = band_album_years[band_name]
    if years_list:
        plt.barh([band_name] * len(years_list), [1] * len(years_list), left=years_list, color='black')

plt.title('Album Releases by Bands by Year')
plt.tight_layout()
plt.savefig('task5_album_gantt.png')