# -- coding: utf-8 --
#!/usr/bin/env python
print 1 + 2 * 4

# 创建一段脚本使用 raw_input() 内建函数从用户输入得到一个字符串，然后显示这个用户刚刚键入的字符串。
strinput = raw_input("请输入一个字符串:")
print '您刚才输入的字符串是:',strinput 


# 创建一段脚本使用 raw_input() 内建函数从用户输入得到一个数值。 将输入数据转换为一个数值对象， 
intinput = raw_input('请输入一个数字:')
print int(intinput)

# 写一个 while 循环， 输出整数从 0 到 10。
i = 0
while(i < 11):
	print i
	i +=1
i = 0
intarray = range(11)
while(i < len(intarray)):
	print intarray[i]
	i += 1

for itmp in intarray:
	print itmp
# 条件判断 判断一个数是正数， 还是负数， 或者等于 0. 开始先用固定的数值，然后修改你的代码支持用户输入数值再进行判断。

i = 1
if i > 0:
	print '正数'
elif i == 0:
	print '0'
else:
	print '负数'

i = int(raw_input('请输入一个数字:'))
if i > 0:
	print '正数'
elif i == 0:
	print '0'
else:
	print '负数'

# 循环和字串 从用户那里接受一个字符串输入，然后逐字符显示该字符串。先用 while 循环实现，然后再用 for 循环实现。
str = raw_input("请输入一个字符串:")
j = len(str)
i = 0
while(i < j):
	print str[i]
	i += 1

for item in str:
	print item

# 创建一个包含五个固定数值的列表或元组， 输出他们的和。然后修改你的代码为接受用户输入数值。 分别使用 while 和 for 循环实现。

strList = [1,2,3,4,5]
result = 0
for item in strList:
	result += item
print '列表的总和是：', result 

index = 0;
while(index < 5):
	input = raw_input('请输入第%d个数字:' % (index + 1))
	intinput = int(input)
	strList[index] = intinput
	index += 1
result = 0
for item in strList:
	result += item
print '输入的总和是：', result 

for index in range(5):
	input = raw_input('请输入第%d个数字:' % (index + 1))
	intinput = int(input)
	strList[index] = intinput
result = 0
for item in strList:
	result += item
print '输入的总和是：', result 

index = 0

result = 0
while (index < len(strList)):
	result += strList[index]
	index += 1
print '输入的总和是：', result 

# 带循环和条件判断的用户输入 使用 raw_input()函数来提示用户输入一个 1 和 100 之间的数，如果用户输入的数满足这个条件， 显示成功并退出。否则显示一个错误信息然后再次提示用户输入数值，直到满足条件为止。
tag = 1
while(tag):
	strinput = raw_input('请输入一个1-100之间的数:')
	intstr = -1
	try:
		intstr = int(strinput);
			
	except BaseException,e:
		e

	if 0 < intstr < 100:
		
		tag = 0
		print '您输入的数是:',intstr,'符合条件，程序退出'

# 带文本菜单的程序 写一个带文本菜单的程序，菜单项如下（1）取五个数的和 (2) 取五个数的平均值....（X）退出。由用户做一个选择，然后执行相应的功能。 当用户选择退出时程序结束。 这个程序的有用之处在于用户在功能之间切换不需要一遍一遍的重新启 你 动 的脚本。（ 这对 发 开 人员测试自己的程序也会大有用处）

def showMenu():
	print '请输入相应的数字或字母，选择菜单'
	print '(1)取五个数的和'
	print '(2)取五个数的平均值'
	print '(x)退出'
	str = raw_input(':')
	if str == '1':
		return 1
	elif str == '2':
		return 2
	elif str == 'x':
		return 'x'
	else:
		return 0

def jiafa():
	count = 0;
	iList = inputNum(5)
	for item in iList:
		count += item
	print '输入数的总和为：',count

def pingjun():
	count = 0;
	iList = inputNum(5)
	for item in iList:
		count += item
	print '输入数的平均值为：',count / 5

def inputNum(num):
	
	
	IList = []
	if num <= 0:
		return IList

	index = 0;
	while(index < num):
		print 'input',num,"index:",index
		try:
			str = '请输入第%d个数字:' % (index + 1)
			inputtstr = raw_input(str);
			intstr = int(inputtstr);
			IList.append(intstr)
			index += 1
		except BaseException,e:
			e
	return 	IList


tag = 1
while(tag):
	menuindex = showMenu()
	if menuindex == 1:
		jiafa()
	elif menuindex == 2:
		pingjun()
	elif menuindex == 'x':
		tag = 0


# 启动 Python 交互式解释器， 通过直接键入 dir()回车以执行 dir()内建函数。 你看到什么？ 显示你看到的每一个列表元素的值， 记下实际值和你想像的值
dir()

# 你会问, dir()函数是干什么的？我们已经知道在 dir 后边加上一对括号可以执行 dir()内建函数， 如果不加括号会如何？ 试一试。 解释器返回给你什么信息？ 你 个 认为这 信息表示什么意思 ？
dir
# <built-in function dir> 建函数

# type() 内建函数接收任意的 Python 对象做为参数并返回他们的类型。 在解释器中键入 type(dir)， 看看你得到的是什么？
print type(3)
 # <type 'int'>
type(dir)
 # <type 'builtin_function_or_method'> 内建函数或方法

 # 本练习的最后一部分， 我们来瞧一瞧 Python 的文档字符串。 通过 dir.__doc__ 可以访问 dir()内建函数的文档字符串。print dir.__doc__可以显示这个字符串的内容。 许多内建函数，方法，模块及模块属性都有相应的文档字符串。我们希望你在你的代码中也要书写文档字符串， 它会对使用这些代码的人提供及时方便的帮助。
print dir.__doc__ # 查看dir这个函数的文档字符串

def abc():
    "这个是文档字符串"
    print 'abc function run'

print abc.__doc__ # 输出abc这个函数的文档字符串
# 这个是文档字符串

# 启动Python交互解释器， 执行dir()函数， 然后键入 import sys 以导入 sys 模块。再次执行 dir()函数以确认 sys 模块被正确的导入。 然后执行 dir(sys) ， 你就可以看到 sys模块的所有属性了。

import sys
dir()
print dir(sys)

# 查看使用的 Python 解释器版本
print sys.version

# 查看使用的 Python 解释器版本
print sys.platform

# 退出解释器
# sys.exit()

# 让用户输入三个数 并将 值 分别 们 将它 保存到3个不同的变量中。不使用列表或排序算法，自己写代码 对这 来 三个数由小到大排序。(b)修改(a)的解决方案,使之从大到小排序
num1 = 0
num2 = 0
num3 = 0

num1 = raw_input("请输入一个数:")
num2 = raw_input("请输入一个数:")
num3 = raw_input("请输入一个数:")

if num1 < num2 < num3:
	print '从小到大排序是:',num1,num2,num3
	print '从大到小排序是:',num3,num2,num1
elif num1 < num3 < num2:
	print '从小到大排序是:',num1,num3,num2
	print '从大到小排序是:',num2,num3,num1
elif num2 < num1 < num3:
	print '从小到大排序是:',num2,num1,num3
	print '从大到小排序是:',num3,num1,num2
elif num2 < num3 < num1:
	print '从小到大排序是:',num2,num3,num1
	print '从大到小排序是:',num1,num3,num2
elif num3 < num1 < num2:
	print '从小到大排序是:',num3,num1,num2
	print '从大到小排序是:',num2,num1,num3
elif num3 < num2 < num1:
	print '从小到大排序是:',num3,num2,num1
	print '从大到小排序是:',num1,num2,num3
