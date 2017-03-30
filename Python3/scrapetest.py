from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

# 简单输出一个网页的html
html = ""
try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
else:
    pass
if html is None:
    print("URL is not found")
else:
    bsobj = BeautifulSoup(html.read(), "html.parser")
    print(bsobj.h1)
    print(bsobj.body)
    print(bsobj.html)


# 通过方法的封装，将异常封装在方法内
def gettitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsobj = BeautifulSoup(html.read(), "html.parser")
        title = bsobj.h1
    except:
        return None
    return title

title = gettitle("http://pythonscraping.com/pages/page1.html")
if title is None:
    print("Title could not be 'bound'")
else:
    print(title)


# 通过异常处理输出一个不存在的标签
try:
    badContent = bsobj.nonExisting.someTag
except AttributeError as e:
    print("Tag was not found")
else:
    if badContent is None:
        print("Tag was not found")
    else:
        print(badContent)


# 通过css属性过虑网页
# bsObj.findAll(tagName, tagAttributes) 获得页面中所有指定的标签
# bsobj.tagName获取页面中第一个指定的标签
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsobj = BeautifulSoup(html.read(), "html.parser")
#
# bsobj.div.findAll()会在bsobj里面的第一个dev下面去查找
namelist = bsobj.findAll("span", {"class": "green"})

# 遍历包含span标签且class属性是green的标签及内容
for name in namelist:
    # 这个name会包含html标签,这个就是BeautifulSoup里面的Tag标签对象
    print(name)

# 遍历包含span标签且class属性是green的去除标签后的内容
for name in namelist:
    # get_text()方法会去除所有的html标签
    print(name.get_text())

# findAll(tag,attributes,recursive,text,limit,**kwargs)
# tag可以是标签也可以是标签列表，attributes是字典标签属性
# recursive 是否递归查找子标签
# text属性用于匹配标签里面的内容是否包含指定的内容,这里是完全匹配
# limit限制个数,find()方法相当于默认限制是1个
# **kwargs 用于指定一些具有指定属性的标签,就是都要满足的，和上面的attributes的或关系是不一样的
otherlist = bsobj.findAll({"h1", "span"}, {"class": "red"})
otherlist = bsobj.findAll({"span"}, {"class": "green"}, True, "King of Prussia")
print(len(otherlist))
otherlist = bsobj.findAll({"span"}, {"class": "green"}, True, "Abbe")
print(len(otherlist))
otherlist = bsobj.findAll(id="text", name="aaa")
print(len(otherlist))
# 当具名参数是class的时候可以在后面加_，因为class是关键字
otherlist = bsobj.findAll(class_="green")
print(len(otherlist))

# BeautifulSoup里面的这里会用到的所有对象
# BeautifulSoup
# Tag对象，就是查找到的元素对象
# NavigableString 是标签里的文字，后面会用到
# Comment 用来查找html里面的注释标签

# 子标签和后代标签,子标签是直接的下一级标签，后代标签是所有递归遍历所有折子标签

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsobj = BeautifulSoup(html.read(), "html.parser")
# 查看body所有的后代span标签
descendantlist = bsobj.body.findAll("span")

# 查看table,id:giftList下的所有子标签
for child in bsobj.find("table", {"id": "giftList"}).children:
    print(child)

# 查看table,id:giftList下的所有后代标签
for child in bsobj.find("table", {"id": "giftList"}).descendants:
    print(child)

# 处理兄弟标签
print("打印table下面的tr的兄弟标签")
# 这里先找到table下面的tr标签，在这个网页中是一个标题，当返回的时候是不包含本身这个标签的.
for sibling in bsobj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)

# 在上面的例子中也可以直接使用这种方法,这样会直接找到第一个表格的第一个标签，前提是需要的数据就是第一个标签，建议还是用上面的方法好,
# 为了爬虫的稳定，尽量选择知道的属性.防止变更的网页导致抓取失败
for sibling in bsobj.tr.next_siblings:
    print(sibling)

# 如果能找到最后一个标签也可以使用previous_siblings函数返回前面的所有兄弟标签
# next_sibling 查看下一个兄弟标签
# previous_sibling 查看上一个兄弟标签

price = bsobj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()
print(price)

# 通过正则表达式查找上面网页中的所有的图片链接
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsobj = BeautifulSoup(html.read(), "html.parser")
images = bsobj.findAll("img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})

# 这里的image就是Tag标签对象，可以通过Tag["属性名"]获取属性的值
for image in images:
    image.attrs # 获取这个标签的全部属性,是一个字典对象
    print(image["src"])

# Lambda表达式
# 这种函数定义的方式是：f(g(),y) 或f(g(x),h(x))
# BeautifulSoup允许传入一个Tag标签对象，返回一个布尔值，如果是真的就会保留，Falst的就是丢弃
bsobj.findAll(lambda tag:len(tag.attrs) == 2) # 返回属性的个数是2的标签列表
# <div class = "body" id = "content"></div>

# 爬虫维基百科，从一个页面经过词条的遍历，到达指定的另一个页面，看需要经过多少个的链接能到达.

# 获得一个页面的/wiki/....的链接
html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon") # Kevin Bacon的维基百科页面
bsobj = BeautifulSoup(html.read(), "html.parser")
for link in bsobj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    if "href" in link.attrs:
        print(link.attrs["href"])

# 从一个页面初始锋利一个链接列表，并随机获取一个页面，递归操作，直到链接列表为0
random.seed(datetime.datetime.now())
def getlinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsobj = BeautifulSoup(html.read(), "html.parser")
    return bsobj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getlinks("/wiki/Kevin_Bacon")
# while len(links) > 0:
#     newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
#     print(newArticle)
#     links = getlinks(newArticle)

# 爬虫维基百科,跳转所有页面，并打印一些东西
pages = set()
start = False
def getlinks(pageurl):
    global pages # 定义全局变量，这样才能在函数里使用
    html = None
    try:
        html = urlopen("http://en.wikipedia.org" + pageurl)
    except HTTPError:
        print("http://en.wikipedia.org" + pageurl + "无法找到")
        return
    bsobj = BeautifulSoup(html.read(), "html.parser")

    # 下面输出一些内容
    try:
        print(bsobj.h1.get_text())
        print(bsobj.find(id="mw-content-text").findAll("p")[0])
        print(bsobj.find(id="ca-edit").find("span").find("a").attrs["href"])
    except AttributeError:
        print("页面缺少一些属性，不过不用担心")
    except IndexError:
        pass
    for link in bsobj.findAll("a",href = re.compile("^(/wiki/)")):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                # """ 新页面 """
                newPage = link.attrs["href"]
                print("-----------------------\n" + str(len(pages)) + ": " + newPage)
                pages.add(newPage)
                getlinks(newPage) # 递归调用
if not not start:
    start = True
    getlinks("")

# 通过互联网的爬虫
pages = set()
random.seed(datetime.datetime.now())

# 获取内页所有内链的列表
def getinternallink(bsobj,includeurl):
    internallinks = []
    # 找出以/开头的链接
    for link in bsobj.findAll("a", href = re.compile("^(/|.*" + includeurl + ")")):
        if link.attrs["href"] not in internallinks:
            internallinks.append(link.attrs["href"])
    return internallinks

# 获取所有外链的列表
def getexternallinks(bsobj,excludeurl):
    externallinks = []
    # 找出所有以"http"或"www"开关且不包含当前URL的链接
    for link in bsobj.findAll("a", href = re.compile("^(http|www)((?!" + excludeurl + ").)*$")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in externallinks:
                externallinks.append(link.attrs["href"])
    return externallinks

# 解析网址,获取一个网直接的主机部分
def spliitaddress(address):
    addressparts = address.replace("http://","").split("/")
    return addressparts

# 在指定页面获取一个外面链接
def getrandomexternallink(startingpage):
    html = None
    try:
        html = urlopen(startingpage)
    except HTTPError:
        print(startingpage + "打开异常")
        return None
    bsobj = BeautifulSoup(html.read(), "html.parser")
    externalinks = getexternallinks(bsobj,spliitaddress(startingpage)[0])
    if len(externalinks) == 0:
        internallinks = getinternallink(bsobj,startingpage)
        return getexternallinks(bsobj,internallinks[random.randint(0,len(externalinks) - 1)])
    else:
        return externalinks[random.randint(0,len(externalinks) - 1)]


# 开始获取网页的一个外链，并打印
def followExternalOnly(startingSite):
    externalink = getrandomexternallink(startingSite)
    print("随机外链是：" + externalink)
    followExternalOnly(externalink)

# followExternalOnly("http://oreilly.com")

allExtlinks  = set()
allIntlinks = set()

# 获得一个网址的所有外链
def getallexternallinks(siteurl):
    html = urlopen(siteurl)
    bsobj = BeautifulSoup(html.read(),"html.parser")
    internallinks = getinternallink(bsobj,spliitaddress(siteurl)[0])
    externallinks = getexternallinks(bsobj,spliitaddress(siteurl)[0])
    for link in externallinks:
        if link not in allExtlinks:
            allExtlinks.add(link)
            print("外链" + link)
    for link in internallinks:
        if link not in allIntlinks:
            print("找到一个内链" + link)
            allIntlinks.add(link)
            getallexternallinks(link)


getallexternallinks("http://oreilly.com")



