
#Cupid's Arrow
#Dammorah J.

import os
import random
limit = 8

def start_screen():
    print("oo      ")
    print("   oo     OOOOOOOO:       OOOOOOOO!        ")
    print("      oOOOO!!!!;;;;O    OO.......:;!O         ")
    print("     'OOO!!!;;;;;;;;O  O.......:   ;!O       ")
    print("     OOO!!!!;;::::::.OO........:    ;!O     ")
    print("     OO!!!!;;:::::..............:   ;!O    ")
    print("    OOO!!!;::::::..............:   ;!O    ")
    print("      OO!!;;::::::.............:   ;!O     ")
    print("      OO!;;::::::......oo.....::::!O       ")
    print("        O!!;::::::........oo..:::O         ")
    print("          !!!;:::::..........ooO           ")
    print("              !!;:::::.......O   oo        ")
    print("               ;;::::.....O        oo  ,o ")
    print("                  :::..O              ooo")
    print("                    ::.              oooo ")
    print("                     :                    ")
    print(" ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄  \   ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ")
    print("▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌    ▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌ ")
    print("▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌   ▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌ ")
    print("▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌   ▐░▌               ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌")
    print("▐░▌          ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌       ▐░▌   ▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌   ▄   ▐░▌ ")
    print("▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌   ▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌ ")
    print("▐░▌          ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░▌     ▐░▌       ▐░▌    ▀▀▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌▐░▌ ▐░▌░▌ ▐░▌")
    print("▐░▌          ▐░▌       ▐░▌▐░▌               ▐░▌     ▐░▌       ▐░▌             ▐░▌     ▐░▌       ▐░▌▐░▌     ▐░▌  ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌ ")
    print("▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌           ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌    ▄▄▄▄▄▄▄▄▄█░▌     ▐░▌       ▐░▌▐░▌      ▐░▌ ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌▐░▌░▌   ▐░▐░▌")
    print("▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░▌    ▐░░░░░░░░░░░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌")
    print(" ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀      ▀▀▀▀▀▀▀▀▀▀▀       ▀         ▀  ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀       ▀▀  ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")

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

    print(lines)

    category_name = lines[0]
    puzzle = random.choice( lines[1:] )

    print(category_name)
    print(puzzle)

    puzzle = (puzzle)
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
    print("")
    print("")
    print("Origial base for Hangman game...... J. Cooper")
    print(" ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" ")
    print("      __   __       ")
    print("     /  \./  \/\_                              ")
    print("  __{^\_ _}_   )  }/^\                              ")
    print(" /  /\_/^\._}_/  //  /                             ")                      
    print("(  (__{(@)}\__}.//_/__A____A_______A________A________A_____A___A___A_____ ")
    print(" \__/{/(_)\_}  )\\ \\---v-----V-----V---Y-----v----Y------v-----V-----v-- ")
    print("   (   (__)_)_/  )\ \>    ")
    print("    \__/     \__/\/\/ ")
    print("       \__,--'     ")
    print(" ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" ")
    print("Modified and Recreated by........WakasaHitomi")
    print("")
    print("")
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
        """file that opens"""
        
    if strikes == 1:
        """file insert"""

    if strikes == 2:
        """file insert"""

    if strikes == 3:
        """file insert"""

    if strikes == 4:
        """file insertr"""

    if strikes == 5:
        """file insert"""

    if strikes == 6:
        """file insert"""

    if strikes == 7:
        """file"""
        

    if strikes == 8:
        """file"""
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
