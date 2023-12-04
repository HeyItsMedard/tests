import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
	def __init__(self, title, size):
		
		# main setup
		super().__init__()
		self.title(title)
		self.geometry(f'{size[0]}x{size[1]}')
		self.minsize(size[0],size[1])

		# widgets - self will turn into parent
		self.flag = Flag(self)

		# run 
		self.mainloop()

class Flag(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, background='red').pack(expand=True, fill='both')
        self.place(x=0, y=0, relwidth=1, relheight=1)  # upper side is filled 33% of the window - if there is no other label, relheight=1/3
        # if I want to fill "columnwise", relwidth=1/3
        ttk.Label(self, background='white').pack(expand=True, fill='both')
        self.place(x=1, y=0, relwidth=1, relheight=1)
        ttk.Label(self, background='green').pack(expand=True, fill='both')
        self.place(x=2, y=0, relwidth=1, relheight=1)

if __name__ == "__main__":
    App('Hungary', (600, 600))
    
	
