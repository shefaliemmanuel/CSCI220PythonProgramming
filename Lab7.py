# Lab7.py
# Name 1: Shefali Emmanuel
# Name 2: Sean Fry

#main() should be the only file executed when you are checked off for this lab
#thus add code to main() to call any functions you write.

import math

def read_file(nameOfFile):
    infile = open(nameOfFile,"r")
    file_String = infile.read()
    infile.close()
    return file_String

def numberWords(filename):
    infile = open(filename, "r")
    file = infile.read()
    
    outfileName = "numberedWords.txt"
    outfile = open(outfileName, "w")
    
    print("Data written to: " + outfileName)

    splitFile = file.split()
    print(splitFile)

    count = 1
    for word in splitFile:
        count += 1
        print(str(count) + ". " + word, file = outfile)
    
    infile.close()
        
def hourlyWages(infileName, outfileName):
    infile= open(infileName, "r")
    outfile= open(outfileName,"w")
    
    increase = 1.65
    for line in infile:
        wageList = line.split()
        hours= int(wageList[3])
        dollars = int(wageList[2]) + increase
        wage = dollars * hours
        
        print(wageList[0] + " " +wageList[1] + " ${:.2f}".format(wage), file=outfile)
    print("Data written to, total.txt.")
    
def nameValue(name):
    lowerName = name.lower()
    ordNum= ord("a")- 1
    total=0
    for ch in lowerName:
        number = ord(ch)
        final = number- ordNum
        total += final
    return total

def sphereArea(radius):
    area = (4/3) + math.pi * radius ** 2
    return area

def sphereVolume(radius):
    area = (4/3) + math.pi * radius ** 3
    return area

def sumN(n):
    total= 0
    for i in range(n):
        nums = eval(input("Input your value for number " +str(i+1) + ": "))
        total += nums
    return total

def sumNCubes(n):
    total = 0

    for i in range(n):
        nums = eval(input("Input your value for number " +str(i+1) + ": "))

        total += nums ** 3
    return total

def main():
    hourlyWages("hourlyWages.txt", "total.txt")

    userName= input("What is your name?: ")

    nameValue(userName)

    area= sphereArea(5)
    print("Area with radius= 5, " + str(round(area,2)))

    area= sphereVolume(10)
    print("Volume= 10, " + str(round(area,2)))

    n= eval(input("How many numbers:"))
    print(sumN(n))

    n= eval(input("How many numbers:"))
    print(sumNCubes(n))
    
main()
