import random
import os


def clear():
    os.system('clear')


# print hangman
def print_hangman(values):
    print()
    print("\t   ÷--------+")
    print("\t   |        |")
    print("\t   {}       |".format(values[0]))
    print("\t  {}{}{}      |".format(values[1], values[2], values[3]))
    print("\t   {}       |".format(values[4]))
    print("\t  {} {}      |".format(values[5], values[6]))
    print("\t           |")
    print("    _______________|____")
    print("   ``'```''`````'````''``")
    print()


def print_hangman_win():
    print()
    print("\t   ÷-------÷")
    print("\t            |")
    print("\t            |")
    print("\t           |")
    print("\t   O       |")
    print("\t  /|\\      |")
    print("\t   |       |")
    print("    ______/_\\______|____")
    print("   ``'```''`````'````''``")
    print()


# print word to be guessed
def print_word(values):
    print()
    print("\t", end='')
    for x in values:
        print(x, end='')
    print()

# check for win


def check_win(values):
    for char in values:
        if char == "_ ":
            return False
    return True


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
    hangman_values = ['O', '--', '|', '--', '|', '/', '\\']

    # hangman values before chosen
    show_hangman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ']

    # loop to create display of word
    for char in word:
        if char.isalpha():
            word_display.append('- ')
        # add a if char.isspace()
            # word_display.append('  ')
        else:
            word_display.append(char + ' ')

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
            print('not a choice... try again')
            continue

    # check if aplpha (can we combine with above with an OR?)
        if not inp[0].isalpha():
            clear()
            print('not a choice... try again')
            continue

        # if tried before
        if inp.upper() in incorrect_letters:
            clear()
            print('you already done picked that! try again')
            continue

         # incorrect input
        if inp.upper() not in correct_letters:
            incorrect_letters.append(inp.upper())
            # update hangman
            show_hangman_values[chances] = hangman_values[chances]
            chances = chances + 1

            # check if lost
            if chances == len(hangman_values):
                print()
                clear()
                # print hung dude with dropped arms... maybe animation fall
                print("\tYOU GOT HUNG!!! GAME OVER!")
                print_hangman(hangman_values)
                print("The word that your dead ass got wrong was : ", word.upper())
                break

        # correct input
        else:
            # update word display
            for i in range(len(word)):
                if word[i].upper() == inp.upper():
                    word_display[i] = inp.upper()

            if check_win(word_display):
                clear()
                print("\tCongratulations! ")
                print_hangman_win()
                print("the word is : ", word.upper())
                break
        clear()


if __name__ == "__main__":
    clear()

    # categories
    topics = {1: "animals", 2: "outerspace", 3: "sports"}

    #words in categories
    dataset = {"animals": ['tiger', 'gorilla', 'racoon', 'snake', 'kangaroo'], "outerspace": [
        'jupiter', 'sputnik', 'mercury', 'neptune'], "sports": ['football', 'basketball', 'rugby']}

    # GAME LOOP
    while True:

        # game menu
        print()
        print("-------------------------------")
        print("\t\tGAME MENU")
        print("-------------------------------")
        print()
        for key in topics:
            print("PRESS ", key, " to select", topics[key])
        print("PRESS",  len(topics)+1, " to quit")
        print()

    # dealing with player category choice
        try:
            choice = int(input("Enter your choice = "))
        except ValueError:
            clear()
            print("not a choice... Try Again")
            continue
    # sanity checks for input
        if choice > len(topics)+1:
            clear()
            print("not even close to one of the choices... Try again")
            continue

        # elif to pick "wild card" random of all the topics!!!!!!

        # elif to pick "ultra wild card" from online api!!!!!!!!

        # exit choice
        elif choice == len(topics)+1:
            print()
            print("Thanks for playin'!")
            break

        # chosen topic
        chosenTopic = topics[choice]

        # selecting random word
        ran = random.choice(dataset[chosenTopic])

        # run rest of game function
        hangman_game(ran)