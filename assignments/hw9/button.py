"""
Name: Patrick Puckhaber
threeDoorGame.py

Problem: a game with three doors...

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Text, Point


class Button:
    """
    Creates a class for the buttons along with the text label. Includes
    methods change color, click detection, undraw, and relabel
    """
    def __init__(self, shape, text):
        self.shape = shape
        p_1 = self.shape.getP1()
        self.text = Text(Point(p_1.getX() + 2.5, p_1.getY() + 2), text)

    def get_label(self):
        return self.text.getText()

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        p_1 = self.shape.getP1()
        p_2 = self.shape.getP2()
        return p_1.getX() <= point.getX() <= p_2.getX() and p_1.getY() <= point.getY() <= p_2.getY()

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text.setText(label)
