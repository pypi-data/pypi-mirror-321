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
import os
import getpass
import time
from tkinter import GROOVE

try:
    import winshell
except ImportError:
    os.system('pip install winshell')
    time.sleep(1)
    import winshell

class obtain:
    global user
    global desktop
    user = getpass.getuser()
    desktop = winshell.desktop()

def Gcw(name = None):
    """
    Retrieve the current wallpaper and save it to desktop.获取当前壁纸并保存到桌面.
    name: 保存到桌面的名字,不填保存后名字为wallpaper.jpg #这个后缀名也得加上,后缀名jpg与png只要是照片的后缀名都行,动图的后缀名不行.
    """
    from tkinter import messagebox
    try:
        import shutil

        source_file_path = r"C:\Users\36376\AppData\Roaming\Microsoft\Windows\Themes\TranscodedWallpaper"
        destination_directory = desktop

        try:
            shutil.copy2(source_file_path, destination_directory)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            
        print('Successfully obtained file.')
        print('已成功获取文件.')

        """进行重命名"""
        from pathlib import Path

        desktop_path = str(Path.home() / "Desktop")
        print(f"Desktop path is {desktop_path}")

        old_file_name = 'TranscodedWallpaper'

        if name == None:
            new_file_name = 'wallpaper.jpg'#jpg与png图片都行.

        else:
            new_file_name = name

        try:
            old_full_path = os.path.join(desktop_path, old_file_name)
            new_full_path = os.path.join(desktop_path, new_file_name)

            # Check if the file exists before attempting to rename it.
            if not os.path.exists(old_full_path):
                raise FileNotFoundError(f"The specified file does not exist at location: '{old_full_path}'")

            os.rename(old_full_path, new_full_path)
            print("File renamed successfully.")
        except Exception as e:
            print(f"An error occurred while trying to rename the file: {e}")
    except Exception as e:
        messagebox.showerror('Error','Error:',e)

def CdesktopW(Wallpaper_path):
    """
    更换桌面壁纸
    注意:Wallpaper是壁纸的绝对路径
    """
    import win32api, win32gui, win32api, win32con

    pic=Wallpaper_path

    print(pic)
    regKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(regKey,"WallpaperStyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(regKey, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # refresh screen
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,pic, 1+2)

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
    label = tk.Label(root,text='按下按钮保存当前壁纸.',font=('黑体',15),pady=15)
    label.pack()
    button = tk.Button(text='按钮',width=10,command=_wallpaper,bg='yellow', relief=GROOVE)
    button.pack(pady=23)
    root.mainloop()