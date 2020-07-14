#!/user/bin/env python
#_*_coding:utf-8_*_

__author__ = 'Damon'

import os


class PdfFile():
    def __init__(self, filepath):
        self.fp = filepath

    def get_num(self):
        return self.n

    def get_vision(self):
        return self.v

class LastestPdf():
    def __init__(self, dir):
        self.d = dir

    def lastest_pdf(self):
        pass
