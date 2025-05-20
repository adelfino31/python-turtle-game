import turtle
turtle.showturtle()
turtle.penup()
turtle.screensize(600, 600)
leftcornerx=79
leftcornery=54
targetsize=46
right=0
left=180
up=90
down=270
center=0
turtle.goto(leftcornerx, leftcornery)
turtle.pendown()
turtle.forward(targetsize)
turtle.setheading(up)
turtle.forward(targetsize)
turtle.setheading(left)
turtle.forward(targetsize)
turtle.setheading(down)
turtle.forward(targetsize)
turtle.penup()
turtle.goto(center, center)
turtle.setheading(right)
turtle.pendown()
force=int(input('Enter the amount of force you need to hit the target: '))
distance=int(input('Enter the distance you need to travel to hit the target: '))
while force<600 and distance<600:
    turtle.setheading(force)
    turtle.forward(distance)
    if (turtle.xcor() >= leftcornerx and
        turtle.xcor() <= (leftcornerx + targetsize) and
        turtle.ycor() >= leftcornery and
        turtle.ycor() <= (leftcornery + targetsize)):
        print('Target hit')
    else:
        turtle.goto(center,center)
        turtle.setheading(right)
        force=int(input('Enter the amount of force to play again: '))
        distance=int(input('Enter a distance to travel: '))
