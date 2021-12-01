"""
Name: Patrick Puckhaber
lab13.py
"""

from graphics import Rectangle, Point


def is_in_binary(search_val, values):
    mid = values[len(values) // 2]
    while mid != search_val and len(values) != 1:
        if mid > search_val:
            values = values[:len(values) // 2]
        else:
            values = values[(len(values) // 2) + 1:]
        mid = values[len(values) // 2]
    if mid == search_val:
        return True
    else:
        return False


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i, len(values)):
            if values[j] < lowest:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]


def rect_sort(values):
    d = {}
    areas = []
    for rect in values:
        d[get_area(rect)] = rect
        areas.append(get_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        values[i] = d[areas[i]]
    print(areas)


def get_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    w = abs(p1.getX() - p2.getX())
    h = abs(p1.getY() - p2.getY())
    return w * h


def trade_alert(filename):
    infile = open(filename, "r")
    data = infile.read().split()
    for i in range(len(data)):
        if int(data[i]) > 830:
            print(i + 1, "ALERT!")
        if 830 >= int(data[i]) >= 500:
            print(i + 1, "Warning")


def main():
    x = [3, 4, 1, 6]
    rect = [Rectangle(Point(0,0), Point(20,20))]
    print(is_in_binary(1, [1, 2, 3, 4]))

    selection_sort(x)
    print(x)
    rect_sort(rect)
    print(rect)
    trade_alert("trades.txt")
    pass


main()
