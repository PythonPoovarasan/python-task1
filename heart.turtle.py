import turtle
turtle.speed(3)
turtle.bgcolor("black")#backgroundcolor
turtle.pensize(100)
def fun():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.color("blue","blue")#heartouter and inner color
turtle.begin_fill()
turtle.left(140)
turtle.forward(119.65)
fun()
turtle.left(120)
fun()
turtle.forward(119.65)
turtle.end_fill()
turtle.hideturtle()
turtle.done()
        
