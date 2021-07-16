import turtle
turtle.Pen()
r = turtle
r.speed(0)
r.color("red")
r.width(4)
for i in range(100):
    r.circle(i*3, 100)
    r.right(45)

