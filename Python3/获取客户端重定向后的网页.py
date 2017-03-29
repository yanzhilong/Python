# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException


# 等页面页面跳转，一直查看某一个html标签是否还在，如果不在就是跳转了
def waitforload(driver):
    ele = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count > 20:
            print("Timing out after 10 seconds and returning")
            return
        time.sleep(.5)
        try:
            # 当标签不在的时候会出现异常
            elem = driver.find_element_by_tag_name("html")
        except StaleElementReferenceException:
            return


def function():
    print("采集等待页面跳转后的页面数据")
    driver = webdriver.PhantomJS(executable_path='phantomjs-2.1.1-windows/bin/phantomjs.exe')
    driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
    waitforload(driver)
    print(driver.page_source)





def function_run():
    print("--------------------")
    function()
    print("--------------------")


if __name__ == "__main__":
    function_run()
