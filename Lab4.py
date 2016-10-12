"""
Lab 3 - Graphics
Name: Shefali Emmanuel
"""

## Discussion #3, Graphics chapter of Zelle text
## Moves a circle based on user clicks
## Comments added: RHS

from graphics import *
import math

def squares():
    print("This function creates and moves squares")
    
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    #Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Click to move square", width, height)

    #number of times user can move circle
    numClicks = 5

    #create a space to instruct user
    instPt = Point(width/2, height-10)
    instructions = Text(instPt,"Click to move square")
    instructions.draw(win)

    #builds a square
    shape = Rectangle(Point(20,20),Point(40,40))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    #allows the user to click multiple times to move the
    #square
    for i in range(numClicks):
        p = win.getMouse()
        c = shape.getCenter() #center of square

        #move amount is distance from center of circle to the
        #point where the user clicked
        newX = p.getX() - c.getX()
        newY = p.getY() - c.getY()
       # shape.move(newX, newY)

        shapes= shape.clone()
        shapes.draw(win)
        shapes.move(newX, newY)
        
    win.getMouse()
    win.close()
    
def rectangle():
    
    width = 400
    height = 400
    win = GraphWin("Click to move rectangle", width, height)

    point1 = win.getMouse()
    point2 = win.getMouse()

    shape = Rectangle(point1,point2)
    shape.setOutline("black")
    shape.setFill("white")
    shape.draw(win)

    point1X = point1.getX()
    point1Y = point1.getY()
    point2X = point2.getX()
    point2Y = point2.getY()

    lengthA= point2Y - point1Y
    rectLength= math.fabs(lengthA)
    
    widthA= point2X - point1X
    rectWidth= math.fabs(widthA)

    area= rectLength * rectWidth
    perimeter= 2 * (rectLength + rectWidth)

    instPt = Point(width / 2, height - 10)
    instructions = Text(instPt," Area: " + str(area) + " Perimeter: " + str(perimeter))
    instructions.draw(win)
    
    print("Click to End the Program")
    win.getMouse()
    win.close()

def circle():

    width = 400
    height = 400
    win = GraphWin("Circle", width, height)
    
    centerPoint = win.getMouse() 
    pointOnEdge = win.getMouse() 

    X1 = centerPoint.getX()
    Y1 = centerPoint.getY()
    X2 = pointOnEdge.getX()
    Y2 = pointOnEdge.getY()
    
    dis= ((X2 - X1)**2) + ((Y2 - Y1)**2)
    distance= math.sqrt(dis)

    shape = Circle(centerPoint, distance)
    shape.setOutline("black")
    shape.setFill("white")
    shape.draw(win)

    instPt = Point(width / 2, height - 10)
    instructions = Text(instPt,"Distance: " + str(distance))
    instructions.draw(win)
    
    win.getMouse()
    win.close()

def pi2():
    total= 0
    num= -4
    denom = 1
    numTerm= eval(input("Number of Terms in a Series: "))
    for i in range(numTerm):
        num = num * (-1)
        total+= (num / denom)
        denom += 2
    print("Sum: ", total)

def pi():
    total= 1
    denom= 1
    numerator= 2
    numTerm= eval(input("Number of Terms in a Series: "))
    for i in range(numTerm):
        total= total * (numerator/ denom)
        numerator += (i % 2) * 2
        denom += ((i+1) % 2) * 2
    aproxPi= total
    print("Approximation of Pi: ", aproxPi)
