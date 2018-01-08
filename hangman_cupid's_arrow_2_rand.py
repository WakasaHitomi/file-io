
#Cupid's Arrow
#Dammorah J.

import os
import random
limit = 8

def start_screen():
    file = "art/hangman_splash_screen.txt"
    with open(file, 'r') as f:
        lines = f.read().splitlines()

    print(lines)


def get_puzzle():
    path = "data"

    file_names = os.listdir(path)

    for i, f in enumerate(file_names):
        print(str(i) + ") " + f)

    choice = input("pick one")
    choice = int(choice)

    file = path + "/" + file_names[choice]
    print(file)

    with open(file, 'r') as f:
        lines = f.read().splitlines()


    category_name = lines[0]
    puzzle = random.choice( lines[1:] )

    print(category_name)

    return puzzle
    print("")
    print("")
    
def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

    print("")
    print("")

def get_guess():
    letter = input ("Guess a letter")
    letter = letter.lower()
    if len(letter) == 1 and letter.isalpha() == True:
        return letter
    else:
        print("Please enter a single letter and not a number or symbol?")
        return get_guess()
    print("")
    print("")

def show_credits():
    file = "art/hangman_show_credits.txt"
    with open(file, 'r') as f:
        lines = f.read().splitlines()

    print(lines)

    exit()

def display_board(solved, guesses):
    print(solved, guesses)
    print("")
    print("")

def show_result(strikes, limit, puzzle):
    if strikes <= limit:
        print("You've Guessed it!")
        print("")
        play_again()

    if strikes > limit:
        print("You have taken an L. Good try though. Your word was " + str(puzzle) + ".")
        print("")
        play_again()

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            play() == True
        elif decision == 'n' or decision == 'no':
            show_credits()
        else:
            print("You're response was incorrect.")

    print("")
    print("")

def mistakes(strikes, limit):
    if strikes == 0:
        file = "art/hangman_zero_strikes.txt"
        with open(file, 'r') as f:
            lines = f.read().splitlines()

        print(lines)
        
    if strikes == 1:
        file = "art/hangman_one_strike.txt"
        with open(file, 'r') as f:
            lines = f.read().splitlines()

        print(lines)


    if strikes == 2:
        file = "art/hangman_two_strikes.txt"
        with open(file, 'r') as f:
            lines = f.read().splitlines()

        print(lines)
 

    if strikes == 3:
        file = "art/hangman_three_strikes.txt"
        with open(file, 'r') as f:
            lines = f.read().splitlines()

        print(lines)
            print(lines)
 

    if strikes == 4:
        file = "art/hangman_four_strikes.txt"
        with open(file, 'r') as f:
            lines = f.read().splitlines()

        print(lines)

    if strikes == 5:
        file = "art/hangman_five_strikes.txt"
        with open(file, 'r') as f:
            lines = f.read().splitlines()

        print(lines)
    if strikes == 6:
        file = "art/hangman_six_strikes.txt"
        with open(file, 'r') as f:
            lines = f.read().splitlines()

        print(lines)

    if strikes == 7:
        file = "art/hangman_seven_strikes.txt"
        with open(file, 'r') as f:
            lines = f.read().splitlines()

        print(lines)
        

    if strikes == 8:
         file = "art/hangman_eight_strikes.txt"
        with open(file, 'r') as f:
            lines = f.read().splitlines()

        print(lines)
        
def play():
    strikes = 0
    
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved, guesses)

    while playing:
        solved !=  puzzle
        guesses += get_guess()
        solved = get_solved(puzzle, guesses)
        display_board(solved, guesses)
        
        if guesses[-1] not in puzzle:
            strikes += 1
        mistakes(strikes, limit)

        if strikes > limit:
            show_result(strikes, limit, puzzle)

        if puzzle == solved:
            show_result(strikes, limit, puzzle)

    show_result(strikes, limit, puzzle)

start_screen()

playing = True

while playing:
    play()
    playing = play_again()
