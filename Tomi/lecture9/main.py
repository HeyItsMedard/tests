# temperature converter
# ℉ -> ℃
import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.title("Temperature converter")
window.resizable(width=False, height=False)

frame = ttk.Frame(master=window, padding=10)

def fahrenheit_to_celsius():
  fahrenheit = entry.get()
  celsius = (5/9) * (float(fahrenheit) - 32)
  result['text'] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

entry = tk.Entry(master=frame, width=10)
label_fahrenheit = tk.Label(master=frame, text="\N{DEGREE FAHRENHEIT}")
button = tk.Button(master=frame, text="->", command=fahrenheit_to_celsius)
result = tk.Label(master=frame, text="\N{DEGREE CELSIUS}")

entry.pack(side=tk.LEFT)
label_fahrenheit.pack(side=tk.LEFT)
button.pack(side=tk.LEFT)
result.pack(side=tk.LEFT)

frame.pack()

window.mainloop()
