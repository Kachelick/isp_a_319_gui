from tkinter import *


def move():
    x = canvas.coords(ball)[2]
    y = canvas.coords(ball)[3]
    if (canvas.x == x) and (canvas.y == y):
        return
    if (canvas.x < x):
        canvas.move(ball, -1, 0)
    if (canvas.x > x):
        canvas.move(ball, 1, 0)
    if (canvas.y < y):
        canvas.move(ball, 0, -1)
    if (canvas.y > y):
        canvas.move(ball, 0, 1)
    root.after(5, move)


def move_oval(event):
    canvas.x = event.x + canvas.radius
    canvas.y = event.y + canvas.radius
    move()


root = Tk()

canvas = Canvas(width=200, height=200)
canvas.pack()

canvas.radius = 25
ball = canvas.create_oval(140, 140, 160, 160,
                     fill='green')
canvas.bind("<Button-1>", move_oval)

root.mainloop()
