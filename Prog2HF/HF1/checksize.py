import os
import json
import pickle


json_file_path = 'file_stats.json'
pickle_file_path = 'file_stats.pkl'


if os.path.exists(json_file_path) and os.path.exists(pickle_file_path):

    with open(json_file_path, 'r') as json_file:
        json_data = json_file.read()
    json_size = len(json_data)

    with open(pickle_file_path, 'rb') as pickle_file:
        pickle_data = pickle_file.read()
    pickle_size = len(pickle_data)

    if json_size < pickle_size:
        print(f"pickle")
    elif json_size > pickle_size:
        print(f"json") # valóban kisebb a pickle
    else:
        print(f"same")
else:
    print("error")