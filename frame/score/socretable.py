import math
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

from frame.score.last_score import LastScore
from frame.score.score import Score


class ScoreTable(tk.Frame):

    def __init__(self, base=None, name=None):
        super().__init__(master=base, background="white", padx=5, pady=5)
        self.grid()

        self.name_label = tk.Label(self, text="投球者名", background="white", bd=1, relief=tk.SOLID, width=7)
        self.name = tk.Label(self, text=name, background="white", bd=1, relief=tk.SOLID, width=7)

        self.label_1 = tk.Label(self, text="1", background="white", bd=1, relief=tk.SOLID)
        self.score_1 = Score(base=self, row=1, column=1)

        self.label_2 = tk.Label(self, text="2", background="white", bd=1, relief=tk.SOLID)
        self.score_2 = Score(base=self, row=1, column=3)

        self.label_3 = tk.Label(self, text="3", background="white", bd=1, relief=tk.SOLID)
        self.score_3 = Score(base=self, row=1, column=5)

        self.label_4 = tk.Label(self, text="4", background="white", bd=1, relief=tk.SOLID)
        self.score_4 = Score(base=self, row=1, column=7)

        self.label_5 = tk.Label(self, text="5", background="white", bd=1, relief=tk.SOLID)
        self.score_5 = Score(base=self, row=1, column=9)

        self.label_6 = tk.Label(self, text="6", background="white", bd=1, relief=tk.SOLID)
        self.score_6 = Score(base=self, row=1, column=11)

        self.label_7 = tk.Label(self, text="7", background="white", bd=1, relief=tk.SOLID)
        self.score_7 = Score(base=self, row=1, column=13)

        self.label_8 = tk.Label(self, text="8", background="white", bd=1, relief=tk.SOLID)
        self.score_8 = Score(base=self, row=1, column=15)

        self.label_9 = tk.Label(self, text="9", background="white", bd=1, relief=tk.SOLID)
        self.score_9 = Score(base=self, row=1, column=17)


        self.label_10 = tk.Label(self, text="10", background="white", bd=1, relief=tk.SOLID)
        self.score_10 = LastScore(base=self, row=1, column=19)
        self.score10_1 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)
        self.score10_2 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)
        self.score10_3 = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=3)

        self.label_total = tk.Label(self, text="total", background="white", bd=1, relief=tk.SOLID, width=6)
        self.total_score = tk.Label(self, text="", background="white", bd=1, relief=tk.SOLID, width=6)

        self.name_label.grid(row=0, column=0)
        self.name.grid(row=1, column=0, rowspan=2, sticky=tk.NS)

        self.label_1.grid(row=0, column=1, columnspan=2, sticky=tk.EW)
        self.label_2.grid(row=0, column=3, columnspan=2, sticky=tk.EW)
        self.label_3.grid(row=0, column=5, columnspan=2, sticky=tk.EW)
        self.label_4.grid(row=0, column=7, columnspan=2, sticky=tk.EW)
        self.label_5.grid(row=0, column=9, columnspan=2, sticky=tk.EW)
        self.label_6.grid(row=0, column=11, columnspan=2, sticky=tk.EW)
        self.label_7.grid(row=0, column=13, columnspan=2, sticky=tk.EW)
        self.label_8.grid(row=0, column=15, columnspan=2, sticky=tk.EW)
        self.label_9.grid(row=0, column=17, columnspan=2, sticky=tk.EW)

        self.label_10.grid(row=0, column=19, columnspan=3, sticky=tk.EW)

        self.label_total.grid(row=0, column=22)
        self.total_score.grid(row=1, column=22, rowspan=2,  sticky=tk.NS)

    def calc(self):
        #  Frame1
        now_count = set_display(maiin_score=self.score_1, score_2=self.score_2, score_3=self.score_3, before_socre=0)

        #  Frame2
        if now_count:
            now_count = set_display(maiin_score=self.score_2, score_2=self.score_3, score_3=self.score_4,
                                    before_socre=now_count)

        #  Frame3
        if now_count:
            now_count = set_display(maiin_score=self.score_3, score_2=self.score_4, score_3=self.score_5,
                                    before_socre=now_count)

        #  Frame4
        if now_count:
            now_count = set_display(maiin_score=self.score_4, score_2=self.score_5, score_3=self.score_6,
                                    before_socre=now_count)

        #  Frame5
        if now_count:
            now_count = set_display(maiin_score=self.score_5, score_2=self.score_6, score_3=self.score_7,
                                    before_socre=now_count)

        #  Frame6
        if now_count:
            now_count = set_display(maiin_score=self.score_6, score_2=self.score_7, score_3=self.score_8,
                                    before_socre=now_count)

        #  Frame7
        if now_count:
            now_count = set_display(maiin_score=self.score_7, score_2=self.score_8, score_3=self.score_9,
                                    before_socre=now_count)


def set_display(main_score: Score, score_2: Score, score_3: Score, before_socre):
    if main_score.strike_flg:
        if score_2.strike_flg:
            if score_3.strike_flg:
                main_score.set_display(num=before_socre + 30)
            else:
                if score_3.count_1:
                    main_score.set_display(num=before_socre + 20 + score_3.count_1)
        else:
            if score_2.spare_flg:
                main_score.set_display(num=before_socre + 20)
            elif score_2.count_2:
                main_score.set_display(num=before_socre + 10 + score_2.count_1 + score_2.count_2)
    elif main_score.spare_flg:
        if score_2.strike_flg:
            main_score.set_display(num=before_socre + 20)
        else:
            main_score.set_display(num=before_socre + 10 + score_2.count_1)
    else:
        if main_score.count_2:
            main_score.set_display(num=before_socre + main_score.count_1 + main_score.count_2)

    return main_score.display_count





