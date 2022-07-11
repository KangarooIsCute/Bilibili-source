# 错误 error
# 异常 exception

def test_fails(num):
    return 1/num
try:
    num = int(input("please input number:"))
    result = test_fails(num)
    print(result)
except ZeroDivisionError as error:
    print(error)
except ValueError as error:
    print(error)