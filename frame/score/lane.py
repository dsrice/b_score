import tkinter as tk
from tkinter import *


class LaneFrame(tk.Frame):
    def __init__(self, base=None):
        super().__init__(master=base)
        self.main = tk.Frame(base)
        self.main.grid()

    def setting(self, lane1, lane2=None, lane3=None):
        self.lane_1 = tk.Label(self.main, text=lane1)
        self.lane_1.grid(row=0, column=0)
        if lane2:
            self.lane_2 = tk.Label(self.main, text=lane2)
            self.lane_2.grid(row=1, column=0)
        if lane3:
            self.lane_3 = tk.Label(self.main, text=lane3)
            self.lane_3.grid(row=2, column=0)
