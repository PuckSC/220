"""
Name: Patrick Puckhaber
greeting.py

Problem: A program that displays a heart and stuff. Lets user fire three arrows from any position,
miss 3 times then message...

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from random import random

from graphics import GraphWin, Point, Circle, Polygon, Line, Text, update


def main():
    window = GraphWin("Greeting Card", 500, 500, autoflush=False)
    window.setCoords(0, 0, 10, 10)

    # Crit Points
    pt_a = Point(4, 6)
    pt_b = Point(6, 6)

    # the heart
    circle1 = Circle(pt_a, 1.22)
    circle2 = Circle(pt_b, 1.22)
    circle1.setFill("red")
    circle1.setOutline("red")
    circle2.setFill("red")
    circle2.setOutline("red")
    triangle = Polygon(Point(2.875, 5.52), Point(7.125, 5.52), Point(5, 2.9))
    triangle.setFill("red")
    triangle.setOutline("red")
    point1 = Point(4.75, 5.25)
    point2 = Point(5.25, 5.25)
    line3 = Line(Point(5, 4.75), Point(4.6, 4.65))
    line4 = Line(Point(5, 4.75), Point(5.4, 4.65))
    circle3 = Circle(Point(5, 5), .8)
    circle3.draw(window)
    point1.draw(window)
    point2.draw(window)
    line3.draw(window)
    line4.draw(window)
    circle1.draw(window)
    circle2.draw(window)
    triangle.draw(window)

    greeting = Point(5, 9)
    greet = Text(greeting, "Happy Valentine's Day!")
    greet.setFace("arial")
    greet.setSize(20)
    greet.setStyle("bold")
    greet.draw(window)

    firepoint = Point(5, 1)
    fire = Text(firepoint, "Click mouse to fire arrows!")
    fire.draw(window)

    # the arrow
    for i in range(3):
        org = window.getMouse()
        vec_org = Point(org.getX(), org.getY())
        vector = Point(((5 - org.getX()) / abs(5 - org.getX()) * (5 / (5 - abs(5 -
                        org.getX()))) + org.getX()),
                       ((5 - org.getY()) / abs(5 - org.getY()) * (5 / (5 - abs(5 -
                        org.getY()))) + org.getY()))
        arrow = Line(vec_org, vector)
        arrow.setArrow("last")
        arrow.draw(window)

        for m in range(8):
            update(8)
            arrow.move((5 - org.getX())/10, (5 - org.getY())/10)
        arrow.undraw()

    fire.undraw()

    for i in range(17):
        update(7)
        circle1.move(-(random()) ** (1 / (i + 1)), random() ** (1 / (i + 1)))
        circle2.move(random() ** (1 / (i + 1)), random() ** (1 / (i + 1)))
        triangle.move(0, -.5)
        greet.move(0, 1)

    luck = Text(Point(5, 6.5), "Better Luck Next Year")
    luck.setFace("helvetica")
    luck.setSize(14)
    luck.setStyle("bold")
    for i in range(8):
        update(6)
        luck.setTextColor("red")
        luck.draw(window)
        update(6)
        luck.undraw()
        luck.setTextColor("black")
        luck.draw(window)
        update(6)
        luck.undraw()
    luck.draw(window)

    close = Text(firepoint, "Click anywhere to Close")
    close.draw(window)

    window.getMouse()
    window.close()


if __name__ == "__main__":
    main()
