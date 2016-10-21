# triangle.py
# Author: Zelle (pp. 103-04)
# Modified by Pharr to eliminate coordinates
# Name: Shefali Emmanuel
# CSCI 220 HW6
# Problem: To use a function, makeTriangle(p1, p2, p3), to create the
#          triangle.
# Input: The the three points that are used to pass the function.
# Output: To create a distance function that returnst hte Euclidean
#         distance; to create a program that calculates the triangle's
#         area and perimeter. The program will also display the
#         peremiter and area values in the graphics window. 
# Certification of Authenticity:
# I certify that this lab is my own work, but I discussed it with:
# _______.

from graphics import *

def main():
    
    print("To create a distance function that returnst hte Euclidean")
    print("distance; to create a program that calculates the triangle's")
    print("area and perimeter. The program will also display the")
    print("peremiter and area values in the graphics window.") 
    
    winWidth = 400
    winHeight = 400
    
    win = GraphWin("Draw a Triangle", winWidth, winHeight)
    message = Text(Point(winWidth/2, winHeight-10), "Click on three points")
    message.draw(win)

    # Get and draw three vertices of a triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Wait for another click to exit
    message.setText("Click anywhere to quit")
    win.getMouse()
    win.close()

    # program to get points
    points=[]
    for i in range(15):
        clickPt=win.getMouse()
        clickPt.draw(win)
        points.append(clickPt)
        print("Point " + "(" + str(clickPt.getX())+"," +
        str(clickPt.getY()) +")")

    print()

    #displays the Perimeter in the document
    instPt = Point(winWidth/2, winHeight-10, "Perimeter")
    instructions = Text(instPt, "Perimeter")
    instructions.setFill("white")
    instructions.setOutline("white")
    instructions.setSize(36)
    instructions.draw(win)
    
    #displays the Area in the document
    instPt = Point(winWidth/4, winHeight-10, "Area")
 #   message.draw(win), 700
 #   instructions = Text(instPt, "Area")
    instructions.setFill("white")
    instructions.setOutline("white")
    instructions.setSize(36)
    instructions.draw(win)

##def perimeter(tri):
##    area=
##    
##def area(tri):
##    area= 

main()
