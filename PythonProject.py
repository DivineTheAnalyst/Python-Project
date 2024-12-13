#Part 1: Working with Data types
#Integers and Float
num1 = 81 #integer
num2 = 2 #float

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1/num2
floor_division = num1 // num2
print(floor_division)
modulus = num1 % num2
print(modulus)
exponentiation = num1**num2

#Strings
firstname = "Ijeawele"
lastname = "Nkwocha"

#Concatenation
fullname = firstname + " " + lastname
print(fullname)

#Repetition
repeat = 5
repetition = fullname * repeat
print(repetition)

#indexing
print(fullname[5])

uppercase = fullname.upper() #using .upper() function
print(uppercase)

lowercase = fullname.lower() #using .lower() function
print(lowercase)

replace = firstname.replace("Ijeawele", "Divine")
print(replace)

find = fullname.find("w", 5)
print(find)

#Lists
holidays = ['easter', 'christmas', 'new year', 'independence', 'workers', 'children']

#indexing
print(holidays[2])

#slicing
print(holidays[1:3])

#appending
holidays.append('teacher')
print(holidays[1:])

#deleting
holidays.remove('workers')
print(holidays[1:])

#operators
weather = ['summer', 'winter']

holidayweather = holidays + weather  #Concatenation
print(holidayweather)

print(weather * 3)  #Repetition

print('april' in holidays)  #in operator

print('summer' not in weather) #not in operator

#Part 2: Practicing Comparison and Logical Operators
num3 = 80
num4 = 34.59
word = "apple"
word2 = "orange"

if num3 == num4:   #equal to operator
    print('equal')
else:
    print('not equal')

if num3 > num1:  #greater than operator
    print('yay')
else:
    print('ugh')

if num1 >= num3 and num4 <= num2:   #and logical operator
    print('wow')
elif word == word2 or firstname != lastname: #or logical operator
    print('interesting')
elif not firstname == lastname:  #not logical operator
    print('proceed')

#Part 3: Mini-Project
FirstName = input('First Name: ')
LastName = input('Last Name: ')
age = int(input('Year of Birth: '))
job_role = input('What job role are you interested in? ')
skills = list(input('What skills do you have for this role?'))
experience = int(input('How many years have you worked in this field? '))


print("Hello", FirstName + " " + LastName, "Thank you for taking your time to apply for a", job_role, "role.")

if experience < 1:
    print("Unfortunately, you do not meet the criteria for this role.")
elif len(skills) <=3:  #if the number of skills less than or equal to 3
    for skill in skills:  #to ensure the candidate has required skills
        if skill == "%ubernete%" and skill == "%erraform%":
            print("You are qualified")
    print("You don't have the required skills")
elif  age > 2006:
    print("Sorry you are too young to apply")
elif job_role != "DevOps%": #to make sure only DevOps applications are processed
    print("We don't have any available openings for this role right now.")
else:
    print("You can move forward with the application")

#A brief reflection of what I learned for each data type and operator
'''
The integer data type is used to define whole number variables.
The float data type is used to define decimal numbers
The string data type is used to define words and letters
The boolean data type is used to define true or false values
The and logical operator ensures all comparisons are true before printing TRUE
The or logical operator ensures just one comparison to be true before printing TRUE
The + operator adds numbers and concatenates strings
The - operator subtracts
The * multiplies numbers with each other and carries out repetition with strings
The / operator divides numbers
The // operator does floor division which outputs the whole number from a decimal number and discards the rest
The % operator outputs the remainder value when division is done between an improper fraction
The % operator can also be used in strings to create allowances for similar values
'''

