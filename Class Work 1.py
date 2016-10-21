#class work 2
#Author:Shefali Emmanuel CSCI 220 9:30
#Authencity Statement: look at the submission policy on oaks

#Purpose: convert cups to ml
#input: cups- user input
#output: display ounces, cups, ml to monitor

import math

import graphics

def cupsToMl():
    print("Cup Converter")
    print()

    #conversion value
    CUPS_TO_OZ = 8
    OZ_TO_ML = 29.57

    #input from user
    cups= eval(input("Enter the number of cups: "))

    #calculates ounces
    ounces = cups * CUPS_TO_OZ

    #calcualtes ml
    ml = ounces * OZ_TO_ML

    #output
    print ()
    print (cups, "cups = ", ounces,"ounces = ", ml, "mL=")

def sibCount():
    total = 0
    numPeople = eval (input("Enter the number of persons to query: "))
    for i in range (numPoeple):
        sib = eval(input("How many siblings? "))
        total = total + sib
    print()
    print("Total: ", total)
    average = total/numPeople
    print("Average: ", average)

def summation():
    upperBound = eval(input("Upper Bound? ")) #this is only an upperbound problem
    total = 0 #set total to 0 so that you will start the listing from the first variable not 0
    for i in range (upperBound + 1): # "+1" does this well
        total = total + i
        print ("Total: ", total, "i: ", i)

def range():
    for i in range(1,13):
        print(i, end ="\t")

def multTable():
    for i in range (1,6):
        print(i, end= "\t")
    print()
    for i in range(1,6):
        print(i*2, end = "\t")
    print()
    for i in rangle (1,6):
        print(i*3, end = "\t")
        
def newMultTable():
    for j in range(1,6):
        for i in range(1,6):
            print(i*j,end = "\t")
        print()

def factorial():
    factorial= eval(input("Factorial Number: "))

    prod = 1
    for i in range (1, factorial+1):
        prod = prod * i
    print(num, "! =", prod)

def newFactorial():
    for i in range (num, 0, -1):
        prod = prod * i
        print(num, "! =", prod)

def numsDivisibleByFive():
    upperBound= eval(input("What is the Upper Bound Value? "))
    total=0 #start with 0 when adding
    for i in range(-10,upperBound+1,5) # +1 to include the upperbound
    print(i, end = "\t") 
        total= total + i

    print("\Ntotal:", total)

def summationEq():
    numTerms= eval(input("Enter the number of terms:"))
    total=0
    for i in range(numTerms):
        num=i+1
        denom= num*3
        print(numerator,"/", denom) #errorchecking
        total += numerator/demon
    print("\nTotal:", total)
