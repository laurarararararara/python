# 定义函数
def mye(level):
    if level < 1:
        raise Exception("Invalid level!")
        # 触发异常后，后面的代码就不会再执行


if __name__ == '__main__':
    try:
        mye(0)  # 触发异常
    # "except"语句必须有用相同的异常来抛出类对象或者字符串
    except Exception as err:
        print(1, err)
    else:
        print(2)
