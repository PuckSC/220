"""
Name: Patrick Puckhaber
vigenere.py

Problem: Encodes a word with a key

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


def code(message, keyword):
    # message and keyword modifications
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
    return result


def main():
    window = GraphWin("Vigenere", 500, 250)
    window.setCoords(0, 0, 10, 10)

    # inputs
    message_input = Entry(Point(7, 7.5), 25)
    message_input.draw(window)

    key_input = Entry(Point(7, 5.5), 25)
    key_input.draw(window)

    # box labels
    message_text = Text(Point(2.5, 7.5), "Message to Encode")
    message_text.draw(window)

    key_text = Text(Point(2.5, 5.5), "Enter Keyword")
    key_text.draw(window)

    # encode button
    encode_text = Text(Point(5, 3), "Encode")
    button_outline = Rectangle(Point(4, 4), Point(6, 2))
    button_outline.draw(window)
    encode_text.draw(window)

    window.getMouse()

    # inputs
    message = message_input.getText()
    keyword = key_input.getText()

    # call function
    result = code(message, keyword)

    # result display
    encode_text.undraw()
    button_outline.undraw()
    output_text = Text(Point(5, 3.25), "Encrypted Message:")
    result_text = Text(Point(5, 2.5), "")
    close_text = Text(Point(5, .75), "Click Anywhere to Close Window")
    output_text.draw(window)
    result_text.draw(window)
    close_text.draw(window)

    result_text.setText(result)

    window.getMouse()
    window.close()


if __name__ == "__main__":
    main()
