# CSCI 220L - Lab 10 Solutions
#
# Name 1: Shefali Emmanuel
#
# Name 2: Savanah Tracy

import math
import random

def calculateSum(value, numIterations):
   i = 0
   total = 0
   while i < numIterations:
       total += value
       i += 1
   return total

def areEqual(num1, num2):
    if abs(num1 - num2) < .0001:
        answer = True
    else:
        answer = False
    return answer

def goodInput():
    value = eval(input("Please input a number: "))
    while (value < 1 or value > 10) and value != -1 and value <= 50:
        value = eval(input("Please imput a number between 1 and 10 include, -1, or greater than 50. "))
        print(str(value) + " is a good input.")
    return value

def numDigits():
    number = 1
    while number > 0:
        number = eval(input("Input a number-- 0 or negative to stop: "))
        digits = 1
        length = number//10
        anotherLength = length
        while anotherLength != 0 and length != 0:
            anotherLength = anotherLength//10
            digits += 1
        print(digits)

def hiLoGame():
    value = random.randint(1,100)
    guess = eval(input("Guess a number between 1 and 100:"))
    numberOfGuesses = 1
    print(value)
    while guess !=value and numberOfGuesses < 7:
        numberOfGuesses +=1
        if guess>value:
            print("Too High")
        elif guess<value:
            print("Too Low")
        guess = eval(input("Try again, input another number:"))
        if guess == value:
            print("Correct. You won in " + str(numberOfGuesses)+" guesses")
        elif numberOfGuesses == 7:
            print("Sorry, you lost.")

def main():
##    sums = calculateSum(.1, 10)
##    print("Sum = " + str(sums))
##
##    results = sums
##    equals = areEqual(1.0, results)
##    if equals == True:
##        print("The two numbers are equal.")
##    else:
##        print("The two numbers are not equal")
##    
##    nums = goodInput()
##    print(nums)
    
##    numDigits()
    hiLoGame()
    
main()
