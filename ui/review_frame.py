# ui/review_frame.py
import tkinter as tk

class ReviewFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        label = tk.Label(self, text="Đây là giao diện ôn tập từ")
        label.pack(pady=20)
