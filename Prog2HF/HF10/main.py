import tkinter as tk

from rating import Rating

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        tk.Label(self, text="Értékelje a terméket az alábbi szempontok szerint!").pack()

        self.rating_frame = tk.Frame(self)
        self.rating_frame.pack(expand=True, fill="both")
        self.rating_objects = []

        self.create_default_ratings() # egy helyen preset kategóriák létrehozása

        self.average = tk.Label(self, text="Átlag: -")
        self.average.pack(fill="both")

        self.adding_frame = tk.Frame(self)
        self.adding_frame.pack(side="bottom", fill="x")
        tk.Label(self.adding_frame, text="Új szempont hozzáadása").pack()
        tk.Label(self.adding_frame, text="Megnevezés:").pack(side="left")
        self.new_rating = tk.Entry(self.adding_frame)
        self.new_rating.pack(side="left", fill="x", expand=True)
        tk.Label(self.adding_frame, text="Skála mérete:").pack(side="left")
        self.spinbox = tk.Spinbox(
            self.adding_frame, from_=2, to=10, textvariable=tk.IntVar(self, 5)
        )
        self.spinbox.pack(side="left")
        tk.Button(self.adding_frame, text="Hozzáad", command=self.add_new_rating).pack(side="left")

    def create_default_ratings(self):
        categories = ["Ár/érték arány", "Íz", "Csomagolás"]
        for category in categories:
            rating = Rating(self.rating_frame, category, callback=self.update_average)
            rating.pack()
            self.rating_objects.append(rating)

    def add_new_rating(self):
        new_category = self.new_rating.get()
        scale_size = int(self.spinbox.get())
        new_rating = Rating(self.rating_frame, new_category, n_options=scale_size, callback=self.update_average)
        new_rating.pack()
        self.rating_objects.append(new_rating)
        
    def update_average(self, category, average): #összegzés és kiszámítás
        averages = [rating.var.get() for rating in self.rating_objects]
        valid_averages = [value for value in averages if value != 0] # selected only
        final_average = sum(valid_averages) / len(valid_averages) if valid_averages else "-"
        self.average.config(text=f"Átlag: {final_average}")
        

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    app = App(root)
    app.pack(expand=True, fill="both")
    root.mainloop()