import tkinter as tk
from tkinter import filedialog

class ConfigWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Configuration")
        self.geometry("300x200")

        self.shortcut_label = tk.Label(self, text="Shortcut:")
        self.shortcut_label.pack()

        self.shortcut_entry = tk.Entry(self)
        self.shortcut_entry.pack()

        self.file_label = tk.Label(self, text="Target file:")
        self.file_label.pack()

        self.file_button = tk.Button(self, text="Choose file", command=self.choose_file)
        self.file_button.pack()

        self.save_button = tk.Button(self, text="Save", command=self.save_config)
        self.save_button.pack()

        self.target_file = None

    def choose_file(self):
        self.target_file = filedialog.askopenfilename()

    def save_config(self):
        with open("config.txt", "w") as config_file:
            config_file.write(f"{self.shortcut_entry.get()}\n{self.target_file}")

    def load_config(self):
        try:
            with open("config.txt", "r") as config_file:
                shortcut, target_file = config_file.read().splitlines()
                self.shortcut_entry.insert(0, shortcut)
                self.target_file = target_file
        except FileNotFoundError:
            pass
