import tkinter as tk
from tkinter import ttk
import requests
import json
import threading
from PIL import Image, ImageTk
import io

SETTINGS_PATH = "Prog2HF/ZH2/settings.json"

class OptionFrame(tk.Frame):
    def __init__(self, master, option_data, vote_callback, server_url):
        super().__init__(master)
        self.server_url = server_url
        self.option_data = option_data
        self.vote_callback = vote_callback

        image_url = f"{self.server_url}/static/img/{self.option_data['id']}.jpg"
        image = self.load_image(image_url)

        self.image_label = tk.Label(self, image=image)
        self.image_label.image = image
        self.image_label.grid(row=0, column=0, rowspan=4, sticky="w")

        name_label = tk.Label(self, text=self.option_data['name'])
        name_label.grid(row=0, column=1, sticky="w")

        vote_button = tk.Button(self, text="Szavazok", command=self.vote)
        vote_button.grid(row=0, column=3, sticky="e")

        self.progressbar = ttk.Progressbar(self, orient=tk.HORIZONTAL, mode='determinate')
        self.progressbar.grid(row=2, column=1, rowspan=2, columnspan=2, sticky="ew", pady=(0, 5))

        self.percentage_label = tk.Label(self, text='', anchor="e")
        self.percentage_label.grid(row=2, column=3, sticky="e")

        self.vote_button = vote_button

    def load_image(self, img_url):
        response = requests.get(img_url)
        img_data = response.content
        image = Image.open(io.BytesIO(img_data))
        photo = ImageTk.PhotoImage(image)
        return photo

    def update_data(self, votes_percentage):
        self.progressbar['value'] = votes_percentage
        self.percentage_label.config(text=f"{votes_percentage:.2f}%")

    def vote(self):
        self.vote_button.config(state=tk.DISABLED)
        self.vote_callback(self.option_data['id'])

class VotingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.server_url = ""
        self.question = None
        self.options = []

        self.geometry("400x500")
        self.resizable(False, False)
        self.options_frame = ttk.Frame(self)
        self.options_frame.pack()

        self.load_settings()

        threading.Thread(target=self.update_data, daemon=True).start()

    def load_settings(self):
        with open(SETTINGS_PATH, "r", encoding='utf8') as settings_file:
            settings_data = json.load(settings_file)
            self.voted_on = settings_data["voted_on"]
            self.server_url = settings_data["server_url"]

    def save_settings(self):
        with open(SETTINGS_PATH, "w", encoding='utf8') as settings_file:
            settings_data = {"voted_on": self.question, "server_url": self.server_url}
            json.dump(settings_data, settings_file, ensure_ascii=False)

    def load_votes_data(self):
        response = requests.get(f"{self.server_url}/results")
        votes_data = response.json()
        if votes_data['question'] != self.question:
            # print("entered")
            self.question = votes_data['question']
            self.title(self.question)
            self.options_frame.destroy()
            self.options_frame = ttk.Frame(self)
            self.options_frame.pack()

            for option_data in votes_data['candidates']:
                option_frame = OptionFrame(self.options_frame, option_data, self.vote_callback, self.server_url)
                option_frame.pack(side=tk.TOP, padx=5, pady=5)
                self.options.append(option_frame)
            print(self.question, self.voted_on)
            if self.question == self.voted_on:
                self.disable_vote_buttons()

        self.update_frames(votes_data)

    def update_data(self):
        while True:
            self.load_votes_data()
            # print('running')
            self.after(1000)

    def update_frames(self, votes_data):
        total_votes = sum(candidate['votes'] for candidate in votes_data['candidates'])

        for option_frame in self.options:
            for option_data in votes_data['candidates']:
                if option_data["id"] == option_frame.option_data["id"]:
                    votes_percentage = (option_data['votes'] / total_votes) * 100 if total_votes != 0 else 0
                    option_frame.update_data(votes_percentage)

    def vote_callback(self, option_id):
        if self.voted_on == self.question:
            return

        payload = {"candidate_id": option_id}
        response = requests.post(f"{self.server_url}/vote", json=payload)

        if response.status_code == 200:
            # print("Successful vote")
            self.voted_on = self.question
            self.save_settings()
            self.disable_vote_buttons()
            self.load_votes_data()

    def disable_vote_buttons(self):
        for option_frame in self.options:
            option_frame.vote_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = VotingApp()
    app.mainloop()
