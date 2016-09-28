# Lab5.py
# Name 1: Shefali Emmanuel
# Name 2: Bailey Williamson

from graphics import *

def cupConverter():
    # Author: RoxAnn H. Stalvey, modified by Walter Pharr
    # Illustrates getting numeric input through graphics window
    winWidth = 300
    winHeight = 200
    win = GraphWin("Convert cups to milliliters", winWidth, winHeight)

    #Specify the message for the input box
    boxDesc = Text(Point(100, 50), "Input cups: ")
    boxDesc.draw(win)

    #Create the Entry object and set its default text to a number
    #  allowing the user to see what type of value is expected
    inp = Entry(Point(200, 50), 5)
    inp.setText("0")
    inp.draw(win)

    #Create a Text object for outputting the result
    output = Text(Point(150, 150), "")
    output.draw(win)

    #This button isn't necessary, but it makes a nice point for the user
    #  to click.  If you click anywhere in the window, the code reacts
    #  the same way.
    btPtX = winWidth/2
    btPtY = winHeight/2
    button = Text(Point(btPtX, btPtY), "Click")
    button.draw(win)
    border = Rectangle(Point(btPtX-35, btPtY-20), Point(btPtX+35, btPtY+20))
    border.draw(win)

    # Wait for a mouse click
    win.getMouse()

    # Discover intput and convert it to a number
    # If numeric input wasn't needed, simply omit the eval()
    cups = eval(inp.getText())

    #Calculate milliliter equivalent here
    ml= cups * 8 * 29.57

    # Display output and change button
    output.setText("value in milliliters = " + str(ml))
    button.setText("Quit")
    
    # Wait for another click to exit
    win.getMouse()
    win.close()


def target():
    winWidth = 300
    winHeight = 300
    win = GraphWin("Archery Target", winWidth, winHeight)

    # Add code here to get the dimensions and draw the target
    centerPt = Point(winWidth/2, winHeight/2)
    radius= winWidth / 100

    win.getMouse()

    shape = Circle(centerPt, radius * 50)
    shape.setOutline("black")
    shape.setFill("white")
    shape.draw(win)

    shape = Circle(centerPt, radius *40)
    shape.setOutline("black")
    shape.setFill("black")
    shape.draw(win)

    win.getMouse()

    shape = Circle(centerPt, radius * 30)
    shape.setOutline("blue")
    shape.setFill("blue")
    shape.draw(win)

    win.getMouse()
    
    shape = Circle(centerPt, radius * 20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    win.getMouse()
    
    shape = Circle(centerPt, radius * 10)
    shape.setOutline("yellow")
    shape.setFill("yellow")
    shape.draw(win)


    # Wait for another click to exit
    print("Click to End the Program")
    instPt = Point(winWidth / 2, winHeight - 10)
    instructions = Text(instPt, "Click to End the Program ")
    instructions.draw(win)
    win.getMouse()
    win.close()



def triangle():
    winWidth = 500
    winHeight = 500
    win = GraphWin("Draw a Triangle", winWidth, winHeight)

    ptA = win.getMouse()
    ptB = win.getMouse()
    ptC = win.getMouse()

    shape = Polygon(ptA, ptB, ptC)
    shape.setOutline("black")
    shape.draw(win)

    dx1= ptA.getX() - ptB.getX()
    dy1= ptA.getY() - ptB.getY()

    dx2= ptB.getX() - ptC.getX()
    dy2= ptB.getY() - ptC.getY()

    dx3= ptC.getX() - ptA.getX()
    dy3= ptC.getY() - ptA.getY()

    a = ((dx1 ** 2) + (dy1 ** 2)) ** (1/2)
    b = ((dx2 ** 2) + (dy2 ** 2)) ** (1/2)
    c = ((dx3 ** 2) + (dy3 ** 2)) ** (1/2)

    s = (a + b + c) / 2
    peri = a + b + c
    area = (s*(s-a)*(s-b)*(s-c))**(1/2)

    instPt= Point(winWidth / 2, winHeight -10)
    instructions= Text(instPt, "Perimeter: " + str(peri))
    instructions.draw(win)

    instPt= Point(winWidth/ 2, winHeight - 30)
    instructions= Text(instPt, "Area: " +str(area))
    instructions.draw(win)

    win.getMouse()
    win.close()

def colorShape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    #create window
    winWidth = 400
    winHeight = 400
    win = GraphWin("Color Shape", winWidth, winHeight)
    win.setBackground("white")

    #create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(winWidth/2, winHeight-20), msg)
    inst.draw(win)

    #create circle in window's center
    shape = Circle(Point(winWidth/2, winHeight/2 - 30), 50)
    shape.draw(win)

    #redTexPt is 50 pixels to the left and forty pixels down from center
    redTextPt = Point(winWidth/2 - 50, winHeight/2 + 40)
    redText = Text(redTextPt, "Red: ")
    redBox = Entry(Point(winWidth/2 - 10, winHeight/2 + 40), 5)
    redBox.draw(win)
    boxDesc = Text(Point(100, 50), "Input cups: ")
    boxDesc.draw(win)

    redText.setTextColor("red")
    redText.draw(win)


    #greenTextPt is 30 pixels down from red
    greenTextPt = redTextPt.clone()
    greenTextPt.move(0,30)
    greenText = Text(greenTextPt, "Green: ")
    greenText.setTextColor("green")
    greenText.draw(win)


    #blueTextPt is 60 pixels down from red
    blueTextPt = redTextPt.clone()
    blueTextPt.move(0,60)
    blueText = Text(blueTextPt, "Blue: ")
    blueText.setTextColor("blue")
    blueText.draw(win)

##    #display rgb text
##    redText.draw(win)
##    greenText.draw(win)
##    blueText.draw(win)

    win.getMouse()
    red = int(redBox.getText())
    print(red)
    print("Click to End the Program")
    win.getMouse()
    win.close()
    
def main():
    cupConverter()
    target()
    triangle()
    colorShape()

def anotherSeries():

    numTerms = eval(input("Number of terms? "))
    val = 0
    for i in range (numTerms):
        mod= i % 3
        answer= mod *2 +2
        val += answer
    print(val)

def anotherSeriesPartner():
    numTerms = eval(input("Number of terms? "))
    val = 1
    numer= 1
    denome=3

    print(numer, "/", denome, ",", end = "")
    
    for i in range (numTerms):
        numer += 2
        denome *= 2

        print(numer, "/", denome, ",", end = "")
        
        val *= numer/ denome
        print(val)
        
        







