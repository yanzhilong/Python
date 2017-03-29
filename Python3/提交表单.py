# -*- coding: utf-8 -*-
import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

def login_base():
    print("提交表单测试")
    params = {'firstname': 'Ryan', 'lastname': 'Michell'}
    r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
    print(r.text)


# 上传文件的表单
def upload_file():
    print("上传文件示例")
    files = {'uploadfile': open('Download/logo.jpg', 'rb')}
    r = requests.post("http://pythonscraping.com/pages/processing2.php",
files=files)
    print(r.text)


# 登陆的时候处理了cookie
def login_cookie():
    print("使用requests的cookie方式登陆")
    params = {'username': 'Ryan', 'password': 'password'}
    r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
    print("Cookie is set to:")
    print(r.cookies.get_dict())
    print("----------")
    print("Going to profile page...")
    r = requests.get("http://pythonscraping.com/pages/cookies/profile.php",
cookies=r.cookies)
    print(r.text)


# 登陆的时候处理了session,这样会自动处理cookie
def login_session():
    print("使用requests的session方式登陆")
    session = requests.session()
    params = {'username': 'Ryan', 'password': 'password'}
    r = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
    print("Cookie is set to:")
    print(r.cookies.get_dict())
    print("----------")
    print("Going to profile page...")
    r = requests.get("http://pythonscraping.com/pages/cookies/profile.php",
cookies=r.cookies)
    print(r.text)


# 登陆需要http接入认证的网站
def login_auth():
    print("使用http接入认证方式登陆")
    auth = HTTPBasicAuth('Ryan','password')
    r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", auth)
    print(r.text)


def function_run():
    print("--------------------")
    login_base()
    print("--------------------")
    upload_file()
    print("--------------------")
    login_cookie()
    print("--------------------")
    login_session()
    print("--------------------")
    login_auth()
    print("--------------------")


if __name__ == "__main__":
    function_run()
