from turtle import *
import colorsys

bgcolor("black")
tracer(500)

def draw():
    h = 0
    for i in range(100):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        h += 0.8
        up()
        goto(0, 0)
        down()
        color("indigo")
        fillcolor(c)
        begin_fill()
        rt(98)
        circle(i, 120)
        fd(280)
        fd(i)
        lt(29)
        for j in range(129):
            fd(i)
            circle(j, 988/3, steps=3)  # Corrected the third argument in circle function
        end_fill()  # Added parentheses for end_fill function call

draw()
