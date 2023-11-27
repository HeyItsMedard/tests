import tkinter as tk

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Simple stringvar")
    self.geometry("300x80")

    self.name = tk.StringVar()

    self.columnconfigure([0, 1, 2], weight=1)

    self.create_ui()

  def create_ui(self):
    padding = { 'padx': 5, 'pady': 5 }

    tk.Label(self, text="Name: ").grid(column=0, row=0, **padding)

    name_entry = tk.Entry(self, textvariable=self.name)
    name_entry.grid(column=1, row=0, **padding)
    name_entry.focus()

    submit_button = tk.Button(self, text="Submit", command=self.submit)
    submit_button.grid(column=2, row=0, **padding)

    self.out_label = tk.Label(self)
    self.out_label.grid(column=0, row=1, columnspan=3, **padding)

  def submit(self):
    self.out_label.config(text=self.name.get())


if __name__ == '__main__':
  app = App()
  app.mainloop()
