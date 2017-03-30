# -*- coding: utf-8 -*-


def function():
    print("字典学习")
    # 定义下个字典
    dict = {"name1": "value1", "name2": "value2"}

    # 遍历一个字典(key和value)
    for key, elem in dict.items():
        print(key, elem)

        # 删除一个元素
    del dict["name1"]
    print(dict)

    # 清除字典
    dict.clear()


def function_run():
    print("--------------------")
    function()
    print("--------------------")


if __name__ == "__main__":
    function_run()
