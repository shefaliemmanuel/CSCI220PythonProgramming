from graphics import *
import time

#read pages 108-109

def main():
    win = GraphWin("My First Window", 500, 300)
                                    #width & height in pixels
    win.setBackground("purple") #methord
    time.sleep(.2)

    colors= ["red", "blue", "green", "magenta", "black"] #list has to be bracketed

    for i in range(5):
        for color in colors:
            win.setBackground(color)
            time.sleep(.2)
    print("Done")

    ptA= Point (40,50)
    cir= Circle (ptA,20)
    cir.setFill("yellow")
    cir.draw(win)
    time.sleep(.4)
    cir.move(10,-15)

def main2():
    winHeight = 400
    winWidth = 400

    win= GraphWin("Click to move circle", winWidth, winHeight)

    pt= Point(winWidth/2, winHeight/2)
    pt.draw(win)

    circ= Circle(pt, 60)
    circ.draw(win)
    circ.setFill("yellow")
    circ.setOutline("red")

    message= Text(Point(winWidth/2, winHeight-10), "")
    message.draw(win)
    message.setText("Click on window to move circle to that point")

    for count in range(5):
        mousePt = win.getMouse()
        centerPt = circ.getCenter()
        newX = mousePt.getX() - centerPt.getX
        newY = mouse.Pt.getY() - centerPt.getY
        circ.move(newX, newY)

    message.setText("Type a number")
    ageBox= Entry(Point(winWidth//2, winHeight - 30), 5)
    age.Box.draw(win)
    win.getMouse()
    age= ageBox, getText()
    print("Age: ",age)
    win.getMouse()
    win.close()
