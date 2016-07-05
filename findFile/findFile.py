#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
此脚本查找目标目录下文件名包含指定关键词的文件，并打印出路径－WUWEI
执行findFile.py->输出findResult.txt
'''

import os

def findFile(path,key):
    result = []
    resultFiles = [os.path.join(path,x) for x in os.listdir(path) if os.path.isfile(os.path.join(path,x)) and key in x]
    dictPaths = [os.path.join(path,x) for x in os.listdir(path) if os.path.isdir(os.path.join(path,x))]

    if dictPaths == []:
        return resultFiles
    else:
        for i in dictPaths:
            try:
                result = result+findFile(i,key)
            except Exception as e:
                print('Error: ',e) # 如果遇到系统文件，权限不足的情况下，会提示permission denied，不影响结果
        return resultFiles+result

def saveResult(path,keys,files):
    with open('./findResult.txt','w',encoding='utf-8') as f:
        f.write(u'路径:' + path + '\t' + '关键词:')
        for key in keys:
            f.write(key+' ')
        f.write(u'\n')
        f.write(u'==================   发现 %d 个结果  ==================\n' % len(files))
        for i in files:
            f.write(u'%s\n'%i)

def main():
    path = input(u"请输入根路径:")
    keys = input(u"请输入关键词:").split(',')  # 支持同时查询多个关键词
    files = []
    for key in keys:
        files = files + findFile(path,key)
    saveResult(path,keys,files)


if __name__ == '__main__':
    main()
    os.system('pause')
