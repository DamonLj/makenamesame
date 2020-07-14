#!/user/bin/env python
#_*_coding:utf-8_*_

__author__ = 'Damon'

import os
import pandas as pd


class PdfFile():
    def __init__(self, filename_ex):
        self.fn_ex = filename_ex
        self.fn, self.ex = os.path.splitext(self.fn_ex)
        self.n = self.get_num()
        self.v = self.get_vision()

    def get_num(self):
        n = self.fn.split("_")[0]
        return n

    def get_vision(self):
        if self.fn[-1] == "D":
            v = 0
        elif self.fn[-1] == ")":
            v = self.fn[-2]
        else: pass
        return v

class LastestPdf():
    def __init__(self, dir):
        self.d = dir
        self.list = []

    def lastest_pdf(self):
        for f in os.listdir(self.d):
            f_c = PdfFile(f)
            self.list.append((f, f_c.n, int(f_c.v)))
        df = pd.DataFrame(self.list, columns=["filename", "number", "virsion"])
        # g1 = df.groupby("number").apply(lambda t:t[t.virsion==t.virsion.max()])
        idx = df.groupby("number")["virsion"].idxmax()
        print(idx)
        return

dir = "D:\Downloads\pdf"
LastestPdf(dir).lastest_pdf()