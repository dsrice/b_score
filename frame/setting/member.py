import tkinter as tk
from tkinter import *

from frame.score.lane import LaneFrame


class MemberFrame(tk.Frame):
    """
    投球者管理フレーム
    """

    def __init__(self, base=None):
        super().__init__(master=base)
        self.frametitle = tk.LabelFrame(self.master, text="投球者情報", padx=10, pady=10)
        self.frametitle.grid()

        self.l_frametitle = tk.LabelFrame(self.frametitle, text="左レーン情報", padx=10, pady=10)
        self.l_frametitle.grid()

        self.l1_label = tk.Label(self.l_frametitle, text="第1投球者", padx=10, pady=10)
        self.l1_name = StringVar()
        self.l1_name_entry = tk.Entry(
            self.l_frametitle,
            textvariable=self.l1_name,
            width=20
        )

        self.l2_label = tk.Label(self.l_frametitle, text="第2投球者", padx=10, pady=10)
        self.l2_name = StringVar()
        self.l2_name_entry = tk.Entry(
            self.l_frametitle,
            textvariable=self.l2_name,
            width=20
        )

        self.l3_label = tk.Label(self.l_frametitle, text="第3投球者", padx=10, pady=10)
        self.l3_name = StringVar()
        self.l3_name_entry = tk.Entry(
            self.l_frametitle,
            textvariable=self.l3_name,
            width=20
        )


        self.r_frametitle = tk.LabelFrame(self.frametitle, text="右レーン情報", padx=10, pady=10)
        self.r_frametitle.grid()

        self.r1_label = tk.Label(self.r_frametitle, text="第1投球者", padx=10, pady=10)
        self.r1_name = StringVar()
        self.r1_name_entry = tk.Entry(
            self.r_frametitle,
            textvariable=self.r1_name,
            width=20
        )

        self.r2_label = tk.Label(self.r_frametitle, text="第2投球者", padx=10, pady=10)
        self.r2_name = StringVar()
        self.r2_name_entry = tk.Entry(
            self.r_frametitle,
            textvariable=self.r2_name,
            width=20
        )

        self.r3_label = tk.Label(self.r_frametitle, text="第3投球者", padx=10, pady=10)
        self.r3_name = StringVar()
        self.r3_name_entry = tk.Entry(
            self.r_frametitle,
            textvariable=self.r3_name,
            width=20
        )

        self.actionarea = tk.LabelFrame(self.frametitle, text="操作内容", padx=10, pady=10)
        self.actionarea.grid()

        self.set_button = tk.Button(self.actionarea, text="スコア表作成", padx=10, pady=10)
        self.set_button["command"] = self.create_score


        self.l1_label.grid(row=0, column=0)
        self.l1_name_entry.grid(row=0, column=1)
        self.l2_label.grid(row=1, column=0)
        self.l2_name_entry.grid(row=1, column=1)
        self.l3_label.grid(row=2, column=0)
        self.l3_name_entry.grid(row=2, column=1)

        self.r1_label.grid(row=0, column=0)
        self.r1_name_entry.grid(row=0, column=1)
        self.r2_label.grid(row=1, column=0)
        self.r2_name_entry.grid(row=1, column=1)
        self.r3_label.grid(row=2, column=0)
        self.r3_name_entry.grid(row=2, column=1)

        self.set_button.grid(row=0, column=0)
        self.l_frametitle.grid(row=0, column=0, padx=10, pady=10)
        self.r_frametitle.grid(row=0, column=1, padx=10, pady=10)
        self.actionarea.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.frametitle.pack()

    def create_score(self):
        self.score_modal = tk.Toplevel(self)
        self.score_modal.title("スコア表")
        self.score_modal.geometry("1300x200")
        socore_modal_frame = tk.Frame(self.score_modal)
        socore_modal_frame.grid()

        l_score_frame = LaneFrame(socore_modal_frame)
        l_score_frame.setting(self.l1_name.get(), self.l2_name.get(), self.l3_name.get())

        r_score_frame = LaneFrame(socore_modal_frame)
        r_score_frame.setting(self.r1_name.get(), self.r2_name.get(), self.r3_name.get())
        l_score_frame.grid(row=0, column=0)
        r_score_frame.grid(row=0, column=1)

        self.set_modal = tk.Toplevel(self)
        self.set_modal.title("スコア設定(左）")
        self.set_modal.geometry("300x200")

        self.set_modal = tk.Toplevel(self)
        self.set_modal.title("スコア設定(右）")
        self.set_modal.geometry("300x200")
