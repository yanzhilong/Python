# -- coding: utf-8 --
# python是动态语言，不需要事先声明变量类型，变量类型在赋值的时候自动根据等等号右边确定了
# 数字类型
# int 有符号整数
# long 长整数
# bool 布尔值
# float 浮点数
# complex 复数
# 字符串

# 整数
number = 100 #十进制整数赋值
number = 0xffaa # 十六进制整数赋值

# 长整数，以L结尾,如果不加L如果超过了整数能表示的最大值，则会自动转成长整数
number = 234234234823489243879238492839898987989797492834
print number
print type(number)

# 布尔值
boo = True
boo = False
boo = 1 > 0
boo = True and True
boo = True or False
boo = not True
boo = not 3 > 1

# 算术运算符
# + - * / //(浮点的除法) %(取余) **(乘方，**是幂 - 返回x的y次幂，就是x的y次方)
result = 10 / 3 # 值是3
result = 10.0 / 3 # 值就是3.333333...
print result

# 比较运算符
# < <= > >= == != <>
boo = 1 > 0
boo = 1 > 3 > 6

# 浮点数
number = 1.23
number - -9.01
# 浮点数就是小数，称为浮点是因为小数点是可变的,1.23 * 10的9次方和12.3 * 10 9次方是一样的，科学表示法就是把10换成e
number = 1.23e9
number = 0.000012  # 也可以写成
number = 1.2e-5 # 表示1.2乘以10的负5次方
name = "您好的名字是%s" % "严志龙"
print name

# 复数

# 字符串
pystr = '字符串值'
pystr = "字符串值"
pystr = """字符串值"""
pystr = 'I\'m "Michael"' # 字符串的转义
pystr = '\\' # 使用了转义,输出一个\
pystr = '\t' # 使用了转义,输出一个制表符
pystr = '\n' # 使用了转义,输出一个换行符
pystr = '\\' # 使用了转义,输出一个\
pystr = r'这里面的字符默认不转义abc\t\n"' # 会直接输出一样的字符
pystr = "asdfsdf"'sdfsdf'"asdfasdf" # 多个字符串默认会直接连接字符串
pystr = 'asd'
pystr = 'sdf' + pystr # 带变量的则需要用+连接字符串
pystr = """多行
内容就不需要输换行符，
直接使用三个引号就
可以了，
默认会加换行符"""
print pystr # 直接带换行符的输出
pystr = "abcdefg" # 字符串默认当作了一个列表，也可以说是一个普通的数组，每个项为字符串的一个字母或汉字
print pystr[0]
str = "python " + "is easy" # 字符串的连接
str = "python" * 2 # 字符串的重复，输出pythonpython

# 字符编码
# ASCII 最早只有127个字母编入
# Unicode 解决全球通过编码的问题，但都会有两个字节以上，会浪费
# UTF-8 可变长的Unicode编码 1 - 6个字节
# 计算机的工作统一使用Unicode编码,需要存储和传输的时候采用UTF-8

# ASCII码和字母的转换
a_ascii = ord('A') # 65
print a_ascii
a_letter = chr(65)
print a_letter

# 字符串格式化
#%s 字符串
#%d 整数
#%f 浮点数
#%x 十六进制

pystr = "Hello %s %s" % ("严志龙","How are you")
pystr = "Hello %s" % "严志龙" # 只有一个参数的时候可以省略
pystr = "比例是 %d%%" % 7 # 字符串需要%的时候要转义
print pystr
pystr = "比例是7%"
print pystr




# 空值None

# 变量在内存中的表现
a = "ABC"
# 内存中做了两件事
# 在内存中创建一个ABC的字符串
# 在内存中创建一个名为a的变量，并指向ABC
b = a
a = "XYZ"
print b # 这时b还是ABC,因为a只是重新指向了一个存放XYZ的地址而已

# 常量一般是全部大小
PI = 3.141596