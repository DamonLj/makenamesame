#!/user/bin/env python
#_*_coding:utf-8_*_

__author__ = 'Damon'


import os


class Makenamesame():
    def __init__(self, dir):
        self.d = dir

    def make_alldir_same(self):
        if os.path.exists(self.d):
            sametuzhilist = self.find_same_tuzhi()
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
            pass
        else:
            filepath2 = os.path.splitext(filepath0)[0] + os.path.splitext(filepath1)[1]
            os.rename(filepath1, filepath2)
        return filepath2

    def find_same_tuzhi(self):
        '''
        找到相同图纸，返回文件夹内所有相同图纸的列表
        '''
        sametuzhilist = []
        for root, dirs, filenames in os.walk(self.d):
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
