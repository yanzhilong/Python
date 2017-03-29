# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 加载javascript基本使用，设定等待时间是3秒
def function_base():
    print("利用Selenium和phantom采集浏览器数据")
    # 指定PhantomJS的可执行文件路径
    driver = webdriver.PhantomJS(executable_path='phantomjs-2.1.1-windows/bin/phantomjs.exe')
    # driver = webdriver.PhantomJS(executable_path='C:\\Users\\yanzl\\Desktop\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe') #这个也可以
    driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
    print("打开成功，等待3秒")
    time.sleep(3)
    print(driver.find_element_by_id('content').text)
    print(driver.find_element_by_css_selector("#content"))
    print(driver.find_element_by_tag_name("div"))
    # 如果想获取同样特征的多个元素
    print("如果想获取同样特征的多个元素")
    print(driver.find_elements_by_tag_name("div"))
    # 使用BeautifulSoup来解析
    print("使用BeautifulSoup来解析")
    pagesource = driver.page_source
    bsobj = BeautifulSoup(pagesource,"html.parser")
    print(bsobj.find(id="content").get_text())
    driver.close()


# 测试加载百度页面
def function_baidu():
    print("利用Selenium和phantom采集百度")
    driver = webdriver.PhantomJS(executable_path='phantomjs-2.1.1-windows/bin/phantomjs.exe')
    # driver = webdriver.PhantomJS(executable_path='C:\\Users\\yanzl\\Desktop\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe') #这个也可以
    driver.get("https://www.baidu.com/")
    print("打开成功，等待3秒")
    time.sleep(5)
    print(driver.page_source)
    driver.close()


# 自动等待加载完成
def function_wait():
    print("利用Selenium和phantom采集浏览器数据")
    # 指定PhantomJS的可执行文件路径
    driver = webdriver.PhantomJS(executable_path='phantomjs-2.1.1-windows/bin/phantomjs.exe')
    driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
    print("打开成功，等待页面加载完成")
    try:
        # 等待页面加载完成,最长10秒
        element = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, "loadedButton")))
    finally:
        print(driver.find_element_by_id('content').text)
        driver.close()


def function_run():
    print("--------------------")
    function_base()
    print("--------------------")
    function_baidu()
    print("--------------------")
    function_wait()
    print("--------------------")
if __name__ == "__main__":
    function_run()
