
## lab2.py
## Purpose: Solves problems assigned in Lab 2
## Name: Shefali Emmanuel CSCI 220 5:10

import math

def helloWorld():
    print("Hello, world!")

def sumOfThrees():
    print("This function sums multiples of three.")
    total = 0
    #user input Upper Bound value
    upperBound = eval(input("Upper Bound: "))
    
    for i in range (upperBound//3):
        total = total + i * 3 + 3

    print()
    print("Total: ", total)
    average = total/upperBound
    print("Average: ", average )

def multiplicationTable():
    print("Prints a multiplication table for the numbers 1 through 12")

    #user input value
    value = 12

    for i in range (value):
        print (i+1, end = " ")
    print()
    for i in range (value):
        print (2 * (i+1), end = " ")
    print()
    for i in range (value):
        print (3 * (i+1), end = " ")
    print()
    for i in range (value):
        print (4 * (i+1), end = " ")
    print()
    for i in range (value):
        print (5 * (i+1), end = " ")
    print()
    for i in range (value):
        print (6 * (i+1), end = " ")
    print()
    for i in range (value):
        print (7 * (i+1), end = " ")
    print()
    for i in range (value):
        print (8 * (i+1), end = " ")
    print()
    for i in range (value):
        print (9 * (i+1), end = " ")
    print()
    for i in range (value):
        print (10 * (i+1), end = " ")
    print()
    for i in range (value):
        print (11 * (i+1), end = " ")
    print()
    for i in range (value):
        print (12 * (i+1), end = " ")
    print()

def triangleArea():
    print ("CalculateS the area of a triangle given the length of its three sides.")
    #user input values
    a= eval(input("A: "))
    b= eval(input("B: "))
    c= eval (input("C: "))
    #formula for average side
    s= (a+b+c)/(2)
    #formula for area
    area= (s*(s-a)*(s-b)*(s-c))
    area= math.sqrt(area)
    print("Area: ", area)

def sumSquares():
    print("Calculates the sum of the squares of the numbers in a given range.")
    total = 0
    lowerBound = eval(input("Lower Bound Value: "))
    upperBound = eval(input("Upper Bound Value: "))
    for i in range(lowerBound, upperBound+1):
        total = total + i**2
    print("Sum: ",total, end = " ")
    print()

def power():
    print("Calculates the base raised to a power.")
    total= 1
    base= eval(input("Base Value: "))
    exponent= eval(input("Exponent Value: "))
    for i in range(exponent):
        total = total * base
    print("Total: ", total)
    print()
    

#Type each function here then call the function from main() below.
#Once the function is working correctly, you can put a comment symbol
#in front of the call in main() so that you don't have to see it run over
#and over.  An example helloWorld function is above with a commented out
#call to the working function below.

#def main():
    #helloWorld()  
    #sumOfThrees()
    #multiplicationTable()
    #triangleArea()
    #sumSquares()
    #power()
