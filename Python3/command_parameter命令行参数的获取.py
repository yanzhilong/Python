# -*- coding: utf-8 -*-
import sys

def function():
    print("测试命令行参数")
    args = sys.argv
    if len(args) == 1:
        print("运行的文件名是：%s" % args[0])
    elif len(args) > 1:
        for index in range(len(args)):
            if index != 0:
                print("第%s个参数是" + args[index])

def function_run():
    print("--------------------")
    function()
    print("--------------------")


if __name__ == "__main__":
    function_run()
