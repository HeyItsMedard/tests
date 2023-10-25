import json
import os

HELP = "README.md"
DATABASE_FILE = "trending.json"
json_file_names = [filename for filename in os.listdir() if filename.endswith('.json')]

def read_from_file(filename: str):
    with open(filename, encoding="utf8") as db:
        data = json.load(db)
    return data

data = read_from_file(DATABASE_FILE)
# for i, question in enumerate(data, 1):
#     print(f"\n{i}. kérdés: {question['question']}")

def help():
    with open(HELP, "r", encoding="utf-8") as file:
        content = file.read()
    print(content)

def write_to_file(filename: str, data):
    with open(filename, 'w', encoding="utf8") as update:
        json.dump(data, update, ensure_ascii=False, indent=4)

def check_answer(length: int, answer: str):
    while not answer.isdigit() or int(answer) > length or int(answer) < 0:
        answer = (input(f"Számot kell megadj 0-tól {length}-ig.\nSzám: "))
    return answer

def confirm_deletion(answer: str, where):
    print(where[int(answer)-1])
    confirm = input("Biztos szeretnéd törölni az adatot? I/N\nSzöveges bevitel: ")
    if any(confirm.lower() == valid_input.lower() for valid_input in ["igen", "I", "igaz"]):
        del where[int(answer)-1]
        print("Succesfully deleted.")
        write_to_file(DATABASE_FILE, data)

def get_answer():
    print("Válassz témát (0 - ESC):")
    for i, jsonf in enumerate(json_file_names, 1):
        print(f"{i}) {(jsonf.split('.')[0]).capitalize()}")
    answer = input("Szám: ")
    answer = check_answer(len(json_file_names), answer)
    return answer

def get_topic_file(answer):
    return read_from_file(json_file_names[int(answer)-1])

def get_topic_name(answer):
    return json_file_names[int(answer)-1].split('.')[0].lower()

def delete_data():
    while True:
        print("""
Mit szeretnél törölni?
1 - Tartalomgyártó
2 - Videó
0 - Kilépés""")
        num_vid = input("Szám: ")
        num_vid = check_answer(2, num_vid)

        if num_vid != "0": 
            print("Melyik tartalomgyártó? (0 - ESC)")
            for i, creator in enumerate(data, 1):
                print(f"{i}) {creator['creator']}")
            answer = input("Szám: ")
            answer = check_answer(len(data), answer)
            if answer == '0':
                print("Visszatérés főmenübe...")
                return

            if num_vid == '1':
                confirm_deletion(answer, data)
        
            if num_vid == '2':
                get_creator = data[int(answer)-1]
                print("Melyik videó? (0 - ESC)")
                for i, video in enumerate(get_creator['contents'], 1):
                    for key_title in video.keys():
                        print(f"{i}) {key_title}")
                answer = input("Szám: ")
                if answer == '0':
                    print("Visszatérés főmenübe...")
                    return
                answer = check_answer(len(get_creator['contents']), answer)
                confirm_deletion(answer, get_creator['contents'])
        
        else:
            print("Visszatérés főmenübe...")
            return
        