import os

try:
    from tkinter import *
    from turtle import Turtle
except:
    os.system("python -m pip install tk")
    os.system("python -m pip install PythonTurtle")
pencil = Turtle()


def curve():
    for i in range(200):
        pencil.right(1)
        pencil.forward(1)


def mainpart():
    pencil.fillcolor("red")
    pencil.begin_fill()
    pencil.left(140)
    pencil.forward(115)
    curve()
    pencil.left(120)
    curve()
    pencil.forward(115)
    pencil.end_fill()


def filltxt():

    pencil.up()
    pencil.setpos(-95, 95)
    pencil.color("black")
    pencil.write("Try out flames as well ;) ", font=("Arial", 13, ""))
    pencil.setpos(-65, 75)
    pencil.write("Crush be like - 'Awww '", font=("Arial", 10, ""))
    # pencil.write("Idea credits - Apoorva SJ", font = ("Arial",7, ""))
    pencil.down()


def arrow():
    pencil.color("red")
    pencil.goto(0, 100)
    pencil.color("black")
    pencil.shape("arrow")
    pencil.up()
    pencil.forward(150)
    pencil.tilt(180)
    pencil.stamp()
    pencil.down()
    pencil.backward(75)
    pencil.up()
    pencil.backward(75)
    pencil.down()
    pencil.backward(150)


mainpart()
filltxt()
arrow()
