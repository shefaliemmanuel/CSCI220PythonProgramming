# CSCI 220L - Lab 8 Solutions
#
# Name 1: Shefali Emmanuel
#
# Name 2:Austin Hollis 
#

def formatPractice():
    
    print ("It's raning {1} and {0}.".format("dogs", "cats"))
    
    print("{0:0.2f} {1:1.3f}".format(2.3,.4567))

    print("Time Left {0:02}:{1:05.2f}". format(3,7.4589))

    print("{0} {1}: {2:2.2f}".format("Steph", "Curry", 43.75432))

def encode():
    userString= input("What do you want encoded? ")
    key= input("What key do you want to shift by? ")
    char=""
    for letter in userString:
        values= ord(letter)
        newVal= values + eval(key)
        char+= chr(newVal)
    print(char)

def encodeBetter():
    userString= input("What do you want encoded? ")
    key= eval(input("What key do you want to shift by? "))
    strDone = ""
    for letter in userString:
        formula= (((ord(letter)-ord("a"))+ key) % 26) + ord("a")
        strDone += chr(formula)
    print(strDone)

def testTens():
    values = [5, 2, -3]
    print(values)
    addTen(values)
    print(values)
    
def addTen(values):
    for i in range(len(values)):
        values[i]=values[i]+10
    print(values)
    
def squareEach(values):
    for i in range(len(values)):
        values[i]=values[i] **2

def sumList(values):
    sumNums=0
    for i in range(len(values)):
        sumNums+= values[i]
    return sumNums
    
def toNumbers():
    values= ["3","5.7","2"]
    for i in range(len(values)):
        values[i] = eval(values[i])
    print(values)
        
    
toNumbers()

def sumOfSquares():
    values = [2, 3, 4]
    print(values)
    squareEach(values)
    total = sumList(values)
    print(total)
sumOfSquares()
