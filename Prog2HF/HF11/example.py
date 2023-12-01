import tkinter as tk
from io import BytesIO

import requests
from PIL import Image, ImageTk

root = tk.Tk()
response = requests.get("https://rickandmortyapi.com/api/character/avatar/1.jpeg")
raw_data = response.content
# read image with Pillow
img = Image.open(BytesIO(raw_data))
# convert image to Tkinter-compatible object
# note: you must keep a reference to this object to avoid its garbage collection
img_tk = ImageTk.PhotoImage(img)
img_label = tk.Label(root, image=img_tk)
img_label.pack()
root.mainloop()
