import tkinter as tk
from tkinter import *

from frame.score.socretable import ScoreTable


class LaneFrame(tk.Frame):
    def __init__(self, base=None):
        super().__init__(master=base)
        self.lane_3_score = None
        self.lane_2_score = None
        self.lane_1_score = None
        self.lane_1 = None
        self.main = tk.Frame(base)
        self.main.grid()

    def setting(self, lane1, lane2=None, lane3=None):
        self.lane_1_score = ScoreTable(self, name=lane1)
        self.lane_1_score.grid(row=0, column=0)
        if lane2:
            self.lane_2_score = ScoreTable(self, name=lane2)
            self.lane_2_score.grid(row=1, column=0)
        if lane3:
            self.lane_3_score = ScoreTable(self, name=lane3)
            self.lane_3_score.grid(row=2, column=0)
