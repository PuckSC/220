"""
Name: Patrick Puckhaber
lab2.py

Problem: The second set of lab assignments
"""


import math


def sum_of_threes():

    upper = eval(input("Define upper bound: "))
    acc = 0
    for i in range(0, upper + 1, 3):
        acc = acc + i
    print(acc)


def multiplication_table():

    for H in range(1, 11):
        for L in range(1, 11):
            print(H * L, end=" ")
        print()


def triangle_area():
    a = eval(input("Enter Side A: "))
    b = eval(input("Enter Side B: "))
    c = eval(input("Enter Side C: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(area)


def sumSquares():
    lower = eval(input("Enter the bottom of range: "))
    upper = eval(input("Enter the top of range: "))
    acc = 0
    for i in range(lower, upper + 1):
        acc += (i ** 2)
    print(acc)


def power():
    base = eval(input("Base?: "))
    exp = eval(input("Exponent?: "))
    acc = 1
    for i in range(exp):
        acc *= base
    print(acc)
