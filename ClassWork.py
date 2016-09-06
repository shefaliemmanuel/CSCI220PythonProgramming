#class work 2
#Author:Shefali Emmanuel CSCI 220 9:30
#Authencity Statement: look at the submission policy on oaks

#Purpose: convert cups to ml
#input: cups- user input
#output: display ounces, cups, ml to monitor

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
    print (cups, "cups = ", ounces,"ounces = ", ml "mL")

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
    
