#!/user/bin/env python
#_*_coding:utf-8_*_

__author__ = 'Damon'

import os
import numpy as np
import pandas as pd


class PdfFile():
    def __init__(self, filename_ex):
        self.fn_ex = filename_ex
        self.fn, self.ex = os.path.splitext(self.fn_ex)
        self.n = self.get_num()
        self.v = self.get_vision()

    def get_num(self):
        n = self.fn.split("_")[0].replace(" ", "")
        return n

    def get_vision(self):
        if self.fn[-1] == "D" or self.fn[-1] == "E":
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
        if os.path.exists(self.d):
            for f in os.listdir(self.d):
                f_c = PdfFile(f)
                self.list.append((f, f_c.n, int(f_c.v)))
            df = pd.DataFrame(self.list, columns=["filename", "number", "virsion"])
            lastest_id = list(df.groupby("number")["virsion"].idxmax())
            old_id = list(set(df.index) - set(lastest_id))
            for i in old_id:
                # print(df.at[i, "filename"])
                os.remove(os.path.join(self.d, df.at[i, "filename"]))
            for i in lastest_id:
                os.rename(os.path.join(self.d, df.at[i, "filename"]),
                          os.path.join(self.d, df.at[i, "number"] + "_" + ".pdf"))
            return 1
        else: return 0
