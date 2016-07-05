#!/usr/bin/python
#-*- coding: UTF-8 -*-

"""
此脚本用于计算BI原始日志的行数-WUWEI
执行countLine_log.py->输出logline.txt
"""

import os
fileext = ('log') # 需要计算行数的文件扩展名
rootdir = '.'     # 路径
line_count = 0    

def countline(f):
    global line_count
    if f.endswith(fileext):
        print(u'正在计算当前文件行数 : %s'%f)
        fo = open(f, 'rb')
        lines = len(fo.read().split(b'\n')) #分隔符设定
        fo.close()
        line_count += lines

def walks(path):
    global line_count
    dname = ''
    lognum= 0
    for root, dirs, files in os.walk(path):
        for f in files:
            f = os.path.join(root, f)
            countline(f)
            lognum += 1 # 每个log文件减去一行\n
            dname = os.path.split(os.path.dirname(f))
            dirname = dname[1]
        print(u'日志%s的行数为 : %s\n\n' %(dirname,line_count-lognum))# 一个目录内的所有子文件的总行数

        f = open('./logline.txt', 'a')
        f.write('日志%s的行数为 : %s\n\n' %(dirname,line_count-lognum))
        f.close()
        
        line_count = 0
        lognum = 0
if __name__ == '__main__':
    walks('.')
    os.system('pause')
