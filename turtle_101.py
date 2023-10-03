import turtle

side_length = float(input("Enter side length of star:"))
turtle.showturtle()

def fourSidedStar(side_length):
    turtle.left(75)
    turtle.forward(side_length)
    turtle.right(60)
    turtle.forward(side_length)
    turtle.left(150)
    turtle.forward(side_length)
    turtle.right(60)
    turtle.forward(side_length)
    turtle.left(150)
    turtle.forward(side_length)
    turtle.right(60)
    turtle.forward(side_length)
    turtle.left(150)
    turtle.forward(side_length)
    turtle.right(60)
    turtle.forward(side_length)

fourSidedStar(side_length)

turtle.exitonclick()