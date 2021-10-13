"""
Name: Patrick Puckhaber
Partner: <your partner's name goes here – first and last>
lab7.py
"""
import math


def cash_conversion():
    user_entry = eval(input("Enter Value: "))
    print("$", "{:.2f}".format(user_entry))


def encode():
    acc = ""
    entry = input("Enter the word to be encoded: ")
    key = eval(input("Enter the key: "))
    for c in entry:
        # entry code
        ec = ord(c)
        # shift code
        sc = ec + key
        ac = chr(sc)
        acc = acc + ac
    print(acc)


def sphere_area(radius):
    surface_area = 4 * math.pi * radius ** 2
    return surface_area


def sphere_volume(radius):
    volume = (4 / 3) * math.pi * radius ** 3
    return volume


def sum_n(n):
    acc = 0
    for i in range(n):
        acc = acc + i
    return acc


def sum_cubes(n):
    acc = 0
    for i in range(n):
        acc = acc + i ** 3
    return acc


def encode_better():
    # message and keyword modifications
    message = input("Word to be Encoded:")
    keyword = input("Enter Keyword: ")
    mess = message.replace(' ', '')
    key_word = keyword.replace(' ', '')
    # repeating then fixing length of key
    key_factor = len(mess) // len(key_word) + 1
    key_seq = key_word * key_factor
    key_code = key_seq[:len(mess)]
    # key maker
    key_list = []
    for ltr in key_code.upper():
        unicode = ord(ltr)
        key_list.append(unicode)
    # message to unicode to re-indexed to A = 0
    mess_code = []
    for ltr in mess.upper():
        unicode = ord(ltr)
        mess_code.append(unicode)
    # output section
    output = []
    for num in range(len(mess_code)):
        keycode = ((mess_code[num] + key_list[num]) + 26) % 26
        keycode = keycode + ord('A')
        output.append(chr(keycode))
    result = ''.join(output)
    print(result)


def main():
    # add function calls here
    # cash_conversion()
    # encode()
    # print(sphere_volume(3))
    # print(sphere_area(2))
    # print(sum_n(5))
    # print(sum_cubes(7))
    encode_better()
    pass


main()
