from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()

def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.backward(20)

def slant_right():
    tim.circle(-100, 10)

def slant_left():
    tim.circle(100, 10)

def clear_screen():
    tim.clear()

screen.listen()
screen.onkey(key="w",  fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=slant_left)
screen.onkey(key="d", fun=slant_right)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()