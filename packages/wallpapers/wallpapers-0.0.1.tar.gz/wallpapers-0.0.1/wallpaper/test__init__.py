# -*- coding: utf-8 -*-
#函数名最前面带下划线的都是辅助函数.
main = True
if main == True:
    print('函数名最前面带下划线的都是辅助函数.')

if main == False:
    pass

"""
Operation of Wallpaper
author: huang yi yi(hyy_sn)
"""
from tkinter import GROOVE
try:
    from __init__ import *

except ImportError:
    from tkinter import messagebox
    messagebox.showerror('No','程序缺少main文件!')
    def _main():
        return ImportError
    _main()

if __name__ == '__main__':
    """WALLPAPER"""
    def _wallpaper():
        from tkinter import messagebox
        Gcw('wallpaper.png')
        Gcw('wallpaper.jpg')
        Gcw('wallpaper.ico')
        messagebox.showinfo('wallpaper','           保存成功!           ')

    import tkinter as tk
    root = tk.Tk()
    root.title('wallpaper')
    root.geometry('300x150+700+300')
    label = tk.Label(root,text='按下按钮保存当前电脑壁纸.',font=('黑体',15),pady=20)
    label.pack()
    button = tk.Button(text='按钮',width=10,command=_wallpaper,bg='yellow', relief=GROOVE)
    button.pack(pady=20)
    root.mainloop()