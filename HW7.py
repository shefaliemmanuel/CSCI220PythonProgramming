# bumper.py
# Name: Shefali Emmanuel
# CSCI 220 HW7
# Problem:To create a new typw of bumper car.
# Input: The pseudocode and outline from Professor Stalvey.
# Output: The program creates two circles of different colors and
#         chooses initial random directions for them to move.        
# Certification of Authenticity:
# I certify that this lab is my own work, but I discussed it with:
# Marge Marshall.

from graphics import*
import random
from math import*

#returns a random number between –moveAmount and +moveAmount
def getRandom(moveAmount):
    start= moveAmount * -1
    stop= moveAmount
    return random.randrange(start, stop)
    
#returns Boolean based on the collision of the two balls
def didCollide(ball,ball2):
    didCollide = False
    point= ball.getCenter()
    point2= ball2.getCenter()
    x= point.getX()
    x2= point2.getX()
    y= point.getY()
    y2= point2.getY()
    r= ball.getRadius()
    r2= ball2.getRadius()
    #rightMost= x+r
    #leftMost= x-r
    #topMost= y-r
    #bottomMost= y+r
    #rightMost2= x2+r2
    #leftMost2= x2-r2
    #topMost2= y2-r2
    #bottomMost2= y2+r2
    #if((rightMost < rightMost2) & (rightMost > leftMost2) &
    #   (topMost > topMost2) & (topMost < bottomMost)):
    #    didCollide = True
    if ((abs(x - x2) < (r+r2)) & (abs(y - y2) < (r+r2))):
        didCollide = True
    return didCollide


#returns True if ball hits a vertical wall, False otherwise
def hitVertical(ball,win):
    point= ball.getCenter()
    x= point.getX()
    r= ball.getRadius()
    #            or
    if ((x-r<=0) | (x+r>=400)):
        return True
    else:
        return False

#returns True if ball hits a horizontal wall, False otherwise
def hitHorizontal(ball,win):
    point= ball.getCenter()
    y= point.getY()
    r= ball.getRadius()
    #            or
    if ((y-r<=0) | (y+r>=400)):
        return True
    else:
        return False

#returns a random color 
def randomColor():
    start = 0
    stop = 255
    red = random.randrange(start, stop)
    green = random.randrange(start, stop)
    blue = random.randrange(start, stop)
    return color_rgb(red, green, blue)

def main():

    print(" ")
    
    #establish width of window
    winWidth = 400
    #establish height of window
    winHeight = 400

    #draw the window
    win =GraphWin("Window",winWidth, winHeight)
    win.setBackground("black")
    
    #make the balls
    ball= Circle(Point(30,40), 10.5)
    ball2= Circle(Point(130,140), 10.5)

    #draw the balls
    ball.draw(win)
    ball2.draw(win)

    #fill the balls with random colors
    ball.setFill(randomColor())
    ball2.setFill(randomColor())
    
    #random number between -10 and 10 which is how much x & y changes
    # for each ball
    xDirection= getRandom(10)
    yDirection= getRandom(10)
    x2Direction= getRandom(10)
    y2Direction= getRandom(10)
    
    #different collision options and how the ball should react 
    runs = 0
    while (runs <1000):
        
        ball.move(xDirection, yDirection)
        ball2.move(x2Direction, y2Direction)
        
        if didCollide(ball,ball2):
            xDirection = xDirection * -1
            yDirection= yDirection * -1
            x2Direction= x2Direction * -1
            y2Direction= y2Direction * -1
            ball.setFill(randomColor())
            ball2.setFill(randomColor())
            
        if hitVertical(ball, win):
            xDirection = xDirection * -1
            ball.setFill(randomColor())
            
        if hitHorizontal(ball, win):
            yDirection= yDirection * -1
            ball.setFill(randomColor())

        if hitVertical(ball2, win):
            x2Direction= x2Direction * -1
            ball2.setFill(randomColor())
            
        if hitHorizontal(ball2, win):
            y2Direction= y2Direction * -1
            ball2.setFill(randomColor())
            
        #incrimenting to get 20 runs
        runs = runs + 1
    
    # Wait for another click to exit
    message = Text(Point(200,200),"Click anywhere to quit!")
    message.setTextColor("white")
    message.draw(win)
    
    
    win.getMouse()
    win.close()

main()
