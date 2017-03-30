# -*- coding: utf-8 -*-
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup


def function():
    print("下载一个文件")
    html = urlopen("http://www.pythonscraping.com")
    bsobj = BeautifulSoup(html.read(),"html.parser")
    imagelocation = bsobj.find("a", {"id": "logo"}).find("img")["src"]
    urlretrieve(imagelocation, "Download\logo.jpg")


def function_run():
    print("--------------------")
    function()
    print("--------------------")


if __name__ == "__main__":
    function_run()
