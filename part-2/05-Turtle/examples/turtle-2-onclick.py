import turtle

names = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']

def square(x, y):
    print(int(x), int(y))
    alex.pendown()
    for _ in range(4):
        alex.forward(step)
        alex.right(90)
    alex.penup()


w = turtle.Screen()
w.bgcolor("lightgreen")

alex = turtle.Turtle()
pos_name = 4
alex.shape(names[pos_name])

alex.color("#4400AA")
alex.speed(1)
alex.pensize(3)

step = 150
turtle.onscreenclick(square, 1)

w.mainloop()
