import tkinter as tk
from tkinter import *


class LastScore:
    def __init__(self, base, row, column):
        self.score_1 = tk.Label(base, text="", background="white", bd=1, relief=tk.SOLID, width=2)
        self.score_2 = tk.Label(base, text="", background="white", bd=1, relief=tk.SOLID, width=2)
        self.score_3 = tk.Label(base, text="", background="white", bd=1, relief=tk.SOLID, width=2)
        self.score = tk.Label(base, text="", background="white", bd=1, relief=tk.SOLID)
        self.base = base
        self.row = row
        self.column = column
        self.score_1.grid(row=self.row, column=self.column)
        self.score_2.grid(row=self.row, column=self.column+1)
        self.score_3.grid(row=self.row, column=self.column+2)
        self.score.grid(row=self.row+1, column=self.column, columnspan=3, sticky=tk.W+tk.E)
        self.strike = PhotoImage(file="image/strike.png")

    def review(self, num, strike_flg=False, spare_flg=False):
        if strike_flg:
            self.score = tk.Label(self.base, text="", background="white", bd=1, relief=tk.SOLID, image=self.strike)

        self.score.grid(row=self.row, column=self.column)
