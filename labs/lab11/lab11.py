"""
Name: Patrick Puckhaber
hangman.py
"""

from random import *


def getWords(wordList):
    file = open(wordList, "r")
    lines = file.readlines()
    words = []
    for word in lines:
        word = word.replace("\n", "")
        words.append(word)
    file.close()
    return words


def pickWord(words):
    secret_word = words[randint(1, len(words))]
    return secret_word


def guessWord(secret_word, guess_letters, guessed_word, letter):
    check = False
    for i in range(len(secret_word)):
        if secret_word[i] == letter:
            guessed_word[i] = letter
            check = True
    if check:
        return True
    guess_letters.append(letter)
    return False


def wordSpelled(guess_word, secret_word):
    if "".join(guess_word) == secret_word:
        return True
    else:
        return False


def guessLetter(guessed_letters, secret_word, guessed_word):
    letter = input("Guess a Letter: ")
    letter = letter.lower()
    check = False
    while check == False:
        check = True
        for ch in guessed_letters:
            if letter == ch:
                print("This letter has already been guessed, try again.")
                letter = input("Guess a letter: ")
                letter = letter.lower()
                check = False
        if (len(letter) != 1) or not (ord(letter) > 97 and ord(letter) <= 121):
            print("This is an invalid entry, try again")
            letter = input("guess a letter: ")
            letter = letter.lower()
            check = False
    if guessWord(secret_word, guessed_letters, guessed_word, letter):
        return True
    else:
        return False


def printBoard(guessed_word, turn_count, guessed_letters):
    print("--" + ("-----" * len(guessed_word)) + "--")
    print(guessed_word)
    print("--" + ("-----" * len(guessed_word)) + "--")
    print()
    print("Turn number: ", turn_count)
    print("Incorrectly guessed letter(s): ", str(guessed_letters))


def playGame():
    words = getWords("list.txt")
    secret_word = pickWord(words)
    turn_count = 0
    guessed_letters = []
    guessed_word = ["-"] * len(secret_word)
    printBoard(guessed_word, turn_count, guessed_letters)
    while turn_count < 8 and not wordSpelled(guessed_word, secret_word):
        if guessLetter(guessed_letters, secret_word, guessed_word) == False:
            turn_count += 1
            printBoard(guessed_word, turn_count, guessed_letters)
    if turn_count >= 7:
        print("You are out of turns, Game Over")
    else:
        print("you have won the game!")

def main():
    playGame()
    pass


main()
