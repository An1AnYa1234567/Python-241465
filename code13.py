# Write a program to demonstrate  Interactive Turtle Pattern Generator and Fractal Renderer.
import turtle

# Configure screen
screen = turtle.Screen()
screen.title("Koch Snowflake Fractal")
screen.setup(width=800, height=700)
screen.bgcolor("#101820")
screen.colormode(255)

# Configure turtle pen
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.color(255, 105, 180)

# Hide turtle and disable animation
pen.hideturtle()
screen.tracer(0, 0)

# Recursive Koch curve
def koch(length, depth):
    if depth == 0:
        pen.forward(length)
    else:
        koch(length / 3, depth - 1)
        pen.left(60)
        koch(length / 3, depth - 1)
        pen.right(120)
        koch(length / 3, depth - 1)
        pen.left(60)
        koch(length / 3, depth - 1)

# Draw snowflake
pen.penup()
pen.goto(-200, 120)
pen.pendown()

for i in range(3):
    koch(400, 3)
    pen.right(120)

# Update drawing
screen.update()

# Keep window open
turtle.done()