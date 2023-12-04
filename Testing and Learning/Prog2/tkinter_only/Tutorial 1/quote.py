import tkinter as tk
import requests
import threading

"A seamless quote generator using the quotable API"
class QuoteGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quote Generator")
        self.geometry("900x260")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)

        self.quotes = []
        self.quote_number = 0

        self.quote_label = tk.Label(self, text="Click the button to generate a quote!", height=6, pady=10, wraplength=600)
        self.quote_label.grid(row=0, column=0, sticky="we", padx=20, pady=10)

        button = tk.Button(self, text="Generate Quote", command=self.update_quote, activebackground="grey", bg="#0052cc", fg="#ffffff")
        button.grid(row=1, column=0, sticky="s", padx=20, pady=10)

        threading.Thread(target=self.fetch_quote, daemon=True).start()

    def fetch_quote(self):
        for i in range(10):
            response = requests.get("https://api.quotable.io/random")
            content = response.json()["content"]
            author = response.json()["author"]
            quote = f"{content}\n\n- {author}"
            self.quotes.append(quote)
            print(f"{i}. fetched quote")
        print("Quotes fetched!")

    def update_quote(self):
        self.quote_label.config(text=self.quotes[self.quote_number])
        self.quote_number += 1
        print(self.quote_number)

        if self.quote_number == len(self.quotes) - 2:
            print("Fetching more quotes...")
            threading.Thread(target=self.fetch_quote, daemon=True).start()

if __name__ == "__main__":
    app = QuoteGenerator()
    app.mainloop()
