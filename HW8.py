# jumpingJack.py
# Name: Shefali Emmanuel
# CSCI 220 HW7
# Problem: To create a simulation of Jack consisting of a stick figure
#          and three buttons: start, stop, and quit.
# Input: The users will click inside to window to initiate the program.
# Output: A jumping jack that follows the button instructions.       
# Certification of Authenticity:
# I certify that this lab is my own work, but I discussed it with:
# Marge Marshall.

from graphics import*
import time

def wasClicked(pt, rect):
    #set values to false
    xInRange= False
    yInRange= False
    #get points
    if pt != None:
        point1= rect.getP1()
        point2= rect.getP2()
        x1= point1.getX()
        x2= point2.getX()
        y1= point1.getY()
        y2= point2.getY()
        #if else statements for range
        if x2 > x1:
            if pt.getX() <= x2 and x1 <= pt.getX():
                xInRange= True
        else:
            if pt.getX() >= x2 and x1 >= pt.getX():
                xInRange= True
        if y2 > y1:
            if pt.getY() <= y2 and y1 <= pt.getY():
                yInRange= True
        else:
            if pt.getY() >= y2 and y1 >= pt.getY():
                yInRange= True
            
    return (xInRange and yInRange)

def main():

    print(" ")
    
    #establish width of window
    winWidth = 400
    #establish height of window
    winHeight = 400

    #draw the window
    win =GraphWin("Window",winWidth, winHeight)
    win.setBackground("black")
    
    #make the body
    ball= Circle(Point(200,100), 10.5)
    bod= Line(Point(200,100), Point(200,200))
    leftLeg= Line(Point(150,250), Point(200,200))
    rightLeg= Line(Point(250,250), Point(200,200))
    leftArm= Line(Point(150,150), Point(200,150))
    rightArm= Line(Point(250,150), Point(200,150))
    leftLeg2= Line(Point(225,275), Point(200,200))
    rightLeg2= Line(Point(175,275), Point(200,200))
    leftArm2= Line(Point(225,200), Point(200,150))
    rightArm2= Line(Point(175,200), Point(200,150))
    leftLeg3= Line(Point(225,275), Point(200,200))
    rightLeg3= Line(Point(175,275), Point(200,200))
    leftArm3= Line(Point(250,100), Point(200,150))
    rightArm3= Line(Point(150,100), Point(200,150))
    
    #draw the body
    ball.draw(win)
    bod.draw(win)
    leftLeg.draw(win)
    rightLeg.draw(win)
    leftArm.draw(win)
    rightArm.draw(win)
##    leftLeg2.draw(win)
##    rightLeg2.draw(win)
##    leftArm2.draw(win)
##    rightArm2.draw(win)
##    leftLeg3.draw(win)
##    rightLeg3.draw(win)
##    leftArm3.draw(win)
##    rightArm3.draw(win)
    
    #fill the body
    ball.setFill("light blue")
    bod.setFill("light blue")
    leftLeg.setFill("light blue")
    rightLeg.setFill("light blue")
    leftArm.setFill("light blue")
    rightArm.setFill("light blue")
    leftLeg2.setFill("light blue")
    rightLeg2.setFill("light blue")
    leftArm2.setFill("light blue")
    rightArm2.setFill("light blue")
    leftLeg3.setFill("light blue")
    rightLeg3.setFill("light blue")
    leftArm3.setFill("light blue")
    rightArm3.setFill("light blue")

    #moves
    move1= [leftLeg,rightLeg,leftArm,rightArm]
    move2= [leftLeg2,rightLeg2,leftArm2,rightArm2]
    move3= [leftLeg3,rightLeg3,leftArm3,rightArm3]
    moveList= [move1, move2, move1, move3]

    #rectangles
    rectangle = Rectangle(Point(75,325), Point(125,375))
    rectangle.setFill("light pink")
    rectangle.draw(win)

    rectangle1 = Rectangle(Point(175,325), Point(225,375))
    rectangle1.setFill("light pink")
    rectangle1.draw(win)
    
    rectangle2 = Rectangle(Point(275,325), Point(325,375))
    rectangle2.setFill("light pink")
    rectangle2.draw(win)
    
    #text messages to display    
    message = Text(Point(100,350),"Start!")
    message.setTextColor("white")
    message.draw(win)

    message1 = Text(Point(200,350),"Stop!")
    message1.setTextColor("white")
    message1.draw(win)
    
    message2 = Text(Point(300,350),"Quit!")
    message2.setTextColor("white")
    message2.draw(win)
    
    message3 = Text(Point(200,50),"Jumping Jacks!")
    message3.setTextColor("white")
    message3.draw(win)

    #get the mouse
    click = win.getMouse()

    #jump functions
    jump = wasClicked(click, rectangle)
    jump1 = wasClicked(click, rectangle1)
    jump2 = wasClicked(click, rectangle2)

    #set x to 1
    x = 1
    #wile loop for buttons
    while not jump2:
        if jump and not jump1:
            for line in moveList[(x-1)%4]:
                line.undraw()
            moveList [x % 4]
            for line in moveList[x%4]:
                line.draw(win)
            time.sleep(2)

            x += 1
        click = win.checkMouse()
        if click != None:
            jump = wasClicked(click, rectangle)
            jump1 = wasClicked(click, rectangle1)
            jump2 = wasClicked(click, rectangle2)
            
    win.close()

main()
