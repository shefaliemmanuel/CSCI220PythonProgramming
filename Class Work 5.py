def main():
    name= input("Enter your full name: ")
    nameList = name.split()
    first= nameList[0]
    middle= nameList[1]
    last= nameList[2]
    userName= first[0] + middle[1] + last[:8]
    email= userName.lower()
    email=userName + "g.cofc.edu"

    print("\nUsername is: " + userName)
    print("Email: " + email)

def manipulateDate():
    months= ["Jan", "Feb", "Mar", "Apr", "May", "June",
             "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
    date= input("Enter date in form mm/dd/yyyy: ")
    dateList= date.split()
    print("dateList: ", dateList)

    monthNum= (intdateList[0])
    print(month[monthNum-1])

    longDate= months[monthNum-1] + "" + dateList[1] + ", " + dateList[2]
    print("\nDate is: " + longDate)

def kindOfFile():
    fileContents= "Alex\nJulia\nAnne\nJacl"
    print(fileContents)
    lines= fileContents.split("\n")
    print(lines)

def readFileExample():
    outfileName= "averages.txt"
    infile= open("data.txt","r")
    outfile= open(outfileName, "w")
    counter= 1
    for line in infile():
        firstInitial = line[0]
        print(firstInitial)
        lastInitial= line[-2] #because the last letter always has a /n
        print(lastInitial)
        userName= firstInitial + lastInitial.upper() #this is a string
        userName+= str(counter) #turn this into a string
        print(userName)
        counter += 1

    for line in infile():
        names = line.split()
        userName = names[0] [1] +names[1] [:4].lower()
        userName += string(len(names[1]))
        print(username)

    grandTotal=0
    for line in infile:
        nums= line.split()
        lineTotal= 0
        for numStr in nums:
            lineTotal += eval (numStr)
        grandTotal += lineTotal
        print("Grand Total:" + str(lineTotal))
    print("Grand total: "+ str(grandTotal))

    for line in infile:
        parts= line.split()
        grades = part[1:]
        total= 0
        for gradeStr in grades:
            total+= eval(gradeStr)
        avg= total/len(grades)
        print(parts[0] + ": " + str(avg))
            
    print("Done")
    
