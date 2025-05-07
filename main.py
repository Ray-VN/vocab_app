import tkinter as tk
from ui.add_word_frame import AddWordFrame
from ui.review_frame import ReviewFrame


class VocabApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vocab App")
        self.geometry("400x300")

        self.current_frame = None
        self.create_menu()
        self.show_add_word_frame()  # Mặc định hiện frame thêm từ

    def create_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        screen_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Chức năng", menu=screen_menu)
        screen_menu.add_command(label="Thêm từ", command=self.show_add_word_frame)
        screen_menu.add_command(label="Ôn tập từ", command=self.show_review_frame)

    def clear_current_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

    def show_add_word_frame(self):
        self.clear_current_frame()
        self.current_frame = AddWordFrame(self)
        self.current_frame.pack(fill="both", expand=True)

    def show_review_frame(self):
        self.clear_current_frame()
        self.current_frame = ReviewFrame(self)
        self.current_frame.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = VocabApp()
    app.mainloop()
