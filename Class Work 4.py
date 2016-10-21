from graphics import *

def moveCircle():
    winHeight= 400
    winWidth=400

    win= GraphWin("Click to move circle", winWidth, winHeight)

    pt= Point(winWidth/2,winHeight/2)
    pt.draw(win)

    circ = Circle(pt,60)
    circ.draw(win)
    circ.setFill("yellow")
    circ.setOutline("red")

    message= Text(Point(winWidth/2, winHeight-10)," ")
    message.draw(win)
    message.setText("Click to move circle")

    for count in range(5):
        mousePt=win.getMouse()
        centerPt=circ.getCenter()
        newX=mousePt.getX()-centerPt.getX()
        newY=moustPt.getY()-centerPt.getY()
        circ.move(newX, newY)

    print()

    message.setText("type a num")
    win.getMouse
    ageBox= Entry(Point(winWidth//2,winHeight-5),5)
    age=ageBox.getText()
    print("Age:", age)
    win.getMouse()
    win.close()
    
