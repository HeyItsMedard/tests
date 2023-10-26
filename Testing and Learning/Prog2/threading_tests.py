"""Sleep"""
from threading import Thread, Lock
from time import sleep
def question_func():
    input("Please give an answer: ")# vár választ
    sleep(3) # elmegy aludni
    print('Printing...') # 3 ms után kiírja a printet
    
calling = Thread(target=question_func)
uinput = input("Futtatni szeretnéd a sleep testet? Y/N: ")
if uinput == 'Y':
    calling.start()

"""Ezt végül megírtam inkább new_threading.pyban szebben, lockkal, classal, nézd azt."""
text = ""
filename = "Testing and Learning\Prog2\\todothread.txt"
reminder_sec = 10
def save_txt_reminder():
    global text # globalt használunk, így thread targetnél nem kell arg, meg mert amúgy is hasznosabb
    global reminder_sec
    while True:
        sleep(reminder_sec)
        print("\nRég volt mentésed. Szeretnél menteni a txt fájlba?")
        isSave = True if input("Y/N: ").strip().upper() == "Y" else False
        if isSave:
            save_to_txt(text)
            new_set_reminder = set_reminder()
            reminder_sec = new_set_reminder if new_set_reminder is not None else 10
        else:
            print("\nNincs mentés.\n")
            new_set_reminder = set_reminder()
            reminder_sec = new_set_reminder if new_set_reminder is not None else 10
            
def set_reminder():
    try:
        new_reminder_sec = int(input("\nEmlékeztető állítása másodpercben: "))
        if new_reminder_sec > 0 and new_reminder_sec <= 600: # 10 perces max
            return new_reminder_sec
        return None
    except:
        return None
    
def save_to_txt(todo_text):
    with open(filename, "w", encoding="utf-8") as file:
            file.write(todo_text)
            print("\nSzöveg elmentve todothread.txt-be.")

timer_thread = Thread(target=save_txt_reminder, daemon=True) # daemon nem akadályozza a program kiléptetését, háttérben fut, miközben kedvünkre tevékenykedhetünk.
timer_thread.start()
print("A sor alá írhatod a tennivalókat Todo: szöveg mellé, ESC beírásával kilép, SAVE-vel ment, üres inputot nem ment, SETre beállít vagy változtat értéket: \n") # SETet nem írtam meg
while True:
    uinput = input("Todo: ")
    if uinput == "ESC":
        break
    elif uinput == "SAVE":
        save_to_txt(text)
    elif uinput == "":
        pass
    else:
        text += "[ ] " + uinput + "\n"
# nem vagyok túl büszke rá, nem szép, de több mint a semmi