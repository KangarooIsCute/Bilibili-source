# 使用汉堡包式编程法:

###############################引用数据库与函数函数############################

from turtle import *
from gamebase import square
from random import randrange
from time import sleep
###############################定义变量########################################

snake = [[0,0],[10,0],[20,0],[30,0],[40,0],[50,0]]
apple_x = randrange(-20,18)*10
apple_y = randrange(-19,19)*10
aim_x = 0
aim_y = 10

###############################定义函数#######################################
def change(x,y):
    global aim_x,aim_y
    aim_x = x
    aim_y = y

def inside_snake():
    for n in range(len(snake)-1):
        if snake[-1][0] == snake [n][0] and snake[-1][1]:
            return True

    return False

def inside_map():
    if -200<=snake[-1][0]<=180 and -190<=snake[-1][1]<=190:
        return True
    else:
        return False
def gameloop():
    global apple_x,apple_y,aim_x,aim_y,snake 
    snake.append([snake[-1][0]+aim_x , snake[-1][1]+aim_y ])
    print(snake[-1][0],snake[-1][1])

    # 要到苹果时加一个的效果，和要到苹果时删除原来的苹果，添加新苹果的效果
    if snake[-1][0]!=apple_x or snake[-1][1]!=apple_y:
        snake.pop(0)
    else:
        apple_x = randrange(-20,18)*10
        apple_y = randrange(-19,19)*10
        # 检测是否要到自己或者碰到墙壁
    if (not inside_map()):
        square(snake[-1][0], snake[-1][1],10,"red")
        update()
        sleep(2)
        snake = [[0,0],[10,0],[20,0],[30,0],[40,0],[50,0]]
        apple_x = randrange(-20,18)*10
        apple_y = randrange(-19,19)*10
        aim_x = 0
        aim_y = 10
    # 定义苹果、边框和内部空白区域的颜色
    clear()
    square(-210,-200,410,"black")
    square(-200,-190,390,"white")
    square(apple_x,apple_y,10,"red")

    for n in range(len(snake)):
        square(snake[n][0],snake[n][1],10,"black")

    ontimer(gameloop,159)
    update()
##########################主程序############################################
setup(420,420,0,0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(0,10), "w")
onkey(lambda: change(0,-10), "s")
onkey(lambda: change(-10,0), "a")
onkey(lambda: change(10,0), "d")
gameloop()
done()