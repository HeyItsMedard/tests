import tkinter as tk

# Create the main window
# IMPORTANT: root is the master widget. All other widgets must be children of root.
# This is why we pass root as the first argument to the Label constructor below.
root = tk.Tk()
root.geometry("600x800")
root.title("My first GUI app")

# IMPORTANT: The main window must be created before any widgets.
# Widgets are things like buttons, text boxes, labels, etc.

# Create and pack the label inside the main window
label = tk.Label(root, text="Hello, Tkinter", font=("Times New Roman", 24))
label.pack(padx=20, pady=20) # padx and pady add padding (space) around the label

# Create and pack the text box inside the main window
textbox = tk.Text(root, height=10, width=50) # height and width are in characters (not pixels)
textbox.pack()

myentry = tk.Entry(root, width=50)
myentry.pack(pady=20)

button = tk.Button(root, text="Click me!", command=lambda: print("You clicked me!"))
button.pack()

buttonframe = tk.Frame(root, )
buttonframe.columnconfigure(0, weight=1) # weight determines how much space the column takes up
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=("Times New Roman", 18))
btn1.grid(row=0, column=0, sticky="nsew") # sticky="nsew" means the button will stretch to fill the cell north-south and east-west
# You could write sticky="ns" to make it stretch only north-south, or sticky="ew" to make it stretch only east-west
# You could also write it like this: tk.W+tk.E+tk.N+tk.S
btn2 = tk.Button(buttonframe, text="2", font=("Times New Roman", 18))
btn2.grid(row=0, column=1, sticky="nsew")
btn3 = tk.Button(buttonframe, text="3", font=("Times New Roman", 18))
btn3.grid(row=0, column=2, sticky="nsew")
btn4 = tk.Button(buttonframe, text="4", font=("Times New Roman", 18))
btn4.grid(row=1, column=0, sticky="nsew")
btn5 = tk.Button(buttonframe, text="5", font=("Times New Roman", 18))
btn5.grid(row=1, column=1, sticky="nsew")
btn6 = tk.Button(buttonframe, text="6", font=("Times New Roman", 18))
btn6.grid(row=1, column=2, sticky="nsew")

buttonframe.pack(fill="both", expand=True) # fill="both" means the frame will stretch to fill the main window
# expand=True means the frame will expand to fill any extra space in the main window
# bad fill style "_": must be none, x, y, or both
# bad expand style "_": must be True or False

anotherbtn = tk.Button(root, text="Another button")
anotherbtn.place(x=100, y=100, height=100, width=100) # place() is another way to position widgets (instead of pack() or grid(), manually) - it's ugly and not recommended

# Start the main event loop
# IMPORTANT: root.mainloop() must be the last line of code in your program.
root.mainloop()
