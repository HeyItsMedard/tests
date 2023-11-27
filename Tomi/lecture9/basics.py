from tkinter import *
# from tkinter.ttk import *
import tkinter
window = Tk()
# widget Label, Button, Entry, Text, Frame
# label = Label(text="Hello world", fg="black", bg="white")
# label.pack()

# button = Button(text="Click me", width=25, height=5, bg="blue", fg="green")
# button.pack()

# entry = Entry(fg="yellow", bg="blue", width=50)
# entry.pack()
# entry.delete(0, END)
# entry.insert(0, 'Hello')

# effects = {
#     "flat": FLAT,
#     "sunken": SUNKEN,
#     "raised": RAISED,
#     "groove": GROOVE,
#     "ridge": RIDGE
# }

# for name, relief in effects.items():
#     frame = Frame(master=window, relief=relief, borderwidth=5)
#     frame.pack()
#     label = Label(master=frame, text=name)
#     label.pack()

# frame1 = Frame(master=window, width=100, height=100, bg="red")
# frame1.pack(fill=BOTH, side=LEFT, expand=True)
# frame2 = Frame(master=window, width=50, height=50, bg="yellow")
# frame2.pack(fill=BOTH, side=LEFT, expand=True)
# frame3 = Frame(master=window, width=25, height=25, bg="blue")
# frame3.pack(fill=BOTH, side=LEFT, expand=True)

# frame = Frame(master=window, width=150, height=150)
# frame.pack()

# label1 = Label(text="hello", bg="red", master=frame)
# label1.place(x=0, y=0)

# label2 = Label(text="world", bg="yellow", master=frame)
# label2.place(x=75, y=75)


# def handle_press(event):
#     print(event.char)


# window.bind('<Key>', handle_press)

# def handle_click():
#     print('clicked me')

# button = Button(text="Click me", height=25, width=50)
# button.bind('<Button-3>', handle_click)
# button.pack()

# button = Button(text="Click me", height=25, width=50, command=handle_click)
# button.pack()


def decrease():
    number = int(value['text'])
    number -= 1
    value['text'] = str(number)

def increase():
    value['text'] = f"{int(value['text']) + 1}"

dec_button = Button(text="-", command=decrease)
value = Label(text="0")
incr_button = Button(text="+", command=increase)

dec_button.pack(side=LEFT)
value.pack(side=LEFT)
incr_button.pack(side=LEFT)

window.mainloop()
