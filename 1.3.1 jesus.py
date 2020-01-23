import turtle as trtl


J = trtl.Turtle()
A= trtl.Turtle()

# Make the outer out line!?
J.speed(0)
J.pensize(3)
J.pencolor("blue")
J.ht()
J.penup()
J.goto(350,-50)
J.pendown()

A.color("yellow")
A.pencolor("black")
A.shape("circle")

J.right(180)
J.forward(150)
J.lt(90)
J.fd(125)
J.lt(90)
J.forward(150)
J.rt(90)
J.fd(200)

J.rt(90)
J.fd(700)

J.rt(90)
J.fd(200)
J.rt(90)
J.forward(150)
J.lt(90)
J.fd(125)
J.lt(90)
J.forward(150)

J.penup()
J.rt(90)
J.fd(100)
J.pendown()

J.right(90)
J.forward(150)
J.lt(90)
J.fd(125)
J.lt(90)
J.forward(150)
J.rt(90)
J.fd(200)

J.rt(90)
J.fd(700)

J.rt(90)
J.fd(200)
J.rt(90)
J.forward(150)
J.lt(90)
J.fd(125)
J.lt(90)
J.forward(150)

# Make the inner out line!?

J.penup()
J.goto(350,-40)
J.pendown()

J.right(180)
J.forward(160)
J.lt(90)
J.fd(145)
J.lt(90)
J.forward(150)
J.rt(90)
J.fd(80)
J.rt(90)
J.fd(40)
J.lt(90)
J.fd(15)
J.lt(90)
J.fd(40)
J.rt(90)
J.fd(85)

J.rt(90)
J.fd(680)


J.rt(90)
J.fd(80)
J.rt(90)
J.fd(40)
J.lt(90)
J.fd(15)
J.lt(90)
J.fd(40)
J.rt(90)
J.fd(85)
J.rt(90)
J.forward(150)
J.lt(90)
J.fd(145)
J.lt(90)
J.forward(160)

J.penup()
J.rt(90)
J.fd(80)
J.pendown()

J.right(90)
J.forward(160)
J.lt(90)
J.fd(145)
J.lt(90)
J.forward(150)
J.rt(90)
J.fd(180)

J.rt(90)
J.fd(320)
J.rt(90)
J.fd(75)
J.lt(90)
J.fd(20)
J.lt(90)
J.fd(75)
J.rt(90)
J.fd(340)

J.rt(90)
J.fd(180)
J.rt(90)
J.forward(150)
J.lt(90)
J.fd(145)
J.lt(90)
J.forward(160)


def Up():
    A.setheading(90)
    A.fd(10)
def Down():
    A.setheading(270)
    A.fd(10)
def Left():
    A.setheading(180)
    A.fd(10)
def Right():
    A.setheading(0)
    A.fd(10)



wn = trtl.Screen()
wn.bgcolor("black")
wn.onkeypress(Right, "Right")
wn.onkeypress(Left, "Left")
wn.onkeypress(Up, "Up")
wn.onkeypress(Down, "Down")
wn.listen()
wn.mainloop()