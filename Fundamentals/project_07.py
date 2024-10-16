# Practice:

#Input:
"""
name = input("Enter your name: ")
age = int(input("Enter your age: "))
welcome = print(f"Hello {name} you're {age} years old")
"""
#------------------------------------------------------------------------------#
"""
#Conditional statement:

number = int(input("Enter a number to analize: "))
if number < 0:
    print("Your number es negative")
elif number == 0:
    print("Your number is zero")
else:
    print("Your number is positive")

color = input("Enter a color: 'yellow', 'red', 'green'")


if color.lower() == "yellow":
    print("Wait a minute")
elif color.lower() == "red":
    print("Can't pass")
else:
    print("Move on!")
"""
#------------------------------------------------------------------------------#
"""
#While loop:

number_list = []

while True:
    numbers = int(input("Enter numbers (zero to stop): "))
    if numbers == 0:
        break
    number_list.append(numbers)
print(number_list)


user_number = int(input("Enter numbers to start to count: "))
i = 1
while True:
    print(i)
    i += 1
    if i >= user_number:
        break
"""
#------------------------------------------------------------------------------#
"""
#For:
for numbers in range(1, 11):
    print(numbers)

fruits = ["pera", "manzana", "banano", "piña", "mango"]
for i in fruits:
    print(i, end=", ")
"""

#------------------------------------------------------------------------------#
#Functions:
import math


def area(radius):
    circle_area = math.pi * pow(radius, 2)
    return circle_area

result = area(4)
print(result)

radius = int(input("Enter circle radius: "))
area = lambda radius : math.pi * pow(radius, 2)
print(area(radius))

