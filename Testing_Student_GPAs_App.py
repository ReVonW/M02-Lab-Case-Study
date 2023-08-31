#ReVon Wilson
#Testing_Student_GPAs
#This app will accept the names of students and GPAs and tests if the student qualifies for either the Dean's List, the Honor Roll. or neither.

#Ask for the students last name
lastName = input("Enter last name:" )
#Check if the last name was entered as 'ZZZ' if true quit proessing
while lastName == "ZZZ":
#Ask user to enter their first name
    firstName = input("Enter first name: ")
#Ask user to input their GPA
gpa = float(input("Enter GPA: "))
#Test if the students GPA is 3.5 or greater, if so they have made the Dean's List.
if gpa >=3.5:
    print("{} {} has made the Dean's List.".format(firstName, lastName))
#Test if student GPA is 3.25 or greater, if so they have made Honor Roll
else:
    if gpa >=3.25:
        print("{} {} has made the Honor Roll.".format(firstName, lastName))
lastName = input("\nEnter last name: ") 
#Quit processing student records if the last name entered is 'ZZZ'