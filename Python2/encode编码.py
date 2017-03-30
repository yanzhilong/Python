# -*- coding: utf-8 -*-
import sys
import csv
import codecs

def default_coding():
    pass


def function():
    print(unicode("好","utf-8"))
    print("系统的默认编码是:")
    print isinstance("你好",unicode)


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
