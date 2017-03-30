# -*- coding: utf-8 -*-
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup


def function():
    print("采集表格数据保存csv")
    html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
    bsobj = BeautifulSoup(html.read(), "html.parser")
    # 主要对比表格是当前页面上的第一个表格
    table = bsobj.findAll("table", {"class": "wikitable"})[0]
    rows = table.findAll("tr")
    csvfile = open("Download/editors.csv", "w", encoding='utf-8', newline="")
    writer = csv.writer(csvfile)
    try:
        for row in rows:
            csvrow = []
            # 查找所有的td，或th元素
            for cell in row.findAll(['td', 'th']):
                csvrow.append(cell.get_text())
            writer.writerow(csvrow)
    finally:
        csvfile.close()


def function_run():
    print("--------------------")
    function()
    print("--------------------")


if __name__ == "__main__":
    function_run()
