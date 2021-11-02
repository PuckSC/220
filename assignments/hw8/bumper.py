"""
Name: Patrick Puckhaber
bumper.py

Problem: bumper car simulator

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
from random import randint
from graphics import Circle, Point, GraphWin, update, color_rgb


def hit_vertical(car_x, graph):
    car = car_x.getCenter()
    return car.getX() <= car_x.getRadius() or car.getX() >= graph.getWidth() - car_x.getRadius()


def hit_horizontal(car_y, graph):
    car = car_y.getCenter()
    return car.getY() <= car_y.getRadius() or car.getY() >= graph.getHeight() - car_y.getRadius()


def did_collide(car1, car2):
    car1_pos = car1.getCenter()
    car2_pos = car2.getCenter()
    distance = math.sqrt((car1_pos.getX() - car2_pos.getX()) ** 2 +
                         (car1_pos.getY() - car2_pos.getY()) ** 2)
    return distance <= car1.getRadius() + car2.getRadius()


def random_color():
    color = color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    return color


def get_random(given):
    rand_num = randint((int(given) * -1), int(given))
    return rand_num


def main():
    # window
    height = 400
    width = 600
    window = GraphWin("Bumper", 600, 400, autoflush=False)
    # "Cars" with single point radius adjustment
    rad = 30
    point_1 = Point(randint(rad + 2, int(width / 2)),
                         randint(rad + 2, (height - (rad + 2))))
    point_2 = Point(randint(int(width / 2), (width - (rad + 2))),
                         randint(rad + 2, (height - (rad + 2))))
    car_a = Circle(point_1, rad)
    car_b = Circle(point_2, rad)
    car_a.setFill(random_color())
    car_b.setFill(random_color())
    car_a.draw(window)
    car_b.draw(window)
    # random start directions scaled to window
    ran_x1 = randint(int(width / 2), width) / (width * .2)
    ran_y1 = randint(int(height / 2), height) / (height * .2)
    ran_x2 = randint(int(width / 2), width) / (width * .2)
    ran_y2 = randint(int(height / 2), height) / (height * .2)

    while True:
        update(40)
        # car movement
        car_a.move(ran_x1, ran_y1)
        car_b.move(ran_x2, ran_y2)
        # car position update
        # car_1 = car_a.getCenter()
        # car_2 = car_b.getCenter()

        # Wall collision
        if hit_vertical(car_a, window):
            ran_x1 = ran_x1 * (-1)
        if hit_horizontal(car_a, window):
            ran_y1 = ran_y1 * (-1)
        if hit_vertical(car_b, window):
            ran_x2 = ran_x2 * (-1)
        if hit_horizontal(car_b, window):
            ran_y2 = ran_y2 * (-1)
        # Car collision response
        if did_collide(car_a, car_b):
            if ran_y2 > 0 and ran_y1 > 0 or ran_y1 < 0 and ran_y2 < 0:
                ran_x1 = ran_x1 * (-1)
                ran_x2 = ran_x2 * (-1)
            elif ran_y2 > 0 > ran_y1 or ran_y1 > 0 > ran_y2:
                ran_x1 = ran_x1 * (-1)
                ran_x2 = ran_x2 * (-1)
                ran_y1 = ran_y1 * (-1)
                ran_y2 = ran_y2 * (-1)


if __name__ == "__main__":
    main()
