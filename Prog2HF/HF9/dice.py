import tkinter as tk
import random

faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")

        self.label = tk.Label(self, text="", font=("Helvetica", 58), wraplength=600)
        self.label.pack(side="top", fill="both", expand=True, anchor="center")

        self.dobokockak_szama = tk.IntVar()
        self.dobokockak_szama.set(1)

        self.sum_label = tk.Label(self, text="Sum = -", font=("Helvetica", 10))
        self.sum_label.pack(side="top", fill="both", expand=False, anchor="center")

        # 28 a maximum dobókockák szama, amit meg tud jeleníteni az ablak widget elcsúszása nélkül
        self.dobokockak_spinbox = tk.Spinbox(self, from_=1, to=28, textvariable=self.dobokockak_szama, command=self.roll) 
        self.dobokockak_spinbox.pack(side="left", fill="both", expand=False, anchor="center")

        self.dobasok_gomb = tk.Button(self, text="Reroll", command=self.roll)
        self.dobasok_gomb.pack(side="right", fill="both", expand=True, anchor="center")

    def draw_dice(self, dobokockak_szama):
        eredmeny_indexek = [random.randint(1, len(faces)) for _ in range(dobokockak_szama)]
        eredmeny = [faces[i-1] for i in eredmeny_indexek]
        eredmeny_str = " ".join(eredmeny)
        self.label.config(text=eredmeny_str)

        sum_eredmeny = sum(eredmeny_indexek)
        self.sum_label.config(text=f"Sum = {sum_eredmeny}")

    def roll(self):
        self.draw_dice(self.dobokockak_szama.get())
    
    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
