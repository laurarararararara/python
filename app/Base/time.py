import calendar
import time

def changeInt(a):
    a = 10


def changeMe(mylist):
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


def printInfo(name, age):
    print("Name: ", name)
    print("Age ", age)
    return


# 可写函数说明
def printInfo2(arg1, *vartuple):
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total


if __name__ == '__main__':
    print("和为：", sum(2, 4))

    printInfo2("args")
    printInfo2(6, 45, 2, 12)

    cal = calendar.month(2022, 1)
    print("以下输出2016年1月份的日历:")
    print(cal)

    # 格式化成2016-03-20 11:45:39形式
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    # 格式化成Sat Mar 28 22:24:24 2016形式
    print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

    # 将格式字符串转换为时间戳
    a = "Sat Mar 28 22:24:24 2016"
    print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

    '''
    实例中有 int 对象 2，指向它的变量是 b，在传递给 ChangeInt 函数时，按传值的方式复制了变量 b，
    a 和 b 都指向了同一个 Int 对象，在 a=10 时，则新生成一个 int 值对象 10，并让 a 指向它。
    '''
    b = 2
    changeInt(b)
    print(b)  # 结果是 2`

    '''
    调用changeMe函数,
    # 函数内取值:  [10, 20, 30, [1, 2, 3, 4]]
    # 函数外取值:  [10, 20, 30, [1, 2, 3, 4]]
    '''
    mylist = [10, 20, 30]
    changeMe(mylist)
    print("函数外取值: ", mylist)

    printInfo(age="zhangsan", name=20)
    printInfo(age=24, name="kihd")
