import tkinter as tk
from tkinter import *


class ScoreTable(tk.Frame):
    def __init__(self, base=None, name=None):
        super().__init__(master=base, background="white", padx=5, pady=5)
        self.grid()

        self.name_label = tk.Label(self, text="投球者名", background="white", bd=1, relief=tk.SOLID, width=7)
        self.name = tk.Label(self, text=name, background="white", bd=1, relief=tk.SOLID, width=7)

        self.label_1 = tk.Label(self, text="1", background="white", bd=1, relief=tk.SOLID, width=6)
        self.score1_1 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)
        self.score1_2 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)

        self.label_2 = tk.Label(self, text="2", background="white", bd=1, relief=tk.SOLID)
        self.score2_1 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)
        self.score2_2 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)

        self.label_3 = tk.Label(self, text="3", background="white", bd=1, relief=tk.SOLID)
        self.score3_1 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)
        self.score3_2 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)

        self.label_4 = tk.Label(self, text="4", background="white", bd=1, relief=tk.SOLID)
        self.score4_1 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)
        self.score4_2 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)

        self.label_5 = tk.Label(self, text="5", background="white", bd=1, relief=tk.SOLID)
        self.score5_1 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)
        self.score5_2 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)

        self.label_6 = tk.Label(self, text="6", background="white", bd=1, relief=tk.SOLID)
        self.score6_1 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)
        self.score6_2 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)

        self.label_7 = tk.Label(self, text="7", background="white", bd=1, relief=tk.SOLID)
        self.score7_1 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)
        self.score7_2 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)

        self.label_8 = tk.Label(self, text="8", background="white", bd=1, relief=tk.SOLID)
        self.score8_1 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)
        self.score8_2 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)

        self.label_9 = tk.Label(self, text="9", background="white", bd=1, relief=tk.SOLID)
        self.score9_1 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)
        self.score9_2 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)

        self.label_10 = tk.Label(self, text="10", background="white", bd=1, relief=tk.SOLID)
        self.score10_1 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)
        self.score10_2 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)
        self.score10_3 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)

        self.label_total = tk.Label(self, text="total", background="white", bd=1, relief=tk.SOLID, width=6)
        self.total_score = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=6)

        self.name_label.grid(row=0, column=0)
        self.name.grid(row=1, column=0)

        self.label_1.grid(row=0, column=1, columnspan=2, sticky=tk.W + tk.E)
        self.score1_1.grid(row=1, column=1)
        self.score1_2.grid(row=1, column=2)

        self.label_2.grid(row=0, column=3, columnspan=2, sticky=tk.W + tk.E)
        self.score2_1.grid(row=1, column=3)
        self.score2_2.grid(row=1, column=4)

        self.label_3.grid(row=0, column=5, columnspan=2, sticky=tk.W + tk.E)
        self.score3_1.grid(row=1, column=5)
        self.score3_2.grid(row=1, column=6)

        self.label_4.grid(row=0, column=7, columnspan=2, sticky=tk.W + tk.E)
        self.score4_1.grid(row=1, column=7)
        self.score4_2.grid(row=1, column=8)

        self.label_5.grid(row=0, column=9, columnspan=2, sticky=tk.W + tk.E)
        self.score5_1.grid(row=1, column=9)
        self.score5_2.grid(row=1, column=10)

        self.label_6.grid(row=0, column=11, columnspan=2, sticky=tk.W + tk.E)
        self.score6_1.grid(row=1, column=11)
        self.score6_2.grid(row=1, column=12)

        self.label_7.grid(row=0, column=13, columnspan=2, sticky=tk.W + tk.E)
        self.score7_1.grid(row=1, column=13)
        self.score7_2.grid(row=1, column=14)

        self.label_8.grid(row=0, column=15, columnspan=2, sticky=tk.W + tk.E)
        self.score8_1.grid(row=1, column=15)
        self.score8_2.grid(row=1, column=16)

        self.label_9.grid(row=0, column=17, columnspan=2, sticky=tk.W + tk.E)
        self.score9_1.grid(row=1, column=17)
        self.score9_2.grid(row=1, column=18)

        self.label_10.grid(row=0, column=19, columnspan=3, sticky=tk.W + tk.E)
        self.score10_1.grid(row=1, column=19)
        self.score10_2.grid(row=1, column=20)
        self.score10_3.grid(row=1, column=21)

        self.label_total.grid(row=0, column=22)
        self.total_score.grid(row=1, column=22)
