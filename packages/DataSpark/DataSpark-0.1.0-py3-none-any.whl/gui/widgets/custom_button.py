import tkinter as tk

class CustomButton(tk.Button):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg="lightblue", fg="black", relief=tk.RAISED)