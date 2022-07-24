import tkinter as tk
from tkinter import *


class Score:
    def __init__(self, base, row, column):
        self.score_1 = tk.Label(base, text="", background="white", bd=1, relief=tk.SOLID, width=2)
        self.score_2 = tk.Label(base, text="", background="white", bd=1, relief=tk.SOLID, width=2)
        self.score = tk.Label(base, text="", background="white", bd=1, relief=tk.SOLID)
        self.base = base
        self.row = row
        self.column = column
        self.score_1.grid(row=self.row, column=self.column)
        self.score_2.grid(row=self.row, column=self.column+1)
        self.score.grid(row=self.row+1, column=self.column, columnspan=2, sticky=tk.EW)
        self.strike = PhotoImage(file="image/strike.png")
        self.spare = PhotoImage(file="image/spare.png")

        self.display_count = 0
        self.display_flg = False
        self.count_1 = 0
        self.count_2 = 0
        self.strike_flg = False
        self.spare_flg = False
        self.gater1_flg = False
        self.gater2_flg = False

    def review(self, num_1, num_2=None, strike_flg=False, spare_flg=False):
        if strike_flg:
            self.score_1 = tk.Label(self.base, text="", background="white", bd=1, relief=tk.SOLID, image=self.strike)
            self.strike_flg = True
            self.count_1 = 10

        elif spare_flg:
            self.score_2 = tk.Label(self.base, text="", background="white", bd=1, relief=tk.SOLID, image=self.spare)
            self.spare_flg = True
            self.count_2 = 10 - self.count_1

        elif num_1 == 0:
            self.score_1 = tk.Label(self.base, text="G", background="white", bd=1, relief=tk.SOLID, width=2)
            self.gater1_flg = True
        else:
            if num_2:
                if num_2 == 0:
                    self.score_2 = tk.Label(self.base, text="-", background="white", bd=1, relief=tk.SOLID, width=2)
                    self.gater2_flg = True
                else:
                    self.score_2 = tk.Label(self.base, text=num_2, background="white", bd=1, relief=tk.SOLID, width=2)
                    self.count_2 = num_2

            self.score_1 = tk.Label(self.base, text=num_1, background="white", bd=1, relief=tk.SOLID, width=2)
            self.count_1 = num_1

        self.score_1.grid(row=self.row, column=self.column)
        self.score_2.grid(row=self.row, column=self.column+1)

        self.base.calc()

    def set_display(self, num):
        self.display_count = num
        self.display_flg = True
        self.score = tk.Label(self.base, text=num, background="white", bd=1, relief=tk.SOLID)
        self.score.grid(row=self.row+1, column=self.column, columnspan=2, sticky=tk.EW)

