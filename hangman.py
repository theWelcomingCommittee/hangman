import random
import os
import requests
import itertools
import colorama
from colorama import Fore, Style
colorama.init()


def clear():
    os.system('clear')

# beginning with print hangman functions


def print_hangman(values):
    print()
    print("\t   ÷-------+")
    print("\t   |       |")
    print("\t   {}       |".format(values[0]))
    print("\t  {}{}{}      |".format(values[1], values[2], values[3]))
    print("\t   {}       |".format(values[4]))
    print("\t  {} {}      |".format(values[5], values[6]))
    print("\t           |")
    print("    ______________/|\\___")
    print(Fore.GREEN + "  ````'```''`````'``'`''``'``" + Style.RESET_ALL)
    print()


def print_hangman_win():
    print()
    print("\t   ÷-------÷")
    print("\t           |")
    print("\t           |")
    print("\t           |")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT +
          "\t   O" + Style.RESET_ALL + "       |")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT +
          "\t  /|\\" + Style.RESET_ALL + "      |")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT +
          "\t   |" + Style.RESET_ALL + "       |")
    print("    ______" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + "/" + Style.RESET_ALL +
          "_" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\\" + Style.RESET_ALL + "_____/|\\___")
    print(Fore.GREEN + "  ````'```''`````'``'`''``'``" + Style.RESET_ALL)
    print()

# print word to be guessed


def print_word(values):
    print()
    print("\t", end=' ')
    for x in values:
        print(x, end=' ')
    print()

# check for win


def check_win(values):
    for char in values:
        if char == "_":
            return False
    return True

# the GAME!


def hangman_game(word):

    clear()
    # stores letters of word to display
    word_display = []
    # store correct letters
    correct_letters = []
    # store incorrect letters chosen
    incorrect_letters = []
    # number of incorrect guessed chances
    chances = 0
    # hangman's body values
    hangman_values = [Fore.LIGHTCYAN_EX + 'O' + Style.RESET_ALL, Fore.LIGHTCYAN_EX + '/' + Style.RESET_ALL, Fore.LIGHTCYAN_EX +
                      '|' + Style.RESET_ALL, Fore.LIGHTCYAN_EX + '\\' + Style.RESET_ALL, Fore.LIGHTCYAN_EX + '|' + Style.RESET_ALL, Fore.LIGHTCYAN_EX + '/' + Style.RESET_ALL, Fore.LIGHTCYAN_EX + '\\' + Style.RESET_ALL]
    # hangman values before chosen
    show_hangman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ']

    # loop to create display of word
    for char in word:
        if char.isalpha():
            word_display.append('_')
            correct_letters.append(char.upper())
        # add a if char.isspace()?
            # word_display.append('  ')
        else:
            word_display.append(char)

    # functions for each game
    while True:
        # print hangman display
        print_hangman(show_hangman_values)
        print_word(word_display)
        print()
        print('incorrect letters : ', incorrect_letters)
        print()

    # player input with checking
        inp = input('pick a letter = ')

        if len(inp) != 1:
            clear()
            print(Fore.LIGHTRED_EX +
                  '  not a choice... try again' + Style.RESET_ALL, end='\r', flush=True)
            continue

    # check if alpha (can we combine with above with an OR?)
        if not inp[0].isalpha():
            clear()
            print(Fore.LIGHTRED_EX +
                  '  not a choice... try again' + Style.RESET_ALL, end='\r', flush=True)
            continue

        # if tried before
        if inp.upper() in incorrect_letters:
            clear()
            print(Fore.LIGHTRED_EX + '  you already done tried that! try again!' + Style.RESET_ALL,
                  end='\r', flush=True)
            continue

         # incorrect input
        if inp.upper() not in correct_letters:
            incorrect_letters.append(inp.upper())
            # update hangman
            show_hangman_values[chances] = hangman_values[chances]
            chances += 1

            # check if lost
            if chances == len(hangman_values):
                print()
                clear()
                print_hangman(hangman_values)
                print(Fore.RED + Style.BRIGHT +
                      "   YOU GOT HUNG!!! GAME OVER!" + Style.RESET_ALL)
                print("the word that your dead ass got wrong was:",
                      Fore.LIGHTCYAN_EX + word.upper() + Style.RESET_ALL)
                break

        # correct input
        else:
            # update word display
            for i in range(len(word)):
                if word[i].upper() == inp.upper():
                    word_display[i] = inp.upper()+" "

            if check_win(word_display):
                clear()
                print_hangman_win()
                print(
                    Fore.GREEN + "   CONGRATULATIONS!!! YOU'RE NOT DEAD YET!" + Style.RESET_ALL)
                print("       the word was:", Fore.LIGHTYELLOW_EX +
                      word.upper() + Style.RESET_ALL)
                break
        clear()


if __name__ == "__main__":
    clear()

    # possibly future links to csv or text files
    # categories
    topics = {1: "animals", 2: "outerspace", 3: "sports",
              4: "any word from these topics", 5: "literally any english word"}

    #words in categories
    dataset = {"animals": ['tiger', 'gorilla', 'racoon', 'snake', 'kangaroo'], "outerspace": [
        'jupiter', 'sputnik', 'mercury', 'neptune'], "sports": ['football', 'basketball', 'rugby']}

    # GAME LOOP
    while True:

        # game menu
        print()
        print("-----------------------------")
        print("    HANGMAN GAME MENU")
        print("-----------------------------")
        print()
        print("choose a topic:")
        for key in topics:
            print("PRESS ", key, " to select", topics[key])
        print("PRESS  6  to quit")
        print()

        ran = ()

        # choosing topic
        try:
            choice = int(input("Enter your choice = "))

        # check input
        except (ValueError or choice < 0 or choice > 6):
            clear()
            print("not a choice... Try Again")
            continue

        # making list of wild card list of all words from topics
        if choice == 4:
            res_list = []
            for key, value in (itertools.chain.from_iterable([itertools.product((k, ), v) for k, v in dataset.items()])):
                res_list.append(value)
            ran = random.choice(res_list)

        # ultra wild card from online api
        elif choice == 5:
            res = requests.get(
                "https://random-word-api.herokuapp.com/word").text
            ran = res.strip('["]')

        # exit choice
        elif choice == 6:
            print()
            print("---------------------")
            print(" Thanks for playin'!!!")
            break

        # pick of the topics
        else:
            chosenTopic = topics[choice]
            ran = random.choice(dataset[chosenTopic])

        # run game function
        hangman_game(ran)
