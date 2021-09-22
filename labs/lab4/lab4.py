"""
Name: <your name goes here – first and last>
lab4.py
"""

from graphics import *
import math


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to add new square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the square
    for i in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)
        c = shape.getCenter()  # center of rectangle/square

        # move amount is distance from center of square to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)

    instructions.undraw()

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to Close Window")
    instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """

    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    p = win.getMouse()
    q = win.getMouse()
    len1 = abs(q.getX() - p.getX())
    wid = abs(q.getY() - p.getY())
    r_shape = Rectangle(p, q)
    r_shape.draw(win)
    area = len1 * wid
    peri = (2 * len1) + (2 * wid)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "The area is: " + str(area))
    instructions.draw(win)

    peript = Point(width / 2, height - 25)
    perimeter = Text(peript, "The perimeter is: " + str(peri))
    perimeter.draw(win)

    exit_point = Point(width / 2, 20)
    close = Text(exit_point, "Click to Close Window")
    close.draw(win)

    win.getMouse()
    win.close()


def circle():
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    p = win.getMouse()
    q = win.getMouse()
    d = math.sqrt((q.getX() - p.getX()) ** 2 + (q.getY() - p.getY()) ** 2)
    r_shape = Circle(p, d)
    r_shape.draw(win)

    radpt = Point(width / 2, height - 25)
    rad = Text(radpt, "The radius is: " + str(d))
    rad.draw(win)

    exit_point = Point(width / 2, 20)
    close = Text(exit_point, "Click to Close Window")
    close.draw(win)

    win.getMouse()
    win.close()


def pi2():
    n = eval(input("How terms are in the series?: "))
    acc = 0
    for i in range(n):
        num = 4
        denom = 1 + 2 * i
        frac = (num / denom) * ((-1)**i)
        acc = acc + frac
    print(acc)
    print("Difference from pi: ", math.pi - acc)


def main():
    squares()
    rectangle()
    circle()
    pi2()


main()
