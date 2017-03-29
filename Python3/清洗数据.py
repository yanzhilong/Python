# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string


# 这个方法清理数据,批回以" "分割的单词列表，并过滤标点符号....
def clean_input(input):
    input = re.sub("\n+", "", input)  # 将多年的\n换成" "空格
    input = re.sub(' +', " ", input)  # 将多个连续的空格过滤成一个空格
    input = bytes(input, "UTF-8")  # 过滤Unicode
    input = input.decode("ascii", "ignore")
    input = input.split(' ')
    cleaninput = []
    for item in input:
        item = item.strip(string.punctuation)  # 通过string.punctuation获取所有的标点符号，这里再通过strip过滤过滤，这里的过滤只是过滤两边的，会保留i'm中的'
        if len(item) > 1 or item.lower() == 'a' or item.lower() == 'i': # 过滤单词字母数为1的,(排除a 和 i)
            cleaninput.append(item)
    return cleaninput


# 这个方法将一个句子(单词用用空格分开)从头开始，每次获取n个单词并存成列表，最后存储到列表中返回
def ngrams(input, n):
    input = clean_input(input)
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output


def function():
    html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
    bsobj = BeautifulSoup(html.read(),"html.parser")
    content = bsobj.find("div",{"id":"mw-content-text"}).get_text()
    ngramsreault = ngrams(content,2)
    print(ngramsreault)
    print("2-grams count is:" + str(len(ngramsreault)))


def function_run():
    print("--------------------")
    function()
    print("--------------------")


if __name__ == "__main__":
    function_run()
