# This is a sample Python script.

'''
if/else
and or
'''


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    num = 9
    if 0 <= num <= 10:  # 判断值是否在0~10之间
        print('hello')
    # 输出结果: hello

    num = 10
    if num < 0 or num > 10:  # 判断值是否在小于0或大于10
        print('hello')
    else:
        print('undefined')

    num = 8
    # 判断值是否在0~5或者10~15之间
    if 0 <= num <= 5 or 10 <= num <= 15:
        print('hello')
    else:
        print('undefined')

var = 100
if var == 100:
    print("变量 var 的值为100")
print("Good bye!")

count = 0
while count < 9:
    print('The count is:', count)
    count = count + 1
print("Good bye!")

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print('偶数：', i)  # 输出双数2、4、6、8、10

i = 1
while True:  # 循环条件为1或True必定成立
    print(i)  # 输出1~10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break

# 1~10的for循环
for a in range(1, 10):
    print('1～10：', a)
