
#Cupid's Arrow
#Dammorah J.

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
    print(" ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄  \\  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ")
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
    puzzle = ["velocity", "heart", "insanity", "disaster", "tragedy", "misery", "hope", "depression", "embrace", "romance", "cherrish", "butterflies"]
    return puzzle[random.randint(0,11)]
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
        print(",d88b.d88b,  ,d88b.d88b, ,d88b.d88b, ,d88b.d88b, ,d88b.d88b,  ,d88b.d88b,  ,d88b.d88b,  ,d88b.d88b,     ")
        print("88888888888  88888888888 88888888888 88888888888 88888888888  88888888888  88888888888  88888888888  ")
        print("`Y8888888Y'  `Y8888888Y' `Y8888888Y' `Y8888888Y' `Y8888888Y'  `Y8888888Y'  `Y8888888Y'  `Y8888888Y' ")
        print("  `Y888Y'      `Y888Y'     `Y888Y'     `Y888Y'     `Y888Y'      `Y888Y'      `Y888Y'      `Y888Y'  ")
        print("    `Y'          `Y'         `Y'         `Y'         `Y'          `Y'          `Y'          `Y'  ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ 8 out of " + str(limit) + " strikes left ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~" + str(strikes) + " wrong guesses ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("")
        
    if strikes == 1:
        print(",d88b.d88b,  ,d88b.d88b, ,d88b.d88b, ,d88b.d88b, ,d88b.d88b,  ,d88b.d88b,  ,d88b.d88b, |,d88b/ /d88b,     ")
        print("88888888888  88888888888 88888888888 88888888888 88888888888  88888888888  88888888888 |88888\ \88888  ")
        print("`Y8888888Y'  `Y8888888Y' `Y8888888Y' `Y8888888Y' `Y8888888Y'  `Y8888888Y'  `Y8888888Y' |`Y888/ /888Y' ")
        print("  `Y888Y'      `Y888Y'     `Y888Y'     `Y888Y'     `Y888Y'      `Y888Y'      `Y888Y'   |  `Y8\ \8Y'  ")
        print("    `Y'          `Y'         `Y'         `Y'         `Y'          `Y'          `Y'     |     `Y'  ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ 7 out of " + str(limit) + " strikes left ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~" + str(strikes) + " wrong guesses ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("")

    if strikes == 2:
        print(",d88b.d88b,  ,d88b.d88b, ,d88b.d88b, ,d88b.d88b, ,d88b.d88b,  ,d88b.d88b,  |,d88b/ /d88b, ,d88b/ /d88b,    ")
        print("88888888888  88888888888 88888888888 88888888888 88888888888  88888888888  |88888\ \88888 88888\ \88888 ")
        print("`Y8888888Y'  `Y8888888Y' `Y8888888Y' `Y8888888Y' `Y8888888Y'  `Y8888888Y'  |`Y888/ /888Y' `Y888/ /888Y'")
        print("  `Y888Y'      `Y888Y'     `Y888Y'     `Y888Y'     `Y888Y'      `Y888Y'    |  `Y8\ \8Y'     `Y8\ \8Y' ")
        print("    `Y'          `Y'         `Y'         `Y'         `Y'          `Y'      |     `Y'           `Y' ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ 6 out of " + str(limit) + " strikes left ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~" + str(strikes) + " wrong guesses ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("")

    if strikes == 3:
        print(",d88b.d88b,  ,d88b.d88b, ,d88b.d88b, ,d88b.d88b, ,d88b.d88b,  |,d88b/ /d88b, ,d88b/ /d88b,  ,d88b/ /d88b,   ")
        print("88888888888  88888888888 88888888888 88888888888 88888888888  |88888\ \88888 88888\ \88888  88888\ \88888 ")
        print("`Y8888888Y'  `Y8888888Y' `Y8888888Y' `Y8888888Y' `Y8888888Y'  |`Y888/ /888Y' `Y888/ /888Y'  `Y888/ /888Y' ")
        print("  `Y888Y'      `Y888Y'     `Y888Y'     `Y888Y'     `Y888Y'    |  `Y8\ \8Y'     `Y8\ \8Y'     `Y8\ \8Y'")
        print("    `Y'          `Y'         `Y'         `Y'         `Y'      |     `Y'           `Y'           `Y' ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ 5 out of " + str(limit) + " strikes left ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~" + str(strikes) + " wrong guesses ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("")

    if strikes == 4:
        print(",d88b.d88b,  ,d88b.d88b, ,d88b.d88b, ,d88b.d88b, |,d88b/ /d88b, ,d88b/ /d88b,  ,d88b/ /d88b,  ,d88b/ /d88b,  ")
        print("88888888888  88888888888 88888888888 88888888888 |88888\ \88888 88888\ \88888  88888\ \88888  88888\ \88888 ")
        print("`Y8888888Y'  `Y8888888Y' `Y8888888Y' `Y8888888Y' |`Y888/ /888Y' `Y888/ /888Y'  `Y888/ /888Y'  `Y888/ /888Y' ")
        print("  `Y888Y'      `Y888Y'     `Y888Y'     `Y888Y'   |  `Y8\ \8Y'     `Y8\ \8Y'     `Y8\ \8Y'       `Y8\ \8Y' ")
        print("    `Y'          `Y'         `Y'         `Y'     |     `Y'           `Y'           `Y'             `Y'  ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ 4 out of " + str(limit) + " strikes left ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~" + str(strikes) + " wrong guesses ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("")

    if strikes == 5:
        print(",d88b.d88b,  ,d88b.d88b, ,d88b.d88b, |,d88b/ /d88b, ,d88b/ /d88b,  ,d88b/ /d88b,  ,d88b/ /d88b, ,d88b/ /d88b, ")
        print("88888888888  88888888888 88888888888 |88888\ \88888 88888\ \88888  88888\ \88888  88888\ \88888 88888\ \88888 ")
        print("`Y8888888Y'  `Y8888888Y' `Y8888888Y' |`Y888/ /888Y' `Y888/ /888Y'  `Y888/ /888Y'  `Y888/ /888Y' `Y888/ /888Y' ")
        print("  `Y888Y'      `Y888Y'     `Y888Y'   |  `Y8\ \8Y'     `Y8\ \8Y'     `Y8\ \8Y'       `Y8\ \8Y'     `Y8\ \8Y'  ")
        print("    `Y'          `Y'         `Y'     |     `Y'           `Y'           `Y'             `Y'           `Y'    ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ 3 out of " + str(limit) + " strikes left ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~" + str(strikes) + " wrong guesses ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("")

    if strikes == 6:
        print(",d88b.d88b,  ,d88b.d88b, |,d88b/ /d88b, ,d88b/ /d88b,  ,d88b/ /d88b,  ,d88b/ /d88b, ,d88b/ /d88b,  ,d88b/ /d88b,  ")
        print("88888888888  88888888888 |88888\ \88888 88888\ \88888  88888\ \88888  88888\ \88888 88888\ \88888  88888\ \88888 ")
        print("`Y8888888Y'  `Y8888888Y' |`Y888/ /888Y' `Y888/ /888Y'  `Y888/ /888Y'  `Y888/ /888Y' `Y888/ /888Y'  `Y888/ /888Y' ")
        print("  `Y888Y'      `Y888Y'   |  `Y8\ \8Y'     `Y8\ \8Y'     `Y8\ \8Y'       `Y8\ \8Y'     `Y8\ \8Y'      `Y8\ \8Y' ")
        print("    `Y'          `Y'     |     `Y'           `Y'           `Y'             `Y'           `Y'            `Y' ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2 out of " + str(limit) + " strikes left ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~" + str(strikes) + " wrong guesses ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("")

    if strikes == 7:
        print(",d88b.d88b, |,d88b/ /d88b, ,d88b/ /d88b,  ,d88b/ /d88b,  ,d88b/ /d88b, ,d88b/ /d88b,  ,d88b/ /d88b,  ,d88b/ /d88b,  ")
        print("88888888888 |88888\ \88888 88888\ \88888  88888\ \88888  88888\ \88888 88888\ \88888  88888\ \88888  88888\ \88888 ")
        print("`Y8888888Y' |`Y888/ /888Y' `Y888/ /888Y'  `Y888/ /888Y'  `Y888/ /888Y' `Y888/ /888Y'  `Y888/ /888Y'  `Y888/ /888Y' ")
        print("  `Y888Y'   |  `Y8\ \8Y'     `Y8\ \8Y'     `Y8\ \8Y'       `Y8\ \8Y'     `Y8\ \8Y'      `Y8\ \8Y'      `Y8\ \8Y'  ")
        print("    `Y'     |     `Y'           `Y'           `Y'             `Y'           `Y'            `Y'            `Y'   ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ 1 out of " + str(limit) + " strikes left ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~" + str(strikes) + " wrong guesses ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("")

    if strikes == 8:
        print("|,d88b/ /d88b, ,d88b/ /d88b,  ,d88b/ /d88b,  ,d88b/ /d88b, ,d88b/ /d88b,  ,d88b/ /d88b,  ,d88b/ /d88b,  ,d88b/ /d88b, ")
        print("|88888\ \88888 88888\ \88888  88888\ \88888  88888\ \88888 88888\ \88888  88888\ \88888  88888\ \88888  88888\ \88888 ")
        print("|`Y888/ /888Y' `Y888/ /888Y'  `Y888/ /888Y'  `Y888/ /888Y' `Y888/ /888Y'  `Y888/ /888Y'  `Y888/ /888Y'  `Y888/ /888Y'")
        print("|  `Y8\ \8Y'     `Y8\ \8Y'     `Y8\ \8Y'       `Y8\ \8Y'     `Y8\ \8Y'      `Y8\ \8Y'      `Y8\ \8Y'      `Y8\ \8Y' ")
        print("|     `Y'           `Y'           `Y'             `Y'           `Y'            `Y'            `Y'            `Y'")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ 0 out of " + str(limit) + " strikes left ( this is your last guess, make it good ) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~" + str(strikes) + " wrong guesses ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("")
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
