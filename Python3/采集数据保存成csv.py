# -*- coding: utf-8 -*-
import csv

def function():
    print("")


def function_create_csv():
    print("手动创建一个csv文件")
    csv_file = open("Download\\test.csv", 'w', encoding='utf8', newline='')
    try:
        writer = csv.writer(csv_file)
        writer.writerow(('number', 'number plus 2', 'number times 2'))
        for i in range(10):
            writer.writerow((i, i+2, i*2))
    finally:
        csv_file.close()


def function_run():
    print("--------------------")
    function()
    print("--------------------")
    function_create_csv()
    print("--------------------")
if __name__ == "__main__":
    function_run()

