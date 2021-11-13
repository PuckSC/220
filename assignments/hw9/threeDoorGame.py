"""
Name: Patrick Puckhaber
threeDoorGame.py

Problem: a game with three doors...

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from button import Button
from graphics import *
from random import randint


def main():
    win = GraphWin("Three Button Game", 600, 400)
    win.setCoords(0, 0, 30, 20)

    # button 1
    pos_1a, pos_1b = Point(5, 8), Point(10, 12)
    btn_1 = Button(Rectangle(pos_1a, pos_1b), Text(Point(7.5, 10), "Door 1"))
    btn_1.draw(win)

    # button 2
    pos_2a, pos_2b = Point(12.5, 8), Point(17.5, 12)
    btn_2 = Button(Rectangle(pos_2a, pos_2b), Text(Point(15, 10), "Door 2"))
    btn_2.draw(win)

    # button 3
    pos_3a, pos_3b = Point(20, 8), Point(25, 12)
    btn_3 = Button(Rectangle(pos_3a, pos_3b), Text(Point(22.5, 10), "Door 3"))
    btn_3.draw(win)

    # Top text
    t_text = Text(Point(15, 17), "Only one door is a winner!")
    t_text.draw(win)

    # bottom text
    b_text = Text(Point(15, 2), "Click to choose a door")
    b_text.draw(win)

    rand_door = randint(1, 3)

    # button game
    while True:
        door_click = win.getMouse()
        cond = 0
        if btn_1.is_clicked(door_click):
            if rand_door == 1:
                btn_1.color_button("green")
                cond = 1
            else:
                btn_1.color_button("red")
                cond = 2

        if btn_2.is_clicked(door_click):
            if rand_door == 2:
                btn_2.color_button("green")
                cond = 1
            else:
                btn_2.color_button("red")
                cond = 2

        if btn_3.is_clicked(door_click):
            if rand_door == 3:
                btn_3.color_button("green")
                cond = 1
            else:
                btn_3.color_button("red")
                cond = 2

        if cond == 1:
            t_text.setText("You Win!")
            b_text.setText("Click to close")
            win.getMouse()
            break
        if cond == 2:
            t_text.setText("You Lose!")
            b_text.setText("Door {0} was the winner, click to close".format(rand_door))
            win.getMouse()
            break
    win.close()


main()
