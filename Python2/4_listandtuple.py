# -- coding: utf-8 --
# list 列表
strList = ['Name1','Name2','Name3']
intList = [1,2,3]
arrayList = ['Name',1,'Age'] # 数据可以不同
arrayList1 = ['Name',1,'Age',arrayList,["123",123]] # 数据可以是另一个列表
arrayList1[4][1] # 要取上面的123可以通过二维数组的形式取数据
item = arrayList[0]; #得到某个位置的元素,从0开始
item = arrayList[len(arrayList)-1]; # 最后一个元素
item = arrayList[-1]; # -1也可以得到最后一个元素
item = arrayList[-2]; # 可以以此类推，得到倒数第二个元素-2
itemcount = len(arrayList) # 获得元素的个数
arrayList.append("newValue") #可以尾部追加一个新的值 
arrayList.insert(1,"newValue") #可以任意位置追加一个新的值 
arrayList.pop() #删除末尾的元素
arrayList.pop(1) # 删除指定位置的元素
arrayList[0] = "new" # 替换某个位置的值

# tuple 元组
# 元组一旦定义了就不能改变了
tuples = ("sdf","123",123) # 定义的时候就要确定数量
tuples = () # 定义一个空的元，但没有意义
tuples = (1) # 这样相当于是tuples = 1,因为()会当作数据运算里的()
tuples = (1,) # 这样才算是定义了只有一个元素的元组
tuples = (1,2,["12",1]) # 通过里面的列表元素可以变向的改变tuples的值
# tuples[0] = 9 # 会出错
tuples[2][0] = "new" # 改变list的值

