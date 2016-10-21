# Lab6.py
# Name 1: Shefali Emmanuel
# Name 2: Joshua Nichols

def nameReverse():
    name= input("Enter your name in first-last order: ")
    nameList= name.split()
    first= nameList[0]
    last= nameList[1]
    username= last + ", " + first
    print(username)

def companyName():
    webAddy= input("Website Address: ")
    nameList= webAddy.split(".")
    domain= nameList[1]
    capDom= domain.capitalize()
    print(capDom)
    
def initials():
    numStd= eval(input("Number of Students: "))
    count = 0
    for i in range(numStd):
        count += 1
        firstN= input("Enter the first name of student " + str(count) + ":")
        print(firstN)
        lastN= input("Enter " + firstN + "'s last name :")
        print(lastN)
        initials= input(firstN + "'s initials are: " + firstN[0] + lastN[0])
        print(initials)

def names():
    for i in range(1):
        nameList= input("List students first and last names seperated by commas: ")
        initialsList= nameList.split(",")
        print("The initials are: ", end="")
        for name in initialsList:
            nameSplit = name.split()
            firstName= nameSplit[0]
            lastName= nameSplit[1]
            firstI = firstName[0]
            lastI = lastName[0]
            initials= firstI + lastI
            print(initials, end=" ")

def third():
    sentNum= eval(input("Number of Sentences: "))
    everyThird = 2
    for i in range(sentNum):
        sentence = input("Sentence: ")
        for j in range(2, len(sentence), 3):

            sentenceThird = sentence[j]
            print(sentenceThird, end="")

def wordCount():
    sentNum = eval(input("Number of sentences: "))
    
    for i in range(sentNum):
        sentence= input("Enter Sentence: ")
        numWords = len(sentence.split())
        print(numWords)

def wordAverage():
    sentNum = eval(input("Number of sentences: "))
    total = 0
    
    for i in range(sentNum):
        sentence= input("Enter Sentence: ")
        words = sentence.split()
        numWords = len(words)
        for j in range(numWords):
            total += len(words[j])
    average = total / numWords
    print(average)

def pigLatin():
    pigLatin = ""
    sentence= input("Enter Sentence: ")
    words = sentence.split()
    for word in words:
        pigLatin += word[1:] + word[0] + "ay "
    print(pigLatin.lower())
    
    
    
            
    
