# -- coding: utf-8 --
# if elif else语句
age = 100
message = ""
if age < 18:
	message = "you are very young"
elif age < 30:
	message = "you are not old"
else:
	message = "you are old"
print message;

if 1: # 任何非零，非空的，及列表数不为空的数都是返回True,否则返回False
	print "1是True"

if '1988' < 2000:
	print "'1988' < 2000" # 会输出这个，因为字符串不能和数字比较，比较了值会不正确
else:
	print "'1988' >= 2000"

num = int("19") # 可以通过int()函数将字符串转换成数字


# while循环

index = 8
while index > 0:
	print index
	index -= 1

# for循环
names = ["name1","name2","name3","name4"]
for name in names:
	print name

# range()函数的使用
nums = [0,1,2,3,4] # 定义一个列表
nums = range(5) # 定义一个跟上面一样的列表

# 根据range的规则，就可以配合for循环进行下标的迭代了
names = ["严志龙1","严志龙2","严志龙3","严志龙4","严志龙5","严志龙6"]
num = len(names); # 得到列表的长度
fornum = range(num) # 根据列表的长度生成整数序列,值是:0-参数-1,
for index in fornum:
	print names[index]


# enumerate()函数遍历列表的值和索引
names = ["严志龙1","严志龙2","严志龙3","严志龙4","严志龙5","严志龙6"] 
for i,name in enumerate(names):
	print name + "的下标是:%d" % i
