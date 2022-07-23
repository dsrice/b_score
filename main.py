import tkinter as tk
from frame.setting.member import MemberFrame

# メインウィンドウを作成
baseGround = tk.Tk()

# ウィンドウのサイズを設定
baseGround.geometry('800x500')

# ウィンドウのタイトルを設定
baseGround.title('設定画面')
frame = MemberFrame(base=baseGround)

frame.pack()
baseGround.mainloop()