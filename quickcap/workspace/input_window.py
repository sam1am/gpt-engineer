import tkinter as tk
from datetime import datetime

class InputWindow(tk.Toplevel):
    def __init__(self, target_file):
        super().__init__()
        self.title("Input")
        self.geometry("300x200")

        self.text_input = tk.Text(self)
        self.text_input.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_text)
        self.submit_button.pack()

        self.cancel_button = tk.Button(self, text="Cancel", command=self.cancel)
        self.cancel_button.pack()

        self.target_file = target_file

    def submit_text(self):
        with open(self.target_file, "a") as file:
            file.write(f"--- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(self.text_input.get("1.0", tk.END))
        self.destroy()

    def cancel(self):
        self.destroy()
