"""
Name: Patrick Puckhaber
mean.py

Problem: Computes the root mean square Average, the Harmonic Mean, and the Geometric Mean.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
I referenced Ch. 11's code from the book (pg. 370-374)
"""

import math


def user_inputs():
    dataset = eval(input("Enter the number values in dataset: "))
    nums = []
    for val in range(dataset):
        val = eval(input("Enter value #" + str(val + 1) + ":"))
        list_values = float(val)
        nums.append(list_values)
    return nums


def rmsaverage(nums):
    total = 0.0
    for num in nums:
        total = total + num ** 2
    return math.sqrt(total / len(nums))


def hmean(nums):
    total = 0
    for num in nums:
        total = total + 1 / num
    return len(nums) / total


def geomean(nums):
    return math.prod(nums) ** (1 / len(nums))


def main():
    data = user_inputs()
    print(round(rmsaverage(data), 3))
    print(round(hmean(data), 3))
    print(round(geomean(data), 3))


if __name__ == "__main__":
    main()
