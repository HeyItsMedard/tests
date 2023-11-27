import tkinter as tk


class Rating(tk.Frame):
    def __init__(self, master, text, n_options=5, callback=None):
        super().__init__(master)
        self.var = tk.IntVar(self)
        self.text = text
        self.n_options = n_options
        self.callback = callback
        label = tk.Label(self, text=text)
        label.grid(row=0, column=0, columnspan=n_options, sticky='w')
        self.buttons = []
        for i in range(n_options):
            button = tk.Radiobutton(self, text=str(i + 1), variable=self.var, value=i + 1, command=self.update_average)
            button.grid(row=1, column=i)
            self.buttons.append(button)

        tk.Button(self, text="Törlés", command=self.clear_selection).grid(row=1, column=n_options, padx=5)

    def update_average(self): #változások kezelése
        selected_value = [int(button["text"]) for button in self.buttons if self.var.get() == int(button["text"])]
        average = sum(selected_value) if selected_value else 0
        self.callback(self.text, average)

    def clear_selection(self):
        self.var.set(0)
        self.callback(self.text, "-")
