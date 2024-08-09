from tkinter import Tk, Button, Label


class GUI:
    def __init__(self, title: str):
        self.window = Tk()
        self.window.title(title)
        self.window.config(padx=10, pady=100)

    @staticmethod
    def add_button(text: str, func, row: int = 4, column: int = 1, columnspan: int = 2):
        button = Button(text=text, width=36, command=func)
        button.grid(row=row, column=column, columnspan=columnspan)

    @staticmethod
    def add_label(text: str, row: int = 2, column: int = 0):
        label = Label(text=text)
        label.grid(row=row, column=column)
