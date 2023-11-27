import tkinter as tk
from tkinter import ttk

# tk.StringVar()
# tk.BooleanVar()
# tk.DoubleVar()
# tk.IntVar()

class App(tk.Tk):
  ERROR = "Error.TLabel"
  SUCCESS = "Success.TLabel"
  WARNING = "Warning.TLabel"

  def __init__(self):
    super().__init__()
    self.title('Password demo')
    self.geometry("300x150")

    self.password_v = tk.StringVar()
    self.confirm_password_v = tk.StringVar()

    self.confirm_password_v.trace("w", self.validate)

    self.columnconfigure([0, 1, 2], weight=1)

    self.style = ttk.Style(self)
    self.style.configure(self.ERROR, foreground="red")
    self.style.configure(self.SUCCESS, foreground="green")
    self.style.configure(self.WARNING, foreground="yellow")

    self.create_ui()

  def create_ui(self):
    padding = { 'padx': 5, 'pady': 5, "sticky": tk.W }

    self.message = ttk.Label(self)
    self.message.grid(column=0, row=0, columnspan=3, **padding)

    ttk.Label(self, text="Next password:").grid(column=0, row=1, **padding)

    password_entry = ttk.Entry(self, textvariable=self.password_v, show="*")
    password_entry.grid(column=1, row=1, **padding)
    password_entry.focus()

    ttk.Label(self, text='Confirm password: ').grid(column=0, row=2, **padding)

    confirm_entry = ttk.Entry(self, textvariable=self.confirm_password_v, show="*")
    confirm_entry.grid(column=1, row=2, **padding)

    submit_button = ttk.Button(self, text="Change")
    submit_button.grid(column=0, row=3, **padding)

  def validate(self, *args):
    password = self.password_v.get()
    confirm_password = self.confirm_password_v.get()

    if password == confirm_password:
      self.set_message("Success: The password looks ok", self.SUCCESS)
      return
    if password.startswith(confirm_password):
      self.set_message("Warning: Keep going", self.WARNING)

    if len(password) == len(confirm_password):
      self.set_message("Error: Passwords are different", self.ERROR)

  def set_message(self, message, type=None):
    self.message.config(text=message)
    if type:
      self.message['style'] = type


if __name__ == '__main__':
  app = App()
  app.mainloop()
