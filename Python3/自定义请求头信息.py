# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def function():
    print("自定义请求头信息，并通过网查查看客户端提交的信息")
    session = requests.session()
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)\
AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
"Accept":"text/html,application/xhtml+xml,application/xml;\
q=0.9,image/webp,*/*;q=0.8"}
    url = "https://www.whatismybrowser.com/\
developers/what-http-headers-is-my-browser-sending"
    req = session.get(url, headers = headers)
    print(req.text)
    bsobj = BeautifulSoup(req.text, "html.parser")
    print(bsobj.find("table", {"class": "table-hover"}).get_text())


def function_run():
    print("--------------------")
    function()
    print("--------------------")


if __name__ == "__main__":
    function_run()
