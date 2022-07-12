import random

num = random.randint(0,100)
while True:
    gnum = int(input("请输入数字:"))
    if gnum < num:
        print("小了")
    elif gnum > num:
        print("大了")
    else:
        print("对了")
        break