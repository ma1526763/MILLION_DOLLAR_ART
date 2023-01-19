from turtle import Turtle, Screen
import random
tim = Turtle()
color_list = ["blue", "red", "green", "black", "yellow"]
tim.shape()
tim.penup()
tim.goto(-230, -230)
tim.hideturtle()
for _ in range(10):
    for _ in range(10):
        random_color = random.random(), random.random(), random.random()
        tim.pendown()
        tim.dot(30, random_color)
        tim.penup()
        tim.forward(50)
    tim.goto(-230, tim.ycor() + 50)
screen = Screen()
screen.exitonclick()
