
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
        self.shape = canvas.create_rectangle(10, 10, size, size, fill=color)
        self.xspeed = random.randrange(-10,10)
        self.yspeed = random.randrange(-10, 10)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed
colors = ['red', 'green', 'blue', 'purple', 'orange', 'yellow', 'turquoise', 'grey', 'cyan', 'magenta', 'skyblue', 'dodgerblue', 'gold', 'pink', 'violet', 'lightgreen', 'maroon', 'darkred']
balls = []
for i in range(175):
    balls.append(Ball(random.choice(colors),random.randrange(50, 100)))

while True:
    for ball in balls:
        ball.move()
    tk.update()
    time.sleep(0.01)


tk.mainloop()