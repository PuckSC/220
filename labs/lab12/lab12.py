"""
Name: Patrick Puckhaber
Lab12.py
"""


from random import randint


def find_and_remove_first(lst, value):
    try:
        i = lst.index(value)
        lst[i] = "Patrick"

    except:
        pass


def read_data(filename):
    f = open(filename, "r")
    d = f.readlines()
    d[0].split(" ")
    i = 0
    while i < len(d):
        d[i] = int(d[i])
        i += 1
    return d


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if i == search_val:
            i += 1
            return True
    return False


def good_input():
    x = eval(input("Enter a number between 1-10: "))
    while 0 < x <= 10:
        x = eval(input("Not in range, make sure entry is in range:"))
    return x


def num_digits():
    x = eval((input("Enter a positive integer: ")))
    while x >= 1:
        m = 0
        while x > 0:
            m += 1
            x //= 10
        print(m)
        x = eval((input("Enter a positive integer: ")))


def hi_lo_game():
    number = randint(1, 100)
    counter = 0
    x = eval(input("Guess a number between 1-100: "))
    while x != number and counter < 7:
        if x > number and counter != 6:
            print("Too high!")
            x = eval(input("Guess a number between 1-100: "))
        elif x < number and counter != 6:
            print("Too low!")
            x = eval(input("Guess a number between 1-100: "))
        counter += 1
    if x == number:
        print("You win in {0} guesses!".format(counter))
    else:
        print("You lose. the number was {0}".format(number))

def main():
    # add other function calls here
    # find_and_remove_first(lst, value)
    # read_data(file)
    # is_in_linear(search_val, values)
    # good_input()
    # hi_lo_game()
    pass


main()
