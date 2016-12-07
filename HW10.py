# TicTacToe.py
# Name: Shefali Emmanuel
# CSCI 220 HW10
# Problem:To write a modular solution to the game of tic-tac-toe.
# Input: A list of functions that need to be tested in the main().
# Output: A Tic-Tac-Toe game.
# Certification of Authenticity:
# I certify that this lab is my own work, but I discussed it with:
# MH, Eduardo, Matthew Bell.

from graphics import*
import random
message3 = Text(Point(200,50),"Let's play Tic-Tac-Toe!")
message3.setTextColor("white")

#methord to build the board
def numbers():
    numbers=[1,2,3,4,5,6,7,8,9]
    return numbers

#create a void methord to display the board
def board(numbers):
    print("{0} | {1} | {2}\n----------".format(numbers[0],numbers[1], numbers[2]))
    print("{0} | {1} | {2}\n----------".format(numbers[3],numbers[4], numbers[5]))
    print("{0} | {1} | {2}\n".format(numbers[6],numbers[7], numbers[8]))

#create a void methord to fill a spot on the board
    #This method will need to have the board, the position to be filled
    #and the character to place in that position.  Do some error checking
    #here so that the board doesn’t allow for letters other than ‘x’ and ‘o’.
def spotFill(board,position,character):
    if (character == "X" or character == "O"):
        board[position]= character
        return board
    else:
        return board
        print("Insert a X or O variable")
    
#create a boolean method to determine if a spot is a legal spot on the board.
def legalSpot(position):
    newPosition= position - 1
    if (position <= 8 and position >= 0):
        return True
    else:
        print("Input a new position")

#tell when someone has won
def gameOverPlayer1(numbers):
# did someone get 3 in a row
    if numbers[0]== "X" and numbers[1]== "X" and numbers[2] == "X":
        return True
    elif numbers[3]== "X" and numbers[4]== "X" and numbers[5]== "X":
        return True
    elif numbers[6]== "X" and numbers[7]== "X" and numbers[8]== "X":
        return True
    elif numbers[0]== "X" and numbers[4]== "X" and numbers[8]== "X":
        return True
    elif numbers[2]== "X" and numbers[4]== "X" and numbers[6]== "X":
        return True
    elif numbers[0]== "X" and numbers[3]== "X" and numbers[6]== "X":
        return True
    elif numbers[1]== "X" and numbers[4]== "X" and numbers[7]== "X":
        return True
    elif numbers[2]== "X" and numbers[5]== "X" and numbers[8]== "X":
        return True
    else:
        return False
    
def gameOverPlayer2(numbers):
# did someone get 3 in a row
    if numbers[0]== "O" and numbers[1]== "O" and numbers[2]== "O":
        return True
    elif numbers[3]== "O" and numbers[4]== "O" and numbers[5]== "O":
        return True
    elif numbers[6]== "O" and numbers[7]== "O" and numbers[8]== "O":
        return True
    elif numbers[0]== "O" and numbers[4]== "O" and numbers[8]== "O":
        return True
    elif numbers[2]== "O" and numbers[4]== "O" and numbers[6]== "O":
        return True
    elif numbers[0]== "O" and numbers[3]== "O" and numbers[6]== "O":
        return True
    elif numbers[1]== "O" and numbers[4]== "O" and numbers[7]== "O":
        return True
    elif numbers[2]== "O" and numbers[5]== "O" and numbers[8]== "O":
        return True
    else:
        return False

#methord that runs the entire game while asking player 1 & 2 for their inputs
def playGame():
    player1= "X"
    player2= "O"
    moves=0
    currentBoard= numbers()
    board(currentBoard)
    isGameOver = isWon(gameOverPlayer1(currentBoard), gameOverPlayer2(currentBoard))
    while isGameOver == False and moves< 9:
        isGameOver = isWon(gameOverPlayer1(currentBoard), gameOverPlayer2(currentBoard))
        
        
        position= -198600
        while position > 9 or position < 0 or position==-198600:
            position= eval(input("Input a position Player 1: "))-1
            if position > 8 or position < 1:
                print("Invalid position.")
        character= "X"
        if legalSpot(position) == True:
            spotFill(currentBoard,position,character)
            board(currentBoard)
            moves += 1
        isGameOver = isWon(gameOverPlayer1(currentBoard), gameOverPlayer2(currentBoard))
        if isGameOver:
            return
        if moves >=9:
            return
        position= -198600
        while position > 9 or position < 0 or position==-198600:
            position= eval(input("Input a position Player 2: "))-1
            if position > 8 or position < 1:
                print("Invalid position.")
        character= "O"
        if legalSpot(position) == True:
            spotFill(currentBoard,position,character)
            board(currentBoard)
            moves += 1
        isGameOver = isWon(gameOverPlayer1(currentBoard), gameOverPlayer2(currentBoard))
        if isGameOver:
            return
        
#create a boolean method to determine if the game has been won.
def isWon(player1,player2):
    if (player1):
        print("Great Job Player 1! You Won!")
        return True
        
    elif (player2):
        print("Great Job Player 2! You Won!")
        return True

    else:
        return False

def main():
    playGame()
main()
