#!/user/bin/env python
#_*_coding:utf-8_*_

__author__ = 'Damon'


import os


def make_name_same(filepath0, filepath1):
    '''
    将file1重命名为和file0相同名字
    需要不同文件后缀
    '''
    if os.path.splitext(filepath0)[1] == os.path.splitext(filepath1)[1]:
        print("文件扩展名相同，不能重命名")
    else:
        filepath2 = os.path.splitext(filepath0)[0] + os.path.splitext(filepath1)[1]
        os.rename(filepath1, filepath2)
    return filepath2
    
def find_same_tuzhi(dir):
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



if __name__ == '__main__':
    print(
        '''
************************************说  明***********************************************
        本程序用于中元报审北京数字审图项目，批量将PDF文件名更改为与PDF图号相同的dwf的文件名。
        1、dwf和pdf放在同一文件夹下。
        2、dwf文件名为正确的：图号_图名。PDF文件名是：图号_签章。
        3、PDF应与dwf一一对应，不能由多余PDF文件。
        例：
                    更改前                                  更改后
        U001G1-A0020-1201_签章.pdf              U001G1-A0020-1201_一层平面图.pdf
        U001G1-A0020-1201_一层平面图.dwf         U001G1-A0020-1201_一层平面图.dwf
        U001G1-A0020-1202_签章(1).pdf           U001G1-A0020-1202_二层平面图.pdf
        U001G1-A0020-1202_二层平面图.dwf         U001G1-A0020-1202_二层平面图.dwf
*********************by damon************************ljmgps******************************
        '''
    )
    dir = input('输入文件夹路径:')
    if os.path.exists(dir):
        sametuzhilist = find_same_tuzhi(dir)
        for t in sametuzhilist:
            make_name_same(*t)
    else:
        print("文件夹路径错误")
        input()
