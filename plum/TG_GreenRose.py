import turtle
turtle.Pen()
sam = turtle
sam.speed(0)
sam.color("green")
sam.width(5)
for i in range(100):
    sam.forward(i*2)
    sam.circle(i*2, 90)
    sam.right(20)
