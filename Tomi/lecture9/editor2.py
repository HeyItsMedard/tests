import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
  filepath = askopenfilename(filetypes=[("Text Files", "*.txt"),("Python fiels", "*.py"), ("All Files", "*.*")])
  if not filepath:
    return
  edit.delete("1.0", tk.END)
  with open(filepath, mode="r", encoding="utf-8") as input_file:
    text = input_file.read()
    edit.insert(tk.END, text)
  window.title(f"Simple editor - {filepath}")


def save_file():
  filepath = asksaveasfilename(
    defaultextension=".txt", filetypes=[("Text Files", "*.txt"),("Python fiels", "*.py"), ("All Files", "*.*")]
  )
  if not filepath:
    return
  with open(filepath, mode="w", encoding="utf-8") as output_file:
    text = edit.get("1.0", tk.END)
    output_file.write(text)
  window.title(f"Simple editor - {filepath}")
window = tk.Tk()

edit = tk.Text(window)
buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(buttons, text="Open", command=open_file)
btn_save = tk.Button(buttons, text="Save as...", command=save_file)
btn_close = tk.Button(buttons, text="Close", command=window.destroy)

btn_open.pack(side=tk.TOP)
btn_save.pack(side=tk.TOP)
btn_close.pack(side=tk.BOTTOM)

buttons.pack(fill=tk.Y, side=tk.LEFT)
edit.pack(side=tk.LEFT)

window.mainloop()
