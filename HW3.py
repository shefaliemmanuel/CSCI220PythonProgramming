# Name: Shefali Emmanuel
# mean.py
# CSCI 220 HW3
# Problem: This program will output the RMS and the Harmonic
#          Mean (2 different ways to calculate the mean).
# Input: 10, 5, 2, 5
# Output: RMS Mean & Harmonic Mean
# Certification of Authenticity:
# I certify that this lab is entirely my own work.
# I certify that this lab is my own work, but I
# discussed it with: Zach Pickler

import math

def mean():
    print("This program outputs the RMS average and harmonic mean.")

    #total number of values
    values= eval(input("Number of Value's: "))

    #set values to 0
    sumValue= 0
    sumValueRMS= 0
    sumHarmonic= 0

    for i in range(values):

        #equation for finding values
        valueNum= eval(input("Value " + str(i + 1) + ": "))
        
        #sum of the values
        sumValue = sumValue + valueNum
        #sum of the values squared
        sumValueRMS += valueNum ** 2
        #one divided by the value of numbers
        sumHarmonic += 1/ valueNum

    #equation to find the average RSM
    rmsAverage= (sumValueRMS / values) ** .5
    print("RMS Average: ",rmsAverage)

    #equation of the Harmonic Mean
    harmonicMean= values/ sumHarmonic
    print("Harmonic Mean: ", harmonicMean)
               
mean()
    
                    
