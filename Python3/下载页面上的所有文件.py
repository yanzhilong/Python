# -*- coding: utf-8 -*-
import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

download_directory = "Download"
baseurl = "http://pythonscraping.com"


def get_absolute_url(baseurl, source):
    if source.startswith("http://www."):
        url = "http://" + source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = source[4:]
        url = "http://" + source
    else:
        url = baseurl + "/" + source
    if baseurl not in url:
        return None
    return url


def get_download_path(baseurl, absoluurl, downloaddirectory):
    path = absoluurl.replace("www.", "")
    path = path.replace(baseurl,"")
    path = download_directory + path
    diretory = os.path.dirname(path)

    if not os.path.exists(diretory):
        os.makedirs(diretory)
    return path


def function():
    print("下载页面上的所有文件")
    html = urlopen("http://www.pythonscraping.com")
    bsobj = BeautifulSoup(html.read(), "html.parser")
    downloadlist = bsobj.findAll(src=True)

    for download in downloadlist:
        fileurl = get_absolute_url(baseurl, download["src"])
        if fileurl is not None:
            print(fileurl)
            try:
                urlretrieve(fileurl, get_download_path(baseurl, fileurl, download_directory))
            except BaseException as b:
                print(b)
                pass


def function_run():
    print("--------------------")
    try:

        function()
    except BaseException as e:
        pass
    print("--------------------")


if __name__ == "__main__":
    function_run()
