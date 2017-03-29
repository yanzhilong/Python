# -*- coding: utf-8 -*-

# 定义普通的生成器及遍历
def generator1():
    print("通过列表生成器的[]改成()，创建一个generator")
    genbylist = (x for x in range(10))
    for item in genbylist:
        print(item)
    print("----------")
    # 也可以这样遍历,一般不这样用
    print("直接通过next(generator)方法遍历一个generator")
    genbylist = (x for x in range(10))
    print(next(genbylist))
    print(next(genbylist))
    print("----------")



# 斐波拉契的函数实现方式,给一个数，从0开始，0和1除外，后面一位等于前面第一位加上前面第二位的和,即f[n] = f[n-1] + f[n-2]
def fblq(max):
    print("通过方法计算斐波拉契")
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    print("----------")

# 通过函数来定义成一个generator，当调用这个函数的时候返回的是一个generator，只有在遍历的时候才计算，所以不会占用大的内存
def fblqgenerator(max):
    print("通过方法实现generator")
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1

def fblqgeneratortest():
    for x in fblqgenerator(6):
        print(x)
    print("----------")

# 通过函数实现generator
def fungenerator():
    print("自定义一个generator")
    yield 1
    yield 2
    print("----------")
    # 这个值是无法遍历到的，只能通过调用next的时候才会有异常，再通过异常的value得到
    return -1


def fungeneratortest():
    for i in fungenerator():
        print(i)

    gene = fungenerator()
    while True:
        try:
            print(next(gene))
        except StopIteration as e:
            print(e.value)
            break


if __name__ == "__main__":
    generator1()
    fblq(6)
    fblqgeneratortest()
    fungeneratortest()