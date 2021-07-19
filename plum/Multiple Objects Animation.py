
from tkinter import *
import random
import time

WIDTH = 800
HEIGHT = 600

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Bouncing Ball")
canvas.pack()

class Ball:
    def __init__(self, color, size):
        self.shape = canvas.create_oval(10, 10, size, size, fill=color)
        self.xspeed = random.randrange(1,8)
        self.yspeed = random.randrange(1, 8)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed

ball = Ball("red", 50)
ball2 = Ball("green", 100)
ball3 = Ball("orange", 76)
ball4 = Ball("purple", 150)
ball5 = Ball("pink", 165)
ball6 = Ball("blue", 180)
ball7 = Ball("yellow", 110)
ball8 = Ball("violet", 90)
ball9 = Ball("gold", 50)
ball10 = Ball("turquoise", 120)
ba = Ball("chocolate", 40)
ball12 = Ball("maroon", 190)

while True:
    ball.move()
    ball2.move()
    ball3.move()
    ball4.move()
    ball5.move()
    ball6.move()
    ball7.move()
    ball8.move()
    ball9.move()
    ball10.move()
    ba.move()
    ball12.move()
    tk.update()
    time.sleep(0.01)


tk.mainloop()