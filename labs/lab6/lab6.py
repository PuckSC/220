"""
Name: Patrick Puckhaber
lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("Enter first name then last name: ")
    fullname = name.split(" ")
    print(fullname[1] + ", " + fullname[0])


def company_name():
    web_site = input("Enter the Company Domain name: ")
    co_name = web_site.split(".")
    print(co_name[1])


def initials():
    class_size = eval(input("Enter the Number of Students in Class: "))
    for i in range(class_size):
        f_name = input("Enter Student's First Name: ")
        l_name = input("Enter " + f_name + "'s  Last Name: ")
        print(f_name + "'s Initials are: " + f_name[0] + l_name[0])


def names():
    clas_names = input("Enter list of names separated by a comma:")
    s_names = clas_names.split(",")
    print("The initials are: ")
    for entry in s_names:
        s_initial = entry.split(" ")
        print(s_initial[0][0] + s_initial[1][0])


def thirds():
    sents = eval(input("Enter # of Input Sentences: "))
    for i in range(sents):
        sentence = input("Enter sentence: ")
        print(sentence[2::3])


def word_avg():
    x = input("Enter your sentence: ")
    acc = 0
    words = x.split(" ")
    for word in words:
        acc = acc + len(word)
    output = acc / len(words)
    print(output)


def pig_latin():
    sentence = input("Enter Sentence to Translate: ")
    sent1 = sentence.lower()
    words = sent1.split(" ")
    print(sentence, "-> ", end= " ")
    for word in words:
        output = word[1:] + word[0] + "ay"
        print(output, end=" ")


def main():
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # word_avg()
    # pig_latin()
    # thirds()

    # add other function calls here


main()
