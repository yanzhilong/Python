# -*- coding: utf-8 -*-
import sys
import csv
import codecs

def default_coding():
    pass

# http://blog.csdn.net/freesigefei/article/details/50623413
# http://blog.csdn.net/mindmb/article/details/7898528

def function():
    print ("由于Python的源码中有设置了coding:utf-8，所以源码编译的时候会编译成utf-8的byts string")
    print ("Python2中代码里面的中文默认会通过asscii码编码")
    hello = "你好" # 这个中文字在编译的时候默认是asscii编译的，所以会打印乱码,这是python2默认的

    print(unicode("好","utf-8"))
    print("系统的默认编码是:")
    print isinstance("你好", unicode)



def writecsv():
    print("写入中文到csv中")
    csv_file = open("Download\\test.csv", 'w')
    try:
        csv_file.write(codecs.BOM_UTF8)
        writer = csv.writer(csv_file)
        writer.writerow(('姓名', '年龄'))
        for i in range(10):
            writer.writerow((i, i + 2, i * 2))
    finally:
        csv_file.close()


def function_run():
    print("--------------------")
    function()
    print("--------------------")
    writecsv()
    print("--------------------")

if __name__ == "__main__":
    function_run()
