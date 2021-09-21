"""
Name: Patrick Puckhaber
traffic.py

Problem: A program that will help them analyze traffic patterns

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    num_roads = eval(input("Enter # of Roads Surveyed"))
    total = 0
    for i in range(num_roads):
        cars = 0
        days = eval(input("Enter # of Days Road " + str(i + 1) + " was surveyed: "))
        for j in range(days):
            count = eval(input("Enter # of cars observed on day " + str(j + 1) + ": "))
            cars = count + cars
            total = total + count
        print("Road", (i + 1), "average vehicles per day:", round(cars / days, 2))
    print("Total number of Vehicles per day: ", total)
    print("Average number of Vehicles per road: ", round(total / num_roads, 2))


if __name__ == "__main__":
    main()
