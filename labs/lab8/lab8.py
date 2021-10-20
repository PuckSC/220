"""
Name: Patrick Puckhaber
lab8.py
"""

from encoder import encode_better


def number_words(in_file_name, out_file_name):
    file_in = open(in_file_name, "r")
    file_out = open(out_file_name, "w")
    i = 1
    for line in file_in:
        new_line = line.split()
        for word in new_line:
            file_out.write(str(i) + " " + word + "\n")
            i += 1

    file_in.close()
    file_out.close()


def hourly_wages(in_file_name, out_file_name):
    file_in = open(in_file_name, "r")
    file_out = open(out_file_name, "w")
    for line in file_in:
        new_line = line.split(" ")
        new_line[2] = str(float(new_line[2]) + 1.65)
        file_out.write(" ".join(new_line) + "\n")

    file_in.close()
    file_out.close()


def calc_check_sum(isbn):
    check_sum = 0
    isbn = str(isbn)
    for i in range(len(isbn)):
        num = int(isbn[i]) * (10 - i)
        check_sum = check_sum + num
    return check_sum % 11


def send_message(file, friend):
    file_in = open(file, "r")
    file_out = open(friend + ".txt", "w")
    for line in file_in:
        file_out.write(line + "\n")

    file_in.close()
    file_out.close()


def send_safe_message(file, friend, key):
    file_in = open(file, "r")
    file_out = open(friend + ".txt", "w+")
    for line in file_in:
        new_line = encode(line, key)
        file_out.write(new_line + "\n")
    file_in.close()
    file_out.close()


def encode(message, shift):
    acc = ""
    for c in message:
        # entry code
        ec = ord(c)
        # shift code
        sc = ec + shift
        ac = chr(sc)
        acc = acc + ac
    return acc


def send_uncrackable_message(file, friend, pad):
    file_in = open(file, "r")
    file_out = open(friend + ".txt", "w")
    for line in file_in:
        new_line = encode_better(line, pad)
        file_out.write(new_line + "\n")
    file_in.close()
    file_out.close()


def main():
    # add other function calls here
    number_words("text_file.txt", "word_file.txt")
    hourly_wages("employees.txt", "hourly_wages.txt")
    calc_check_sum("0072946520")
    send_message("message.txt", "bob")
    send_safe_message("message.txt", "mike", 10)
    send_uncrackable_message("message.txt", "aaron", "pad_file")
    pass


main()
