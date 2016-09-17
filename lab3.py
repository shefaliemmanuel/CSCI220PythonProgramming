## <Shefali Emmanuel>
## lab3.py

from graphics import *

#Calculate the average of a group of numbers per assignment instructions
def average():
    print("Finds average")

    totalGrade= eval(input("Number of Grades: "))

    sumGrade= 0
    
    for num in range(totalGrade):
        gradeNum= eval(input("Enter your grade on HW" + str(num+1) + "? "))
        print()
        
        sumGrade += gradeNum
        print("Sum of all Grades:", sumGrade)
        
    total= sumGrade/ totalGrade
    print("Average Total of Grades: ", total)

def fibonacci():
    print("Finds Fibonacci Number")
    
    nValue= eval(input("What is the value of n? "))

    first= 0
    second= 0
    next= 1
    
    for i in range(nValue):
        first= second
        second= next
        next= first + second
        print("Fibonacci Sequence: ", first)

def newton():
    print("Finds square root")
    x= eval(input("What is the value of X? "))
    appTime= eval(input("How many times to improve the approximation? "))
    approximation= x / 2
    for i in range(appTime):
        approximation= (approximation + (x/ approximation)) / 2
    print ("Approximation: ", approximation)

def buildHouse():
    #blue background
    win = GraphWin("Background", 500, 500)
    win.setBackground("blue")
    #white square house
    rectangle= Rectangle(Point(200,200), Point(300,300))
    rectangle.setFill("white")
    rectangle.draw(win)
    #brown triangle roof
    polygon= Polygon(Point(200,200), Point(250,100), Point(300,200))
    polygon.setFill("brown")
    polygon.draw(win)

def sequence():
    denom= 1
    numTerm= eval(input("Number of Terms in a Series: "))
    for i in range(numTerm):
        denom += (i % 2) *2

        print(denom)

def pi():
    denom= 1
    n= eval(input("What is the value of N: "))
    numTerm= eval(input("Number of Terms in a Series: "))
    for i in range(numTerm):
        product

#Example graphics program
def makeCircle():
    #creates the window
    winWidth = 300
    winHeight = 400
    win = GraphWin("Click a point", winWidth, winHeight)
    win.setBackground("yellow")

    #creates a Point object that is centered in the window
    center = Point(winWidth//2, winHeight//2)

    #draws a blue circle around center point
    ball = Circle(center, 20)
    ball.setFill("blue")
    ball.draw(win)
        
    #creates and displays instructions
    instructPoint = Point(winWidth//2, winHeight - 10)
    instructions = Text(instructPoint, "Click window to close.")
    instructions.draw(win)

    #Allows the user to click the window and then closes window
    clickPt = win.getMouse()
    win.close()
    
def main():
    average()
    #fibonacci()
    #newton()
    #sequence()
    #pi()
