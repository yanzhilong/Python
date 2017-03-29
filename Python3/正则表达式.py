# -*- coding: utf-8 -*-
import re


# 去除两边空格
def cuteblank():
    source = "      aslkfjoasdf    "
    print(source)
    p1 = "[^\\s+].*[^\\s]+"  # 这是我们写的正则表达式规则，你现在可以不理解啥意思
    pattern1 = re.compile(p1)  # 我们在编译这段正则表达式
    matcher1 = re.search(pattern1, source)  # 在源文本中搜索符合正则表达式的部分
    result = matcher1.group(0)  # 打印出来
    print(result)


def function_run():
    print("--------------------")
    cuteblank()
    print("--------------------")


if __name__ == "__main__":
    function_run()
