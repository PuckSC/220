"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from graphics import *
import math


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target
    z = win_width
    p = Point(win_width / 2, win_height / 2)
    circle5 = Circle(p, z/2)
    circle4 = Circle(p, z/2.5)
    circle3 = Circle(p, z/3.5)
    circle2 = Circle(p, z/5.5)
    circle1 = Circle(p, z/10)

    circle5.setFill("white")
    circle4.setFill("black")
    circle3.setFill("blue")
    circle2.setFill("red")
    circle1.setFill("yellow")

    circle5.draw(win)
    circle4.draw(win)
    circle3.draw(win)
    circle2.draw(win)
    circle1.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.
    p = win.getMouse()
    q = win.getMouse()
    r = win.getMouse()
    len1 = math.sqrt(abs((q.getX() ** 2) - (p.getX() ** 2)) + ((q.getY() ** 2) - (p.getY() ** 2)))
    len2 = math.sqrt(abs((r.getX() ** 2) - (p.getX() ** 2)) + ((r.getY() ** 2) - (p.getY() ** 2)))
    len3 = math.sqrt(abs((r.getX() ** 2) - (q.getX() ** 2)) + ((r.getY() ** 2) - (q.getY() ** 2)))
    r_shape = Polygon(p, q, r)
    r_shape.draw(win)
    peri = len1 + len2 + len3
    s = peri / 2
    area = math.sqrt(s * (s - len1) * (s - len2) * (s - len3))

    inst_pt = Point(win_width / 2, win_height - 10)
    instructions = Text(inst_pt, "The area is: " + str(area))
    instructions.draw(win)

    peript = Point(win_width / 2, win_height - 25)
    perimeter = Text(peript, "The perimeter is: " + str(peri))
    perimeter.draw(win)

    exit_point = Point(win_width / 2, 20)
    close = Text(exit_point, "Click to Close Window")
    close.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)
    # WRITE EVERYTHING HERE
    red_box = Entry(Point(win_width / 2 + 50, win_height / 2 + 40), 5)
    green_box = Entry(Point(win_width / 2 + 50, win_height / 2 + 70), 5)
    blue_box = Entry(Point(win_width / 2 + 50, win_height / 2 + 100), 5)

    red_box.draw(win)
    green_box.draw(win)
    blue_box.draw(win)

    for i in range(5):
        win.getMouse()
        r = int(red_box.getText())
        g = int(green_box.getText())
        b = int(blue_box.getText())
        color = color_rgb(r, g, b)
        shape.setFill(color)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    s = input("Enter string: ")
    print(s[0])
    print(s[-1])
    print(s[1:6])
    print(s[0] + s[-1])
    print(s[:3] * 3)
    for c in s:
        print(c)
    print(len(s))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1]+values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1]
    print(x * 5)
    x = values[2:5]
    print(x)
    x = values[2], values[3], values[0]
    print(x)
    x = values[0], values[2], float(values[5])
    print(x)
    x = values[0] + values[2] + float(values[5])
    print(x)
    x = len(values)
    print(x)


def another_sequence():
    n = eval(input("Enter the numbers of terms in the sequence: "))
    acc = 0
    for i in range(n):
        y = 2 + 2 * (i % 3)
        acc = acc + y
        print(y, end=" ")
    print()
    print(acc)


def main():
    target()
    # triangle()
    # color_shape()
    # process_string()
    # process_list()
    # another_sequence()
    # pass


main()
