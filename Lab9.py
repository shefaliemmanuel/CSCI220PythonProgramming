## Lab9.py
##
## Name 1: Shefali Emmanuel
##
## Name 2: Elex Moore
##

from graphics import *
from math import sqrt

def starter():
    """
    Ask for a wrestler's weight and number of wins, determine whether
    the wrestler is a starter.
    """

    weight = eval(input("Enter the wrestler's weight: "))

    numWins = eval(input("Enter the number of wins: "))

    if weight >= 150 and weight < 160 and numWins >= 5:
        print("Starter") 
    elif weight > 199 or numWins > 20:
        print("Starter")
    else:
        print("Not Starter")

def isValid(isbn):
    if len(isbn) == 10:
        isbnMulti= 10
        isbnSum = 0
        for num in isbn:
            isbnSum += int(num) * (isbnMulti)
            isbnMulti= isbnMulti -1 
        if isbnSum % 11 == 0:
            valid = True
        else:
            valid = False
    else:
        valid = False

    return valid

def circleOverlap():
    """
    Draw two circles and determine whether they overlap.
    """
    #Build window
    winHeight = 400
    winWidth = 400
    win = GraphWin("Overlapping circles", winHeight, winWidth)

    #Text area for instructions for user
    instruct = Text(Point(winWidth/2, winHeight-10), "")
    instruct.draw(win)

    #Get center point and x/y for center
    instruct.setText("To draw a circle, click the centerpoint for the circle")
    center1 = win.getMouse()
    center1.draw(win)
    cX1= center1.getX()
    cY1 = center1.getY()

    #Get center point and x/y for center
    instruct.setText("To draw a circle, click the centerpoint for the circle")
    center2 = win.getMouse()
    center2.draw(win)
    cX2 = center2.getX()
    cY2 = center2.getY()

    #Get point on the circumference and its x/y coordinates
    instruct.setText("Click a point on the border of the circle.")
    border1 = win.getMouse()
    bX1 = border1.getX()
    bY1= border1.getY()

    #Get point on the circumference and its x/y coordinates
    instruct.setText("Click a point on the border of the circle.")
    border2 = win.getMouse()
    bX2 = border2.getX()
    bY2= border2.getY()

    #Calculate radius using Euclidean distance
    radius1 = sqrt((cX1-bX1) ** 2 + (cY1-bY1) ** 2)
    circle1 = Circle(center1, radius1)
    circle1.draw(win)

    #Calculate radius using Euclidean distance
    radius2 = sqrt((cX2-bX2) ** 2 + (cY2-bY2) ** 2)
    circle2 = Circle(center2, radius2)
    circle2.draw(win)

    distance= sqrt((cX2-cX1)**2+(cY2-cY1)**2)
    
    if (radius1 + radius2) >= distance:
        instruct.setText("The Circle Overlap's")
    else:
        instruct.setText("The Circle does not overlap.")

    # Wait for another click to exit
    instruct.setText("Click anywhere to close.")
    win.getMouse()
    win.close()

def leapYear(year):
    if year % 400 == 0:
        value = True
    elif year % 100 == 0:
        value = False
    elif year % 4 == 0:
        value = True
    else:
        value = False
    return value
                

def main():
    ''' Add code to test all of your functions '''
##    starter()
##    ans = isValid("0072946520")
##    if ans == True:
##        print("Valid")
##    else:
##        print("Not Valid")
    
##    circleOverlap()
    if leapYear(2000) == True:
        print("2000 is a leap year")
    else:
        print("2000 is not a leap year")

main()
