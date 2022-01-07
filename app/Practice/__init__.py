import time
from math import sqrt
"""
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
"""


def repeat():
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (i != k) and (i != j) and (j != k):
                    print(i, j, k)


'''
输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：'''


def day(year, month, day):
    months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
    if 0 < month <= 12:
        sum = months[month - 1]
    else:
        print('data error')
    sum += day
    leap = 0
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        leap = 1
    if (leap == 1) and (month > 2):
        sum += 1
    print('it is the %dth day.' % sum)
'''
输入三个整数x,y,z，请把这三个数由小到大输出'''

'''斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：1、1、2、3、5、8、13、21、34、……'''


def feibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return feibo(n - 1) + feibo(n - 2)


def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def small(x, y, z):
    l = [x, y, z]
    l.sort()
    print(l)

'''判断101-200之间有多少个素数，并输出所有素数。'''


def isPrime():
    h = 0
    leap = 1
    for m in range(101, 201):
        k = int(sqrt(m + 1))
        for i in range(2, k + 1):
            if m % i == 0:
                leap = 0
                break
        if leap == 1:
            print('%-4d' % m)
            h += 1
        leap = 1
    print('The total is %d' % h)


if __name__ == '__main__':
    isPrime()
    print(feibo(3))
    print(feibo(5))
    print(fib(5))
    small(6, 5, 7)
    repeat()
    day(2021, 1, 1)

    '''复制数组'''
    a = [1, 2, 3]
    b = a[:]
    print(b)


myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print(key, value)
    time.sleep(1)  # 暂停 1 秒