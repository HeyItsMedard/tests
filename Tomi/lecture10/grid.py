from tkinter import *
from functools import partial
window = Tk()

# rowconfigure(index, weight, minsize)
# columnconfigure(index, weight, minsize)

def on_press(i, j):
  print(f"clicked on {i}:{j} button")


# for i in range(3):
#   window.rowconfigure(i, weight=1, minsize=50)
#   window.columnconfigure(i, weight=1, minsize=75)
#   for j in range(3):
#     frame = Frame(master=window, relief=RAISED, borderwidth=1)
#     frame.grid(row=i, column=j, padx=5, pady=5)
#     button = Button(master=frame, text=f"Row {i}\nColumn{j}", command=partial(on_press, i, j))
#     button.pack(padx=5, pady=5)

window.columnconfigure([0, 1, 2, 3], minsize=50)
window.rowconfigure(0, minsize=50)

label1 = Label(text=1, bg="black", fg="white")
label2 = Label(text=2, bg="black", fg="white")
label3 = Label(text=3, bg="black", fg="white")
label4 = Label(text=4, bg="black", fg="white")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky="ns") # fill=Y
label3.grid(row=0, column=2, sticky="ew") # fill=X
label4.grid(row=0, column=3, sticky="news") # fill=BOTH

window.mainloop()
