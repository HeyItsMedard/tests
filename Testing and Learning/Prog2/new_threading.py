import threading
import time

class TodoListManager:
    def __init__(self, filename, reminder_sec):
        self.text = ""
        self.filename = filename
        self.reminder_sec = reminder_sec
        self.lock = threading.Lock()

    def save_txt_reminder(self):
        while True:
            time.sleep(self.reminder_sec)
            print("\nRég volt mentésed. Szeretnél menteni a txt fájlba?")
            is_save = input("Y/N: ").strip().upper() == "Y"
            if is_save:
                with self.lock:
                    self.save_to_txt(self.text)
                new_set_reminder = self.set_reminder()
                self.reminder_sec = new_set_reminder if new_set_reminder is not None else 10 # default adunk neki 10-et
            else:
                print("\nNincs mentés.\n")
                new_set_reminder = self.set_reminder()
                self.reminder_sec = new_set_reminder if new_set_reminder is not None else 10 

    def set_reminder(self):
        with self.lock:
            try:
                new_reminder_sec = int(input("\nEmlékeztető állítása másodpercben: "))
                if 0 < new_reminder_sec <= 600: # 10 perc max
                    return new_reminder_sec
                return None
            except ValueError:
                return None

    def save_to_txt(self, todo_text):
        with open(self.filename, "w", encoding="utf-8") as file:
            file.write(todo_text)
        print("\nSzöveg elmentve todothread.txt-be.")

    def run(self):
        timer_thread = threading.Thread(target=self.save_txt_reminder, daemon=True) # daemon nem akadályozza a program kiléptetését, háttérben fut, miközben kedvünkre tevékenykedhetünk.
        timer_thread.start()

        print("A sor alá írhatod a tennivalókat Todo: szöveg mellé, ESC beírásával kilép, SAVE-vel ment, üres inputot nem ment, SETre beállít vagy változtat értéket: \n") # SETet nem írtam meg

        while True: # case is lehet if you fancy
            uinput = input("Todo: ")
            if uinput == "ESC":
                break
            elif uinput == "SAVE":
                with self.lock:
                    self.save_to_txt(self.text)
            elif uinput == "":
                pass
            else:
                with self.lock:
                    self.text += "[ ] " + uinput + "\n"

if __name__ == "__main__":
    filename = "Testing and Learning/Prog2/todothread.txt"
    reminder_sec = 10
    manager = TodoListManager(filename, reminder_sec)
    manager.run()
