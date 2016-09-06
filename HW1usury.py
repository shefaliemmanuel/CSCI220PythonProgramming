# Name: Shefali Emmanuel
# usury.py
# CSCI 220 HW1
# Problem: This program will helps everyone realize the true interest
#          rates they will be paying on their loans.
# Certification of Authenticity:
# I certify that this lab is entirely my own work.
# I certidy that this lab is my own work, but I
# discussed it with: Professor Stalvey, Elaina Cole, and Megan Gould.

def principlePaymentPlan():
    print("This program will calculate the principle,", end = " ")
    print("monthly payment total amount paid, and total", end = " ")
    print("interest paid for buying a home or car.")

    #value used for the yearly percentage
    YEARLY_PERCENTAGE = 1200 

    #user input- interest, rate, principal, and months
    #output- monthly payment, total amount paid, and total
    #        interest paid to monitor
    
    #calculate interest
    interest = eval(input("Enter the Interest Rate: "))
    
    #calculate rate
    rate = interest / YEARLY_PERCENTAGE
    print ("Rate: ", rate)

    #calculate principal
    principal = eval(input("Enter the Loan Amount: "))

    #calculate the number of months
    months = eval(input("Enter the Number of Months: "))

    #calculate new monthly payment total
    num = principal *(rate * (1 + rate) ** months)
    denom = ((1+rate)**months-1)

    monthlyPayment= num / denom
    print ("Monthly Payment: ", monthlyPayment)

    #calcuate total amount paid
    totalAmountPaid = monthlyPayment * months
    print ("Total Interest Paid: ", totalAmountPaid)

    #calculate total interest paid
    totalInterestPaid = totalAmountPaid - principal
    print ("Total Amound Paid: ", totalInterestPaid)
                    
