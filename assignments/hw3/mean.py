"""
Name: Patrick Puckhaber
mean.py

Problem: Computes the root mean square Average, the Harmonic Mean, and the Geometric Mean.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math


def main():
    dataset = eval(input("Enter number of values to be averaged: "))
    sum_inv = 0
    product = 1
    sum_sq = 0
    for values in range(dataset):
        values = eval(input("Enter Value: "))
        sum_inv += 1 / values
        product *= values
        sum_sq += values ** 2

    avg_rms = math.sqrt(sum_sq / dataset)
    print(round(avg_rms, 3))

    avg_h = dataset / sum_inv
    print(round(avg_h, 3))

    avg_g = product ** (1 / dataset)
    print(round(avg_g, 3))


if __name__ == "__main__":
    main()
