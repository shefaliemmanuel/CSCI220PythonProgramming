#Sales Person class
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
class SalesPerson():

    # initializes ID and name, and initializes the list of sales to an empty list
    def __init__(self, ID, name):
        self.ID = ID
        self.name= name
        self.sales = []
        
    # getter methrod for ID
    def getID(self):
        return self.ID
    
    # getter methrod for name
    def getName(self):
        return self.name
        
    # setter method for name
    def setName(self,name):
        self.name= name
        
    # enters the parameter value into the list of sales       
    def enterSale(self, aSale):
        self.sales.append(aSale)
        
    #returns Salesperson's sum of total sales
    def totalSales(self):
        total=0
        for i in self.sales:
            total += i
        return total

    #returns a list of all sales
    def getSales(self):
        newList= []
        for i in self.sales:
            newList.append(i)
        return newList

    # a Boolean method that returns True if the total sales
    # meet or exceed the quota provided, and False if not
    def metQuota(self, quota):
        total = self.totalSales()
        if total >= quota:
            return True
        else:
            return False

    # that compares this Salesperson (self) to another
    # (provided as a parameter) based on the values of
    # their total sales amounts.      
    def compareTo(self, otherPerson):
        if self.totalSales() < otherPerson.totalSales():
            return -1
        if self.totalSales() > otherPerson.totalSales():
            return 1
        
        else:
            return 0

    # method that displays the ID, name, and total sales       
    def __str__(self):
        return (str(self.ID)) + " " + (self.name) + " " +  (str(self.totalSales()) )
