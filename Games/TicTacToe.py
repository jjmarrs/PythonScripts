#This program is not yet finished

import random

def displayGrid():
    print("     |        |      ")
    print("  1  |    2   |   3  ")
    print("     |        |      ")
    print("---------------------")
    print("     |        |      ")
    print("  4  |    5   |   6  ")
    print("     |        |      ")
    print("---------------------")
    print("     |        |      ")
    print("  7  |    8   |   9  ")
    print("     |        |      ")

def explainGame():
    print("\nWelcome to the quick run through of the game 'Tic Tac Toe'")
    print("As you can see on the board above, there are 9 individual squares")
    print("You will be asked the option of choosing an 'X' or an 'O'")
    print("After your selection is made, the game will officialy begin.")
    print("\nYou will choose a number and place a corresponding X or O in that square.")
    print("The main goal of the game is to get 3 of your 'X's' or 'O's' in 3 vertical, horizontal"
          " or diagonal squares.")
    print("Once you do that you win, and if the opponent (the computer in this case) does the above, they win.")
    print("Good luck and have fun!")
    askSelection()

def askSelection():
    userChoice =(input("\nChoose your weapon: X or O?"))
    if userChoice == 'X':
        selection = 'X'
    else:
        selection = 'O'
    youSure = input("You have selected " + userChoice + (" Is that right? (y/n)"))
    if youSure == 'n':
        askSelection()
    else:
        begin()

def begin():
    board = [1,2,3,4,5,6,7,8,9]



def startGame():
    print("\nHello user, welcome to the game of Tic Tac Toe\n")
    displayGrid()
    userInput = (input("do you know how to play? (y/n)"))
    if userInput == ' n':
        explainGame()
    else:
        askSelection()

startGame()

#NOT YET FINISHED
#Soon(TM)