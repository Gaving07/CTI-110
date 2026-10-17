# Your Name: Gavin Guy
# Date: 10/17/2026
# Assignment Name: Turtle House
# Description: Draws a house using a square and a triangle.

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("My Turtle House")

# Create the turtle
t = turtle.Turtle()
t.color("darkgreen")
t.pensize(4)
t.speed(3)

# Draw the square using a while loop
i = 0
while i < 4:
    t.forward(150)
    t.left(90)
    i += 1

# Move to the top of the square
t.left(90)
t.forward(150)
t.right(90)

# Draw the triangle roof using a for loop
for i in range(3):
    t.forward(150)
    t.left(120)

# Hide the turtle when finished
t.hideturtle()

# Keep the window open
turtle.done()