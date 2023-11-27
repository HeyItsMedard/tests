import tkinter as tk
from tkinter import messagebox

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Tkinter App")
        self.geometry("400x300")

        self.menubar = tk.Menu(self)

        self.filemenu = tk.Menu(self.menubar, tearoff=0) # tearoff=0 means the menu can't be torn off
        self.filemenu.add_command(label="Close", command=self.on_close)
        self.filemenu.add_separator() # adds a separator line
        self.filemenu.add_command(label="Close Immediately", command=self.destroy)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Doing nothing", command=lambda: print("Doing nothing")) # lambda is a way to create a function without a name
        self.actionmenu.add_command(label="Show Message", command=self.show_message) # same as button

        self.menubar.add_cascade(label="File", menu=self.filemenu) # label="File" is the default
        self.menubar.add_cascade(label="Action", menu=self.actionmenu)

        self.config(menu=self.menubar)
        
        self.label = tk.Label(self, text="Hello, Tkinter", font=("Arial", 18)) # self is the master widget (with root, it's self.root)

        self.textbox = tk.Text(self, font=("Arial", 12), height=5, width=30)
        self.textbox.bind("<KeyPress>", self.shortcut) # bind() is used to bind an event to a function
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar() # IntVar is a special Tkinter variable that can be used to store integers, in this case, 0 or 1

        self.check = tk.Checkbutton(self, text="Check me!", font=("Arial", 12), variable=self.check_state) 
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self, text="Click me!", font=("Arial", 12), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clearbtn = tk.Button(self, text="Clear", font=("Arial", 12), command=lambda: self.textbox.delete('1.0', tk.END))
        self.clearbtn.pack(padx=10, pady=10)
        
        self.protocol("WM_DELETE_WINDOW", self.on_close) # protocol() is used to bind an event to a function
    
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END)) #from start to finish
        else:
            messagebox.showinfo("Message", message=self.textbox.get('1.0', tk.END)) #title='Message' is the default

    def shortcut(self, event):
        # print(event.keysym) # keysym is the name of the key that was pressed
        # print(event.state) # state is a bitmask of the modifier keys that were pressed (shift, ctrl, alt, etc.)
        if event.state == 12 and event.keysym == "Return":
            self.show_message()
        # keysym can be "Return", "BackSpace", "Delete", "Up", "Down", "Left", "Right", "Home", "End", "Page_Up", "Page_Down", "Escape", "Tab", "F1", "F2", etc.
        # state can be 4 (control), 1 (shift), 8 (alt), 12 (control+alt), 16 (num lock), 20 (caps lock), 36 (shift+alt), 40 (shift+alt+control), etc.

    def on_close(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.destroy()

    def run(self):
        self.mainloop()

# You can also do this:
# class MyApp:
#     def __init__(self):
#         self.root = tk.Tk() etc.
#         now we will use root everywhere instead of self

if __name__ == "__main__":
    app = MyApp()
    app.run()
