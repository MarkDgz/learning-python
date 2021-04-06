import turtle

window = turtle.Screen()
turtle.speed(5)
turtle.pensize(5)

turtle.penup()
turtle.goto(-350, 100)
turtle.pendown()
turtle.color("black")

# Drawing the outline of a square
turtle.fillcolor("white")
turtle.begin_fill()
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.penup()
turtle.end_fill()

#Draw the outline of a square in loop
turtle.goto(-175, 100)
turtle.color("magenta")
turtle.pendown()
for i in range(4): 
    turtle.forward(150)
    turtle.left(90)
turtle.penup()

# Multi-Color Stroke 
turtle.goto(0, 100)
turtle.pendown()
for colours in ["yellow","red","purple","blue"]:
    turtle.color(colours)
    turtle.forward(150)
    turtle.left(90)
turtle.penup()

# Filled Square with Stroke
turtle.goto(175, 100)
turtle.color("orange","yellow")
turtle.pendown()
turtle.begin_fill()

for i in range(4): 
    turtle.forward(150)
    turtle.left(90)
turtle.end_fill()
turtle.penup()

# Drawing a Triangle
turtle.goto(-350, -200)
window = turtle.Screen()
turtle.bgcolor("gray")
turtle.fillcolor("khaki")
turtle.begin_fill()
turtle.pendown()

for i in range(3):
    turtle.forward(300)
    turtle.left(120)
turtle.end_fill()
turtle.penup()

# Drawing a Circle
turtle.goto(175, -200)
turtle.pendown()
window = turtle.Screen()
turtle.bgcolor("darkkhaki") # changing background color of the window
turtle.color("navy", "violet") # stroke, fill colours
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.penup()

window.exitonclick()


