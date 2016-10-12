# Name: Shefali Emmanuel
# fallGreeting.py
# CSCI 220 HW4
# Problem: This program will output a jack-o-lantern as well as a
#            flashing.
#           sign saying "Happy Fall!"
# Input: Code will be inputed as well as mouse clicks once the program
#       is running
# Output: The mesages, "Happy Fall" and "Click anywhere to close," as
#         well as the image of a jack-o-lantern.
# Certification of Authenticity:
# I certify that this lab is my own work, but I
# discussed it with: Megan Gould and Zach Pickler.

from graphics import *

def fallGreeting():
    print("This program outputs the RMS average and harmonic mean.")

    #set the window
    win = GraphWin("Circle", 800,800)
    win.setBackground ("black")
    #set the window's width
    width = win.getWidth()
    #set the window's height
    height = win.getHeight()

    #creates the rectangle of the jack-o-lantern
    rec= Rectangle(Point(360,300),Point(430,100))
    #fill the rectangle dark green
    rec.setFill("dark green")
    #draw the rectangle
    rec.draw(win)

    #creates the circle of the jack-o-lantern
    circle = Circle(Point(400,400),200)
    #fill the rectangle dark orange
    circle.setFill("dark orange")
    #draw the circle
    circle.draw(win)
    
##   points=[]
##    for i in range(15):
##        clickPt=win.getMouse()
##        clickPt.draw(win)
##        points.append(clickPt)
##        print("Point " + "(" + str(clickPt.getX())+"," +
##        str(clickPt.getY()) +")")
##
##    print()

    #creates the right eye of the jack-o-lantern
    rightEye= Polygon(Point(500,380), Point(450,330), Point(420,380))
    #outline the eye black
    rightEye.setOutline("black")
    #fill the eye black
    rightEye.setFill("black")
    #draw eye
    rightEye.draw(win)

    #creates the left eye of the jack-o-lantern
    leftEye= Polygon(Point(300,380), Point(350,330), Point(380,380))
    #outline the eye black
    leftEye.setOutline("black")
    #fill the eye black
    leftEye.setFill("black")
    #draw eye
    leftEye.draw(win)

    #creates the nose of the jack-o-lantern
    nose=Polygon(Point(370,440), Point(400,400), Point(430,440))
    nose.setOutline("black")
    nose.setFill("black")
    #draw nose
    nose.draw(win)

    #creates the mouth of the jack-o-lantern
    mouth = Oval(Point(300,450),Point(500,550))
    mouth.setOutline("black")
    mouth.setFill("black")
    #draw mouth
    mouth.draw(win)
    
    #creates the lip of the jack-o-lantern
    mouth_lip = Rectangle(Point(300,450),Point(500,500))
    mouth_lip.setOutline("dark orange")
    mouth_lip.setFill("dark orange")
    mouth_lip.draw(win)
    
    #creates the one of the teeth of the jack-o-lantern
    tooth1 = Rectangle(Point(350,500),Point(375,525))
    tooth1.setOutline("dark orange")
    tooth1.setFill("dark orange")
    tooth1.draw(win)

    #creates the one of the teeth of the jack-o-lantern
    tooth2 = Rectangle(Point(450,500),Point(425,525))
    tooth2.setOutline("dark orange")
    tooth2.setFill("dark orange")
    tooth2.draw(win)

    #displays Happy Fall in the document
    instPt = Point(385, 700)
    instructions = Text(instPt, "Happy Fall !!!")
    instructions.setFill("white")
    instructions.setOutline("white")
    instructions.setSize(36)
    instructions.draw(win)

    # provides the tooth that flickers                       
    for i in range(10):
        tooth3 = Rectangle(Point(387,550),Point(412,525))
        tooth3.setOutline("red")
        tooth3.setFill("red")
        tooth3.draw(win)
        time.sleep(.5)
        tooth3 = Rectangle(Point(387,550),Point(412,525))
        tooth3.setOutline("black")
        tooth3.setFill("black")
        tooth3.draw(win)
        time.sleep(.5)

    #displays Click to close program in the document
    instructions.undraw()
    instructions = Text(instPt, "Click to close program.")
    instructions.setFill("white")
    instructions.setOutline("white")
    instructions.setSize(36)
    instructions.draw(win)
     
    win.getMouse()
    win.close()
fallGreeting()
                    
