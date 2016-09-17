# Name: Shefali Emmanuel
# cdTime.py
# CSCI 220 HW2
# Problem: This program will helps everyone realize the true interest
#          rates they will be paying on their loans.
# Certification of Authenticity:
# I certify that this lab is entirely my own work.
# I certidy that this lab is my own work, but I
# discussed it with: Kendall Dunn, Alex Giarrocco, and Megan Gould

def cdTime():
    print("This program calculates the total time on a CD.")

    #total number of CD's
    totalCd= eval(input("Number of CD's: "))
    totalMinOfAllCd= 0
    totalSecOfAllCd= 0

    #create a loop for the total cd's
    for num in range(totalCd):

        #set values to 0
        sumMin= 0
        sumSec= 0
        
        #find out how many tracks are on the cd
        trackNum= eval(input("How many tracks are on the CD "
                             + str(num + 1) + "? " ))

        for i in range(trackNum):
            #find out how many minutes are on a track
            mins= eval(input("How many minutes are on track "
                             + str(i + 1) + "? "))
            #find out the amount of seconds on a track
            secs= eval(input("How many seconds are on track "
                             + str(i + 1) + "? "))
            print()

            # sumMin= sumMin + mins
            sumMin += mins
            #sumSec= sumSec + secs
            sumSec += secs
            
            print()
            
        #turning second values in to minute values by dividing by 60
        extraMin= sumSec // 60
        #making the value become second values by dividing by 60
        totalSecOfCd= sumSec % 60
        #find the total minutes on the cd
        totalMinOfCd= (sumMin + extraMin)


          
        #print out the total time of all the cd's added together
        print("CD " + str(num + 1) + " Total time: "
              + str(totalMinOfCd) + " minutes "
              + str(totalSecOfCd) + " seconds ")
        #totalMinOfAllCd= totalMinOfAllCd + totalMinOfCd
        totalMinOfAllCd += totalMinOfCd
        #totalSecOfAllCd= totalSecOfAllCd+ totalSecOfCd
        totalSecOfAllCd += totalSecOfCd

    #calculating the total minutes as a whole number 
    totalMin= totalSecOfAllCd // 60
    #calculating the total minutes left also known as the remainder
    totalMinRemainder= totalSecOfAllCd % 60
    #calculate the total minutes of all cd's       
    totalMinOfAllCd += totalMin
    print()
        
    numWholeHours = totalMinOfAllCd // 60
    #print("Number Hours: ", numWholeHours)

    #turning second values in to minute values by dividing by 60
    extraMinutes = (totalMinOfAllCd % 60)
    #print("Total Minutes:", extraMinutes)

    leftOverMins = totalMinOfAllCd - (numWholeHours * 60)
    #print("Total Seconds: ", totalSecOfAllCd)


    extraHours = totalMinOfAllCd // 60
    #making the value become second values by dividing by 60
    hours = extraHours % 60
    #final print statement expressing the total time of all Cds together
    print("Total Time of all CDs: " + str(numWholeHours) + " hours "
      + str(extraMinutes) + " minutes "
      + str(totalMinRemainder) + " seconds ")
            
cdTime()

    
                    
