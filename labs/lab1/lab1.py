"""
Name: Patrick Puckhaber
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    total = eval(input("Enter total number of shots: "))
    shots_made = eval(input("Enter shots made: "))
    shooting_percentage = shots_made / total * 100
    print("Shooting Percentage =", shooting_percentage, "%")


def coffee():
    coffee = eval(input("Enter number of pounds of coffee purchased: "))
    total = (coffee * 10.5) + (coffee * 0.86) + 1.5
    print("Total Cost =", "$", total)


def kilometers_to_miles():
    kilometers = eval(input("Enter the number of Kilometers: "))
    miles = kilometers / 1.61
    print("Distance in Miles = ", miles)
