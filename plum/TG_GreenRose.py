import turtle
turtle.Pen()
p = turtle
p.speed(0)
p.color("green")
p.width(5)
for i in range(100):
    p.forward(i*2)
    p.circle(i*2, 90)
    p.right(20)
