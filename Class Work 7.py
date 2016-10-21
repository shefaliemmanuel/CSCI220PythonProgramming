import math

def circArea(rad):
    area= math.pi * rad ** 2
    return area

def rectArea(length, width):
    area= length * width
#         **length and width are the parameters
    return area

def calcAverage(nums):
    # nums are the parameter
    total = 0
    for num in nums:
        total += num
    avg= total/ len(nums)
    return avg

#VOID FUNCTION
def writeAverage(nums, filename):
    total = 0
    for num in nums:
        total += num
    avg= total/ len(nums)
    outfile = open(file, "w")
    print(avg, file= outfile)
    outfile.close()
    print("Data written to: " + filename)

def changeList(values,value):
    # parameters= values and value
    values.append(value)
    

def main():
    print("Area if rad = 10 " + str(circArea(10)))

    area= circArea(3)
    print("Area of rad= 3 " + str(area))
    
    rArea = rectArea(3,5)
    print("Area of l= 3, w= 5: " + str(area))

    rArea = rectArea(4,6)
#                   ** argument 4,6    
    print("Area of l= 4, w= 6: " + str(area))

    average= calcAverage([70, 80, 90, 100, 100])
    print("Avg [70, 80, 90, 100, 100]: "+ str(average))

    writeAverage([3,5,7], "avg.txt")

    names= ["Alex", "Jayse", "Megan"]
    print(names)
    changeList(names, "Matt")
    #         arguments are names an matt
    print(names)
    
main()
