# Name: Shefali Emmanuel
# weightedAverage.py
# CSCI 220 HW5
# Problem: To calculate student grades and averages.
# Input: The text file that contains the file to average the grades.
# Output: The individual and class averages.
# Certification of Authenticity:
# I certify that this lab is my own work, but I discussed it with:
# Zach Pickler and Eduardo Abreu.

def main():
    print("The program will compute and display each student's average "
          "along with their class average.")

    nameOfFile= str(input('what is the name of the file?'))
    #read the file
    file_string = read_file(nameOfFile)
    #list the file
    files_listed = file_listed(file_string)
    class_total = 0
    length_class = 0
    for line in files_listed:
        namesAndGrades,first_names,second_names = get_name_and_numbers(line)
        total = calculate_average(namesAndGrades)
        average = total / 100
        print("{0} {1}'s average: {2}".format (first_names, second_names, average))
        class_total += average
        length_class += 1

    class_average = class_total / length_class
    print(' ')
    print('class average: {0:0.1f}'.format (class_average))

#reading the file
def read_file(nameOfFile):
    infile = open(nameOfFile,"r")
    file_String = infile.read()
    infile.close()
    return file_String

#all of the files listed
def file_listed(file_string):
    files_listed = file_string.split('\n')
    return files_listed

#prints out names and numbers
def get_name_and_numbers(line_string):
    nameAndGrades = line_string.replace('   ',' ')
    namesAndGrades = line_string.split(' ')
    #the student's first name
    first_names = namesAndGrades[0]
    #last names of student's
    second_names = namesAndGrades[1]
    del namesAndGrades[0:2]
    return namesAndGrades,first_names,second_names

#calculates avearges
def calculate_average(average):
    total = 0
    for i in range(1,len(average),2):
        a= int(average[i])
        inputs = i - 1
        b= int(average[inputs])
        total += (a * b)

    return total

main()      
            

                    
