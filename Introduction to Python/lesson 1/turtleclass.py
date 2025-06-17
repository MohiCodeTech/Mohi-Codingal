import turtle
pen = turtle.Turtle()
pen.speed(2)
pen.color("red")
pen.fillcolor("red")

# pen.begin_fill()

# for i in  range(3):
#     pen.forward(50)
#     pen.right(120)

# pen.end_fill()

# turtle.done()

#semicircle

# number_of_sides = 100
# side_lenth = 30

# for i in range(number_of_sides):
#     pen.forward(side_lenth)
#     pen.right(360 / number_of_sides)

# turtle.done()

#star
# for i in range(5):
#     pen.forward(150)
#     pen.right(144)

# turtle.done()

# pen.circle(100)
# turtle.done()

turtle.bgcolor("white")

for i in range(100):
    pen.forward(i * 2)
    pen.right(75)

turtle.done()