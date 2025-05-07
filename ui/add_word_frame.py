# ui/add_word_frame.py

import tkinter as tk
from tkinter import messagebox
from models.vocabulary import Vocabulary
from database.db import save_vocab_list, load_vocab_list


class AddWordFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.vocab_list = load_vocab_list()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Từ vựng:").pack()
        self.word_entry = tk.Entry(self)
        self.word_entry.pack()

        tk.Label(self, text="Ý nghĩa:").pack()
        self.meaning_entry = tk.Entry(self)
        self.meaning_entry.pack()

        tk.Button(self, text="Lưu", command=self.save_word).pack(pady=10)

    def save_word(self):
        word = self.word_entry.get()
        meaning = self.meaning_entry.get()

        if word and meaning:
            new_word = Vocabulary(word, meaning)
            self.vocab_list.append(new_word)
            save_vocab_list(self.vocab_list)
            messagebox.showinfo("Thành công", f"Đã lưu từ: {word}")
            self.word_entry.delete(0, tk.END)
            self.meaning_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập đủ từ và nghĩa.")
