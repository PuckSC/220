"""
Name: Patrick Puckhaber
lab9.py
"""

from graphics import *
import math


def addTens(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squaresEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc = acc + nums[i]
    return acc


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])


def writeSumOfSquares():
    ifn = input("Enter the Name of the input file: ")
    infile = open(ifn, "r")
    outfile = open("SoS.txt", "w")
    for line in infile:
        data = line.split(" ")
        toNumbers(data)
        squaresEach(data)
        total = sumList(data)
        print("Sum of Squares = ", total, file=outfile)
    infile.close()
    outfile.close()


def starter():
    weight = eval(input("Enter weight: "))
    numWins = eval(input("Enter number of wins"))
    if 150 <= weight < 160 and numWins > 5:
        print("Player should start")

    elif weight > 199 or numWins > 20:
        print("Player should start")
    else:
        print("Player should not start")


def leapYear(year):
    entered = year
    if entered % 4 == 0 and (entered % 100 != 0 or entered % 400 == 0):
        print(entered, "is a leap year")
    else:
        print(entered, "is not a leap year")


def circleOverlap():
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    p = win.getMouse()
    q = win.getMouse()
    d = math.sqrt((q.getX() - p.getX()) ** 2 + (q.getY() - p.getY()) ** 2)
    r_shape = Circle(p, d)
    r_shape.draw(win)

    p1 = win.getMouse()
    q1 = win.getMouse()
    d1 = math.sqrt((q1.getX() - p1.getX()) ** 2 + (q1.getY() - p1.getY()) ** 2)
    r_shape2 = Circle(p1, d1)
    r_shape2.draw(win)

    d2 = math.sqrt((p1.getX() - p.getX()) ** 2 + (p.getY() - p1.getY()) ** 2)
    ovr_pt1 = Point(width / 2, height - 20)
    if d2 < d + d1:

        overlap_txt = Text(ovr_pt1, "Circles Overlap")
        overlap_txt.draw(win)
    else:

        overlap_null = Text(ovr_pt1, "Circles DO NOT Overlap")
        overlap_null.draw(win)

    exit_point = Point(width / 2, 20)
    close = Text(exit_point, "Click to Close Window")
    close.draw(win)

    win.getMouse()
    win.close()


def main():
    # addTens([5,2,-3])
    # sumList([5,2,-3])
    # toNumbers([5,2,-3])
    # writeSumOfSquares()
    # starter()
    # leapYear(2100)
    # circleOverlap()
    # add other function calls here
    pass


main()
