# SalesTestDriver.py
# Author: Pharr
# Name: Shefali Emmanuel
# CSCI 220 HW11
# Problem:To write a class that encapsulates data for a sales person.
# Input: A Class SalesPerson has an ID number (int), a name (string),
#           and a list of sales (float). It provides a constructor
#           __init__ that initializes ID and name, and initializes the
#       list of sales to an empty list.  Member methods for SalesPerson.
# Output: To create a main method that inputs the name of the file from
#           which the sales information is to be read, instantiates an
#           object of type SalesForce, invokes the SaleForce getData()
#           method with the file name, invokes the SaleForce quotaReport()
#           method with a quota amount, invokes the SaleForce topSalesPerson()
#           method and invokes the SalesForce individualSales() method a
#           couple of times.
# Certification of Authenticity:
# I certify that this lab is my own work, but I discussed it with:
# Marge.
# SalesTestDriver - creates a SalesForce object and uses it
# to determine aspects of the sales force.

from SalesForce import SalesForce
from SalesPerson import SalesPerson

def main():
    theSalesForce = SalesForce()
    theSalesForce.addData("salesdata.txt")
    
    print ("Quota report:")
    theSalesForce.quotaReport(750)
    print ("\n************************\n")

    topSales = theSalesForce.topSalesPerson()
    print ("Top sales person:")
    print (topSales)
    print ("\n************************\n")
    
    theSalesForce.individualSales(123)
    print ()
    theSalesForce.individualSales(999)
    print ()
    theSalesForce.individualSales(456)
    print ()
    theSalesForce.individualSales(345)

main()
