#Sales Force
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
from SalesPerson import *

class SalesForce:

    # maintains a list of SalesPerson objects
    def __init__(self):
        self.list= []
        
    # inputs information for all salespersons from that file
    def addData(self, filename):
        f= open(filename, 'r')
        for line in f:
            variables= line.split()
            ID= eval(variables[0])
            name= variables[1] + " " + variables[2]
            sales= []
            for i in variables[3:]:
                sales.append(eval(i))
            temp= SalesPerson(ID, name)
            for i in sales:
                temp.enterSale(i)
            self.list.append(temp)

    #  prints each salesperson's ID, name and total sales and whether or
    # not the salesperson met the sales quota.       
    def quotaReport(self, quota):
        for x in self.list:
            ID= x.getID()
            name= x.getName()
            totalSales= x.totalSales()
            metQuota= x.metQuota(quota)
            final= (str(ID) + " " + name + " " + str(totalSales) + " " + str(metQuota))
            print(final)
            
    # returns the Salesperson object representing the individual with the
    # highest sales amount
    def topSalesPerson(self):
        topSalesPerson = self.list[0]
        for i in self.list:
            if (topSalesPerson.compareTo(i) == 0):
                topSalesPerson= i
            elif (topSalesPerson.compareTo(i) == -1):
                topSalesPerson= i
                
        return topSalesPerson
    
    # prints the sales record (all of his sales) and the total of his sales
    # for the employee with the ID specified            
    def individualSales(self, ID):
        salesPerson = None
        for i in self.list:
            if i.getID() == ID:
                salesPerson = i
        if salesPerson == None:
            print("Not Found")
        else:
            sales= str(salesPerson.getSales())
            totalSales= str(salesPerson.totalSales())
            print(sales, totalSales)
            
