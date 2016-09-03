## Lab1.py
## CSCI 220L
## Shefali Emmanuel

import math

#Simple function to print statement to user
def main():
    print ("Programming is fun, but it is not a spectator sport.")
    print ("I look forward to learning tocontrol this computer though programming!")
    print ("Hello, world") #one string
    print ("Hello", "world") #seperatestrings #comma means space
    print ("2" + "3") #string concatenation
    print (2 + 3)
    print (2 * 3)
    print ("2" * 3) #string integer

#this function calcualtes the area of a rectangle
def CalcRectArea():
    print("Calcultes the Area of a Rectangle")
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print ("Area =", area)
    
#this fucntion calcuates the volume of a cylinder
def CalcCylinderVolume():
    print("Calucates the Volume of a Cylinder")
    PI= math.pi
    Radius= eval (input("Enter raduis: "))
    Height= eval (input("Enter height: "))
    Area= PI * Radius * Radius * Height
    print("Area:", Area)
    
#this function calculates a basketball player's total shots and shots made
def shootingPercentage():
    print ("Calculates a basketball player's total shots and shots made.")
    shotsMade = eval(input("Enter the Shots Made: "))
    totalShots = eval(input("Enter the Total Shots: "))
    shootingPercentage = (shotsMade / totalShots) * 100
    print("shootingPercentage: ", shootingPercentage)

#this function calculates the cost of shipping a coffee order
def coffee():
    print("Calucates the Cost of Shipping a Coffee Order")
    COFFEE_PER_POUND= 10.50 #CONSTANT
    SHIPPING_PER_POUND= 0.86
    OVERHEAD= 1.50
    numberOfPounds = eval(input("Number of Pounds: "))
    totalCostOfPounds = numberOfPounds * COFFEE_PER_POUND
    totalShipping = numberOfPounds * SHIPPING_PER_POUND
    total = OVERHEAD + totalCostOfPounds +totalShipping
    print("Total: ", total)

#this fuction calcualtes kilometers to miles
def kilometersToMiles():
    kilometers = eval(input("Number of Kilometers: "))
    KM_TO_MILES = 1.61
    totalMiles = kilometers / KM_TO_MILES
    print("Total Miles: ", totalMiles)
    
