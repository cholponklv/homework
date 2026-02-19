import turtle

side_length = float(input("Enter the side length of the hexagon in pixels: "))
t = turtle.Turtle()

for i in range(6):
    t.forward(side_length)
    t.left(60)

turtle.exitonclick()