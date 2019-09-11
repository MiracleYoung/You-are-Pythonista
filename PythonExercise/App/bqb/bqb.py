# 捂脸表情

import turtle


# 画指定的任意圆弧
def arc(sa, ea, x, y, r):  # start angle,end angle,circle center,radius
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.left(sa)
    turtle.fd(r)
    turtle.pendown()
    turtle.left(90)
    turtle.circle(r, (ea - sa))
    return turtle.position()


turtle.hideturtle()
# 画脸
turtle.speed(5)
turtle.setup(900, 600, 200, 200)
turtle.pensize(5)
turtle.right(90)
turtle.penup()
turtle.fd(100)
turtle.left(90)
turtle.pendown()
turtle.begin_fill()
turtle.pencolor("#B26A0F")  # head side color
turtle.circle(150)
turtle.fillcolor("#F9E549")  # face color
turtle.end_fill()

# 画嘴
turtle.penup()
turtle.goto(77, 20)
turtle.pencolor("#744702")
turtle.goto(0, 50)
turtle.right(30)
turtle.fd(110)
turtle.right(90)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#925902")  # mouth color
turtle.circle(-97, 160)
turtle.goto(92, -3)
turtle.end_fill()
turtle.penup()
turtle.goto(77, -25)
# 画牙齿
turtle.pencolor("white")
turtle.begin_fill()
turtle.fillcolor("white")
turtle.goto(77, -24)
turtle.goto(-81, 29)
turtle.goto(-70, 43)
turtle.goto(77, -8)
turtle.end_fill()

turtle.penup()
turtle.goto(0, -100)
turtle.setheading(0)
turtle.pendown()

# 画左边眼泪
turtle.left(90)
turtle.penup()
turtle.fd(150)
turtle.right(60)
turtle.fd(-150)
turtle.pendown()
turtle.left(20)
turtle.pencolor("#155F84")  # tear side color
turtle.fd(150)
turtle.right(180)
position1 = turtle.position()
turtle.begin_fill()
turtle.fillcolor("#7EB0C8")  # tear color
turtle.fd(150)
turtle.right(20)
turtle.left(270)
turtle.circle(-150, 18)
turtle.right(52)
turtle.fd(110)
position2 = turtle.position()
turtle.goto(-33, 90)
turtle.end_fill()
# 画右边眼泪
turtle.penup()
turtle.goto(0, 0)
turtle.setheading(0)
turtle.left(90)
turtle.fd(50)
turtle.right(150)
turtle.fd(150)
turtle.left(150)
turtle.fd(100)
turtle.pendown()
turtle.begin_fill()
turtle.fd(-100)
turtle.fillcolor("#7EB0C8")  # tear color
turtle.right(60)
turtle.circle(150, 15)
turtle.left(45)
turtle.fd(66)
turtle.goto(77, 20)
turtle.end_fill()
# 画眼睛
turtle.penup()
turtle.pencolor("#6C4E00")  # eye color
turtle.goto(-65, 75)
turtle.setheading(0)
turtle.left(27)
turtle.fd(38)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#6C4E00")  # eye color
turtle.left(90)
turtle.circle(38, 86)
turtle.goto(position2[0], position2[1])
turtle.goto(position1[0], position1[1])
turtle.end_fill()

# 画手
turtle.pencolor("#D57E18")  # hand side color
turtle.begin_fill()
turtle.fillcolor("#EFBD3D")  # hand color
# 第一个手指
arc(-110, 10, 110, -40, 30)
turtle.circle(300, 35)
turtle.circle(13, 120)
turtle.setheading(-50)
turtle.fd(20)
turtle.setheading(130)
# 第二个手指
turtle.circle(200, 15)
turtle.circle(12, 180)
turtle.fd(40)
turtle.setheading(137)
# 第三个手指
turtle.circle(200, 16)
turtle.circle(12, 160)
turtle.setheading(-35)
turtle.fd(45)
turtle.setheading(140)
# 第四个手指
turtle.circle(200, 13)
turtle.circle(11, 160)
turtle.setheading(-35)
turtle.fd(40)
turtle.setheading(145)
# 第五个手指
turtle.circle(200, 9)
turtle.circle(10, 180)
turtle.setheading(-31)
turtle.fd(50)
# 画最后手腕的部分
turtle.setheading(-45)
turtle.pensize(7)
turtle.right(5)
turtle.circle(180, 35)
turtle.end_fill()
turtle.begin_fill()
turtle.setheading(-77)
turtle.pensize(5)
turtle.fd(50)
turtle.left(-270)
turtle.fd(7)
turtle.pencolor("#EFBD3D")
turtle.circle(30, 180)
turtle.end_fill()
# 测试
# res=arc(70,220,90,50,300)
# print(res[0],res[1])

turtle.done()


'''
# 斜眼笑表情
'''
import turtle as t

# -------------脸
t.setup(960, 959, 0, 0)
t.color("orange")
t.pensize("25")
t.penup()
t.goto(-300, 0)
t.pendown()
t.left(90)
t.fillcolor("yellow")
t.begin_fill()
t.circle(-300)
t.end_fill()

# -----------嘴-----------
t.penup()
t.goto(-220, -10)
t.seth(90)
for i in range(90):
    t.pensize(4 + 0.15 * i)
    t.color("brown")
    t.pendown()
    t.circle(-220, -1)
for i in range(90):
    t.pensize(17.5 - 0.15 * i)
    t.color("brown")
    t.pendown()
    t.circle(-220, -1)

    # ------------左眼---------------
t.penup()
t.goto(-80, 150)
t.color("orange")
t.pensize("25")
t.seth(90)
t.pendown()
t.left(50)
t.circle(200, 80)
t.seth(270)
t.circle(200, 15)

t.penup()
t.goto(-70, 90)
t.color("orange")
t.pensize("25")
t.seth(90)
t.pendown()
t.left(50)
t.circle(200, 65)
t.left(10)
t.circle(200, 10)

t.penup()
t.goto(-70, 150)
t.seth(270)
t.pendown()
t.circle(-200, 15)

# -------------右眼----------------


t.penup()
t.goto(70, 150)
t.color("orange")
t.pensize("25")
t.seth(90)
t.pendown()
t.right(50)
t.circle(-200, 80)
t.seth(270)
t.circle(-200, 15)

t.penup()
t.goto(70, 90)
t.seth(90)
t.pendown()
t.right(50)
t.circle(-200, 65)
t.right(10)
t.circle(200, 10)

t.penup()
t.goto(70, 150)
t.seth(270)
t.pendown()
t.circle(200, 15)

t.penup()
t.pensize(5)
t.color("black")
t.goto(-300, 125)
t.pendown()
t.seth(0)
t.fillcolor('black')
t.begin_fill()
t.circle(15, 360)
t.end_fill()

t.penup()
t.pensize(5)
t.color("black")
t.goto(100, 120)
t.pendown()
t.seth(0)
t.fillcolor('black')
t.begin_fill()
t.circle(15, 360)
t.end_fill()

# ----------左眉毛-----------------
t.penup()
t.goto(-70, 200)
t.color("black")
t.pensize("25")
t.seth(90)
t.pendown()
t.left(30)
t.circle(200, 60)

# ----------右眉毛-----------------
t.penup()
t.goto(70, 200)
t.color("black")
t.pensize("25")
t.seth(90)
t.pendown()
t.right(30)
t.circle(-200, 60)

# ---------左红-------------------
t.penup()
t.color("red")
t.goto(150, 20)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(20)
t.end_fill()

# ---------右红----------------
t.penup()
t.color("red")
t.goto(-180, 20)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(20)
t.end_fill()

t.done()
