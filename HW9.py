# Hangman.py
# Name: Shefali Emmanuel
# CSCI 220 HW9
# Problem: Write a program to support the children's spelling game
#           hangman.
# Input: The user will input a letter of their choice.
# Output: A hangman visual along with the letters in the word,
#           the letters that were incorrect.     
# Certification of Authenticity:
# I certify that this lab is my own work, but I discussed it with:
# Eduardo, Matt, Megan Landun.

from graphics import*
import random

#set above everything so that these variables can be accsesed easily
entry1 = Entry(Point(120, 300),5)
message3 = Text(Point(200,50),"Let's play CofC Sorority Hangman!")
message3.setTextColor("white")

#import text file
def hangman():
    infile = open("wordlist.txt","r")
    file_String = infile.read()
    return file_String.split()

#create random word choosing generator    
def randomWord():
    fileList = hangman()
    word= fileList[random.randint(0, (len(fileList)-1))]
    return word

#add "_" per letter and print to screen
def guessed(word,win):
    print(word)
    length= len(word)
    guessList= []
    
    for i in range(length):
        guessList.append("_ ")
        
    finalWord = buildFinalWord(guessList)
    print(finalWord)

    tries=0
    #will keep all the wrong letters guessed
    lettersGuessed = []

    #make the body
    gallows= Rectangle(Point(300,264),Point(289,79))
    gallows1= Rectangle(Point(189,70),Point(299,84))
    ball= Circle(Point(200,100), 10.5)
    bod= Line(Point(200,100), Point(200,200))
    leftLeg= Line(Point(150,250), Point(200,200))
    rightLeg= Line(Point(250,250), Point(200,200))
    leftArm= Line(Point(150,150), Point(200,150))
    rightArm= Line(Point(250,150), Point(200,150))
    
    #list of hangman parts to work everytime user guesses a wrong letter
    hangingman=[gallows1, ball, bod, leftLeg, rightLeg, leftArm, rightArm]

    #fill the body
    gallows.setFill("light blue")
    gallows.setOutline("light blue")
    gallows1.setFill("light blue")
    gallows1.setOutline("light blue")
    ball.setFill("light blue")
    bod.setFill("light blue")
    leftLeg.setFill("light blue")
    rightLeg.setFill("light blue")
    leftArm.setFill("light blue")
    rightArm.setFill("light blue")

    #messages to be printed to the screen
    message4 = Text(Point(200,300)," ")
    message4.setTextColor("white")
    message4.draw(win)

    message6 = Text(Point(200,350),"wrong letters")
    message6.setTextColor("white")
    message6.draw(win)

    message7 = Text(Point(100,350),"Wrong Letters:")
    message7.setTextColor("white")
    message7.draw(win)
    message4.setText(finalWord)

    while (tries < 7) and (correctWord(finalWord,word)== False):
        
##      coded= input("Enter a letter: ")
        win.getMouse()
        coded= entry1.getText()
        entry1.setText('')
            #demorgans law
        if not ((len(coded) > 1) or (coded in lettersGuessed) or not(coded in word)):
    
        
            for j in range(len(word)):
                if word[j] == coded:
                    guessList[j] = coded
            print("Correct!")
                    
        else:
            lettersGuessed.append(coded)
            print("You have entered the wrong letter or have already entered this letter.")
            hangingman[tries].draw(win)
            tries += 1
            print("try again")

        print(lettersGuessed)
        message6.setText(lettersGuessed)
        finalWord= buildFinalWord(guessList)
        print (finalWord)
        message4.setText(finalWord)
        
    #what to print to the diaplay if player guesses correct
    if (correctWord(finalWord,word)== True):
        print("Great Job! You figured out the word!")
        message3.setText("Great Job! You figured out the word!")
        
        #what to print to the diaplay if player guesses incorrect
    else:
        print("Horrible Job! You did not figured out the word!")
        message3.setText("Horrible Job! You did not figured out the word!")
    return finalWord

#final word formula
def buildFinalWord(guessList):
        finalWord= (''.join(guessList))
        return finalWord
    
 # the correct word formula       
def correctWord(finalWord, word):
    if finalWord == word:
        return True
    
    else:
        return False

def main():
    #establish width of window
    winWidth = 400
    #establish height of window
    winHeight = 400

    #draw the window
    win =GraphWin("Window",winWidth, winHeight)
    win.setBackground("black")

    #set the gallows and draw it in the display
    gallows= Rectangle(Point(300,280),Point(289,79))
    gallows.setFill("light blue")
    gallows.draw(win)

    #set the base and draw it in the display
    base= Rectangle(Point(315,270),Point(275,280))
    base.setFill("light blue")
    base.setOutline("light blue")
    base.draw(win)
    
    #drawing the messages to the display
    message3.draw(win)
    entry1.draw(win)

    #text messages to the display
    message8 = Text(Point(50,300),"Enter a letter:")
    message8.setTextColor("white")
    message8.draw(win)

    rectangle2 = Rectangle(Point(275,325), Point(325,375))
    rectangle2.setFill("light pink")
    rectangle2.draw(win)

    message2 = Text(Point(300,350),"Submit!")
    message2.setTextColor("white")
    message2.draw(win)
    
    #how to get the main function to run through the main
    guessed(randomWord(),win)

    win.getMouse()
    win.close()
    
main()
