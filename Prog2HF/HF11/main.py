import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

import random
import threading
import time
import io

# Note to reader/reviewer: set your own 'rounds' in load_next_question() if you insist (100 max)
# I requested the page 5 times due to item limit of 20 per page - you could request more if you wish
# but it will take longer to load the game if you set it higher of course

class RickAndMortyQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Rick and Morty Quiz")
        self.root.resizable(False, False)

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=5)

        self.score_label = tk.Label(root, text="Score: 0/0", font=("Arial", 10))
        self.score_label.pack()

        self.options_frame = tk.Frame(root)
        self.options_frame.pack(pady=5)

        self.characters = []
        self.used_characters = []
        self.current_character = None # whole character object
        self.correct_answer = None # character name
        self.score = {"correct": 0, "total": 0}

        self.requested_pages = set()
        # Because results only contain 20 characters, I request 5 pages to get a decent variation of characters
        for _ in range(5):
            page_number = random.randint(1, 42)
            while page_number in self.requested_pages:
                page_number = random.randint(1, 42)
            characters_on_page = self.get_characters_on_page(page_number)
            self.characters.extend(characters_on_page)

        self.load_next_question()

    def get_characters_on_page(self, page_number):
        try:
            response = requests.get(f"https://rickandmortyapi.com/api/character/?page={page_number}")
            data = response.json()
            return data["results"]
        except requests.RequestException as e: # could happen if we give a bad page number
            messagebox.showerror("Error", f"Error fetching data: {e}")

    def load_next_question(self):
        if not self.characters:
            messagebox.showinfo("Game Over", "No characters available. Game over.")
            self.root.destroy()

        unused_characters = [character for character in self.characters if character not in self.used_characters]

        if len(self.used_characters) == 10: # Note to reader: set your own 'rounds' here
            messagebox.showinfo("Game Over", f"Game Over! Score: {self.score['correct']}/{self.score['total']}")
            self.root.destroy()
        
        # gets a random character from the list of unused characters, sets it as the right answer and displays it
        self.current_character = random.choice(unused_characters)
        self.used_characters.append(self.current_character)
        self.correct_answer = self.current_character["name"]

        image_url = self.current_character["image"]
        image = self.load_image(image_url)
        self.display_image(image)

        self.display_options()

        # Disable buttons for 3 seconds to prevent input during answer display
        self.disable_buttons()
        threading.Thread(target=self.enable_buttons, daemon=True).start()

    def load_image(self, url):
        response = requests.get(url)
        image = Image.open(io.BytesIO(response.content))
        return ImageTk.PhotoImage(image)

    def display_image(self, image):
        self.image_label.config(image=image)
        self.image_label.image = image

    def display_options(self):
        # we pass the correct answer to the options list first
        options = [self.correct_answer]
        # then we add 3 random names to the list 
        while len(options) < 4:
            random_character = random.choice(self.characters)
            random_name = random_character["name"]
            if random_name not in options:
                options.append(random_name)
        
        # shuffle the options so the correct answer isn't always the first option
        random.shuffle(options)

        # Displays buttons with the options, and binds selected to the check_answer method
        for i in range(4):
            button = tk.Button(self.options_frame, text=options[i], command=lambda selected_index=i: self.check_answer(selected_index))
            button.grid(row=i, column=0, pady=5)

    def disable_buttons(self):
        for child in self.options_frame.winfo_children(): # lists all widgets in options_frame
            child.config(state=tk.DISABLED) # disables all widgets so they can't be clicked

    def enable_buttons(self):
        for child in self.options_frame.winfo_children():
            child.config(state=tk.NORMAL) # enables all widgets so they can be clicked

    def check_answer(self, selected_index):
        # Getting text from selecxcted button and comparing it to the correct answer
        selected_answer = self.options_frame.winfo_children()[selected_index].cget("text")
        if selected_answer == self.correct_answer:
            self.score["correct"] += 1
        self.score["total"] += 1
        self.update_score_label()
        self.display_correct_answer()
        self.disable_buttons()
        threading.Thread(target=self.reset_options_frame, daemon=True).start()

    def update_score_label(self):
        # Displayed below image at all times
        score_text = f"Score: {self.score['correct']}/{self.score['total']}"
        self.score_label.config(text=score_text)

    def display_correct_answer(self):
        # Displayed at the bottom of the window when user selects an option
        correct_label = tk.Label(self.options_frame, text=f"Correct answer: {self.correct_answer}", font=("Arial", 12))
        correct_label.grid(row=4, column=0, pady=10)

    def reset_options_frame(self):
        # Leaving some time for the user to read the correct answer, then resetting the frame for next round
        time.sleep(3)
        self.options_frame.destroy()
        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack(pady=5)
        self.load_next_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = RickAndMortyQuiz(root)
    root.mainloop()