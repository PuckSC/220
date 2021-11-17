"""
Name: Patrick Puckhaber
weighted_average.py

Problem: Takes data from a file, computes averages, and outputs to a different file

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


# take inputs from file; fname, lname, w1, g1, etc
def ind_avg(s_data):

    # data groom
    data_prime = s_data.split(": ")
    datum = data_prime[1].split(" ")
    data = []
    for i in datum:
        point = float(i)
        data.append(point)
    weight = data[0::2]
    grade = data[1::2]

    # storage assets
    name = data_prime[0]
    stu_avg = 0
    err = 0
    w_total = 0

    # weight total for error processing; 0 is no error; 1 is error high, 2 error low
    for val in weight:
        w_total = val + w_total
        if w_total > 100:
            err = 1
        if w_total < 100:
            err = 2
        if w_total == 100:
            err = 0
    # properly weighted grades are returned
    if err == 0:
        for i in range(len(grade)):
            total = grade[i] * weight[i]
            stu_avg = total / 100 + stu_avg
    return err, stu_avg, name


def weighted_average(file_in, file_out):
    input_file = open(file_in, "r")
    output_file = open(file_out, "w")
    line = input_file.readlines()
    # class average list for calculation
    class_list = []
    # line by line loop
    for student in line:
        err, avg, stu_name = ind_avg(student)
        # error outputs
        if err == 2:
            print(stu_name + "'s average: Error: The weights are less than 100.", file=output_file)
        if err == 1:
            print(stu_name + "'s average: Error: The weights are more than 100.", file=output_file)
        # grades with no weighting error are printed and added to class avg counter
        if err == 0:
            print(stu_name + "'s average:", round(avg, 1), file=output_file)
            class_list.append(avg)
    print("Class average:", round(sum(class_list) / len(class_list), 1), file=output_file)
    # close up files
    input_file.close()
    output_file.close()


def main():
    weighted_average("grades.txt", "avg.txt")


if __name__ == "__main__":
    main()
