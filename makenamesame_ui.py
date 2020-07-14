#!/user/bin/env python
#_*_coding:utf-8_*_

__author__ = 'Damon'


import os
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb


class MnsUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)  #初始化此框架的主窗口类
        self.master = master
        self.pack()  #放置框架在窗口上
        self.create_widgets()
        self.master.title("中元北京数审图纸命名工具")
        self.master.update()  #更新获取窗口大小，用于窗口居中
        # 获取屏幕分辨率，算出窗口左上角坐标定位
        self.x_ = self.master.winfo_screenwidth() / 2 - self.master.winfo_width() / 2
        self.y_ = self.master.winfo_screenheight() / 2 - self.master.winfo_height() / 2
        self.master.geometry("+%d+%d" % (self.x_, self.y_))

    def create_widgets(self):
        l_1 = tk.Label(self, text="文件夹路径:", font=("微软雅黑", 12))
        l_1.grid(row=1, column=0, padx=20)

        self.dirpath = tk.StringVar()
        e_dirpath = tk.Entry(self, textvariable=self.dirpath, font=("微软雅黑", 12))
        e_dirpath.grid(row=1, column=1, ipadx=150)

        b_getdir = tk.Button(self, text="选择文件夹", command=self.get_dirpath, font=("微软雅黑", 12))
        b_getdir.grid(row=1, column=2, padx=20)

        b_makenamesame = tk.Button(self, text="重命名文件", command=self.make_allname_same, font=("微软雅黑", 12))
        b_makenamesame.grid(row=2, column=1, pady=20)

        l_explanation = tk.Label(self)
        l_explanation["text"] ='''
*********************************************说  明************************************************************
        本程序用于中元报审北京数字审图项目，批量将PDF文件名更改为与PDF图号相同的dwf的文件名。
        1、dwf和pdf放在同一文件夹下。
        2、dwf文件名为正确的：图号_图名。PDF文件名是：图号_签章。
        3、PDF应与dwf一一对应，不能由多余PDF文件。
        例：
                    更改前                                                           更改后
        U001G1-A0020-1201_签章.pdf                 U001G1-A0020-1201_一层平面图.pdf
        U001G1-A0020-1201_一层平面图.dwf        U001G1-A0020-1201_一层平面图.dwf
        U001G1-A0020-1202_签章(1).pdf              U001G1-A0020-1202_二层平面图.pdf
        U001G1-A0020-1202_二层平面图.dwf        U001G1-A0020-1202_二层平面图.dwf
********************************by damon************************ljmgps**********************************
        '''
        l_explanation["justify"] = tk.LEFT  #设置文字左对齐
        l_explanation.grid(row=0, column=1)

    def get_dirpath(self):
        self.path_ = fd.askdirectory()
        self.dirpath.set(self.path_)

    def make_allname_same(self):
        dir = self.dirpath.get()
        result = Makenamesame().make_alldir_same(self.dirpath.get())
        if result:
            mb.showinfo(title="Info", message="重命名成功！")  #使用message类弹出新窗口
        else:
            mb.showerror(title="Info", message="文件夹路径错误！")

    def cancel(self):
        self.master.destroy()  #关闭窗口，不是框架，所以是master


class Makenamesame():
    def make_alldir_same(self, dir):
        if os.path.exists(dir):
            sametuzhilist = self.find_same_tuzhi(dir)
            for t in sametuzhilist:
                self.make_name_same(*t)
            return 1
        else:
            return 0

    def make_name_same(self, filepath0, filepath1):
        '''
        将file1重命名为和file0相同名字
        需要不同文件后缀
        '''
        if os.path.splitext(filepath0)[1] == os.path.splitext(filepath1)[1]:
            print("文件扩展名相同，不能重命名!")
        else:
            filepath2 = os.path.splitext(filepath0)[0] + os.path.splitext(filepath1)[1]
            os.rename(filepath1, filepath2)
        return filepath2

    def find_same_tuzhi(self, dir):
        '''
        找到相同图纸，返回文件夹内所有相同图纸的列表
        '''
        sametuzhilist = []
        for root, dirs, filenames in os.walk(dir):
            pdflist = []
            dwflist = []
            for file in filenames:
                if os.path.splitext(file)[1] == ".pdf":
                    pdflist.append(file)
                elif os.path.splitext(file)[1] == ".dwf":
                    dwflist.append(file)
                else:
                    pass
            for pdf in pdflist:
                for dwf in dwflist:
                    if dwf.split("_")[0] == pdf.split("_")[0]:
                        sametuzhilist.append([os.path.join(root, dwf), os.path.join(root, pdf)])
                    else: pass
        return sametuzhilist


root = tk.Tk()
app = MnsUI(master=root)
app.mainloop()
