import random
from turtle import Turtle

tim = Turtle()

colors = ["DeepSkyBlue4", "LightSteelBlue", "CornflowerBlue", "RoyalBlue", "Blue", "MediumBlue", "Navy", "DarkBlue"]

def change_direction():
     direction = [0, 90, 180, 270]
     tim.right(random.choice(direction))


while True:
    tim.width(10)
    tim.forward(20)
    change_direction()
    tim.color(random.choice(colors))


