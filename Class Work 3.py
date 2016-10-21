from graphics import *
import time

def main():
    win= GraphWin ("My first window", 500,300)
    win.setBackground("purple")
 ##   time.sleep(.2)

   # colors = ["red", "blue", "magents"]

    #for i in range (5):
     #   for color in colors:
      #      win.setBackground(color)
       #     time.sleep(.2)

    ptA=Point(50,100)
    cir = Circle(ptA,20)
    cir.setFill("pink")
    cir.draw(win)
    for i in range (20):
        time.sleep(.2)
        cir.move(10,-15)
        time.sleep(.5)
        cir.move(10,15)
   
