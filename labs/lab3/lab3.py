"""
Name: Patrick Puckhaber
lab3.py

Problem: The Third set of lab assignments
"""


def average():

    n = eval(input("Enter the Number of Grades to Input"))
    total = 0
    for i in range(n):
        i = eval(input("Enter Grade for HW" + str(i + 1)))
        total = total + i
    avg = total / n
    print("Your average grade:", avg)


def tip_jar():
    acc = 0
    for i in range(5):
        i = eval(input("Enter Donation Amount: "))
        acc = acc + i
    print("Total Donations:", acc)


def newton():
    # ask user for number and how many times to improve the approx, refines are how many times to loop
    x = eval(input("Enter integer to square root: "))
    n = eval(input("Enter the number of times to refine: "))
    approx = x / 2
    for i in range(n):
        approx = (approx + (x / approx))/2

    print("The Square Root of", approx)


def sequence():
    x = eval(input("What is the number of terms in the series?: "))
    for i in range(1, x + 1):
        print(1 + (i // 2 * 2))


def pi():
    # num 2+(x//2*2) and denom 1+ (x+1)//2*2 variables, then make fraction; acc (frac*acc), print acc*2
    n = eval(input("Enter number of terms in the series:"))
    acc = 1
    for i in range(n):
        num = 2 + (i // 2 * 2)
        denom = 1 + ((i + 1) // 2 * 2)
        acc = acc * (num / denom)
    print(acc * 2)
