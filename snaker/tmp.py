from random import random,choice
from turtle import *

player=[0,-140]
ball=[0,140]
diraction=[choice([-2,-1,1,2]),choice([-2,-1])]

def move(aim):

def bounce():
    if ball[0]<=300 or ball[0]>=290:
        diraction[0]=-diraction[0]
    elif ball[1]>=150:
        diraction[1]=-diraction[1]
    elif ball[1]<=-140+10+15 and player[0]<=ball[0]<=player[0]+70:
        diraction[1]+-diraction[1]

def outside():
    if ball[1]<=-140 :
        return True

def ractangle(x,y,width,height):
    up()
    goto(x,y)
    begin_fill()
    for n in range(2):
        forward(width)
        left(90)
        frward(height)
        left(90)
    end_fill()
def draw():
    clear()
    up()
    goto(ball[0],ball[1])
    dot(10,"red")
    rectangle(player[0],player[1],70,10)
    update()
def gameLoop():
    bounce()
    ball[0] +=diraction[0]*2
    ball[1] +=diraction[1]*2
    draw()
        if outside():
            return
        ontimer(gameLoop,50)

setup(620,420,200,0)
hideturtle()
tracer(False)
listen()
onkey(lambda:move(20),'d')
onkey(lambda:move(-20),'a')
gameLoop()
done()