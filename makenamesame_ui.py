#!/user/bin/env python
#_*_coding:utf-8_*_

__author__ = 'Damon'


import os
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import simpledialog as sd


class MnsUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.master.title("中元北京数审图纸命名工具")
        self.master.update()
        self.x_ = self.master.winfo_screenwidth() / 2 - self.master.winfo_width() / 2
        self.y_ = self.master.winfo_screenheight() / 2 - self.master.winfo_height() / 2
        self.master.geometry("+%d+%d" % (self.x_, self.y_))

    def create_widgets(self):
        l1 = tk.Label(self, text="文件夹路径:", font=("微软雅黑", 12))
        l1.grid(row=1, column=0, padx=20)

        self.dirpath = tk.StringVar()
        dirpath_entry = tk.Entry(self, textvariable=self.dirpath, font=("微软雅黑", 12))
        dirpath_entry.grid(row=1, column=1, ipadx=150)

        getdir_button = tk.Button(self, text="选择文件夹", command=self.get_dirpath, font=("微软雅黑", 12))
        getdir_button.grid(row=1, column=2, padx=20)

        makenamesame_button = tk.Button(self, text="重命名文件", command=self.make_allname_same, font=("微软雅黑", 12))
        makenamesame_button.grid(row=2, column=1, pady=20)

        explanation = tk.Label(self)
        explanation["text"] ='''
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
        explanation["justify"] = tk.LEFT
        explanation.grid(row=0, column=1)

    def get_dirpath(self):
        self.path_ = fd.askdirectory()
        self.dirpath.set(self.path_)

    def make_allname_same(self):
        dir = self.dirpath.get()
        result = Makenamesame().make_onedir_same(self.dirpath.get())
        if result:
            # self.pop_ok("重命名成功!", "green")  #使用自建弹窗
            mb.showinfo(title="Info", message="重命名成功！")
        else:
            # self.pop_ok("文件夹路径错误!", "red")  #使用自建弹窗
            mb.showerror(title="Info", message="文件夹路径错误！")

    def cancel(self):
        self.master.destroy()

    # # 使用自建弹窗
    # def pop_ok(self, info="OK", fg="black"):
    #     root_ = tk.Toplevel()
    #     ok_window = OkDialog(master=root_, info=info, fg=fg)
    #     # ok_window = OkDialog(master=self.master, info=info, fg=fg) #将ok框架放到通一个主窗口上
    #     self.wait_window(ok_window)


# #发现messagebox，就不用自己新建类了，自己建的类无法禁用底层窗口
# class OkDialog(tk.Frame):
#     def __init__(self, master=None, info="OK", **kw):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.info = info
#         self.kw = kw
#         self.master.title("")
#         self.create_widgets()
#         self.master.update()
#         self.x_ = self.master.winfo_screenwidth() / 2 - self.master.winfo_width() / 2
#         self.y_ = self.master.winfo_screenheight() / 2 - self.master.winfo_height() / 2
#         self.master.geometry("+%d+%d" % (self.x_, self.y_))
#
#
#     def create_widgets(self):
#         l_ok = tk.Label(self, text=self.info, **self.kw)
#         l_ok.pack(padx=60, pady=20)
#
#         b_ok = tk.Button(self, text="确定", command=self.cancel, font=("微软雅黑", 12))
#         b_ok.pack(padx=60,pady=10)
#
#     def cancel(self):
#         self.master.destroy()


class Makenamesame():
    def make_onedir_same(self, dir):
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
        pdflist = []
        dwflist = []
        for file in os.listdir(dir):
            if os.path.splitext(file)[1] == ".pdf":
                pdflist.append(file)
            elif os.path.splitext(file)[1] == ".dwf":
                dwflist.append(file)
            else:
                pass
        for pdf in pdflist:
            for dwf in dwflist:
                if dwf.split("_")[0] == pdf.split("_")[0]:
                    sametuzhilist.append([os.path.join(dir, dwf), os.path.join(dir, pdf)])
        return sametuzhilist


root = tk.Tk()
app = MnsUI(master=root)
app.mainloop()
