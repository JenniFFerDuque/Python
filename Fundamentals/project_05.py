# Functions practice:

#WAP to calculate MCD:
def MCD(dividend, divider):
    rest = dividend  % divider
    while rest != 0:
        rest = dividend % divider
        dividend = divider
        divider = rest
    return dividend

MCD_Calculated = MCD(28761579, 412776)
print(f"MCD: {MCD_Calculated}")

#-------------------------------------------------------------------------------#
#WAP to calculate mcm
def MCM(dividend, divider):
    total = dividend*divider
    absolute_value = abs(total)
    mcm = absolute_value // MCD(dividend, divider)
    return mcm

MCM_Calculated = MCM(12, 8)
print(f"MCM: {MCM_Calculated}")


#-------------------------------------------------------------------------------#
#WAP to ask user enter an email. Output if email is valid creating a function. Email is valid if it had "@" symbol
def right_email(email):
    for i in email:
        if i == "@":
            print("Valid email")
            break
    else:
        print("Invalid email")

right_email("Jenni@gamil.com")
"""
Chat GPT recomendation:

def right_email(email):
    if "@" in email:
        print("Valid email")
    else:
        print("Invalid email")

right_email("Jenni@gmail.com")
"""
#-------------------------------------------------------------------------------#

#WAP to ask user numbers until they input zero, then show summatory result using functions
total = 0

def summatory(user_number):
    global total # If we refer to global variable we must to use the reserved word 'global'
    total += user_number

user_number = int(input("Enter your number: "))

while user_number != 0:
    summatory(user_number)
    user_number = int(input("Enter your number: "))


print("Summatory: ", total)

#-------------------------------------------------------------------------------#

#WAP to know if a number input by user is prime or not

def prime_number(user_number):
    if user_number < 2:
        return False
    for i in range (2, user_number):
        if (user_number % i) == 0:
            return False
    return True

user_number = int(input("Enter a integer number: "))
print("Is the number prime?: ", prime_number(user_number))

#-------------------------------------------------------------------------------#

#WAP to enter a number and a digit. Output how many times digit is in the number

integer_number = int(input("Enter a integer number: "))
digit = int(input("Enter a digit: "))


while digit >= 10:
    print("It's not a digit, please try again")
    digit = int(input("Enter a digit: "))

def digit_ocurrences(integer_number, digit):
    frequency = 0
    while integer_number != 0:
        lastDigit = integer_number % 10
        if lastDigit == digit:
            frequency += 1
        integer_number = integer_number // 10
    return frequency

print("Number of digit ocurrences", digit_ocurrences(integer_number, digit))

#-------------------------------------------------------------------------------#
#WAF to enter values, output its factorial and how many times the user input numbers

def factorial(user_numbers):
    factorial_numb = 1
    for i in range(1, user_numbers + 1):
        factorial_numb *= i
    return factorial_numb


count = 0
while True:
    user_input = int(input("Enter your numbers (0 to stop): "))
    if user_input == 0:
        break
    count += 1
    print("Factorial is:", factorial(user_input))

print(f"Total numbers: {count}")

#-------------------------------------------------------------------------------#
#WAF which calculate IVA (by default = 21). User must indicates amount and IVA percent

def IVA(amount, IVA_percent=21):
    user_IVA = IVA_percent/100
    IVA_total = amount * user_IVA
    bill_total = amount + IVA_total
    return print(f"Total payment is: {bill_total}")
IVA(15000)
IVA(30000, 19)

#-------------------------------------------------------------------------------#
#WAF which receive a list and return the average

my_list = []

for i in range(5):
    user_numbers = int(input(f"Enter {i+1} number: "))
    my_list.append(user_numbers)


def average(list):
    for i in list:
        total = sum(list)
        average = total/len(list)
    return print(f"Average: {average}")

average(my_list)

#-------------------------------------------------------------------------------#
#WAF which receives a list and determine what numbers are pair and odd

number_list = [1, 2, 3, 4, 5]
pairs = []
odds = []

def pairity_check(number_list):
    for i in number_list:
        if i % 2 == 0:
            pairs.append(i)
        else:
            odds.append(i)
    return {"Pair numbers": pairs, "Odds numbers": odds}

#Here we've implemented a dicctionary, as soon as posible we'll see how to use it
result = pairity_check(number_list)
print(result)

#-------------------------------------------------------------------------------#
#WAF which elevate a number enter by parameters the base and the exponent

def pow(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

if base < 0 or exponent < 0:
    "Something went wrong, numbers are negative"
print(pow(base, exponent))

#-------------------------------------------------------------------------------#
#WAF which calculate the area of a circle and other one that calculate the volume of a cylinder using the first function

import math

def circle_area(radius):
    area = math.pi * (radius**2)
    return area

def cylinder_volume(radius, hight):
    volume = circle_area(radius)*hight
    return volume

user_radius = int(input("Enter the circle radius to calculate its area: "))
print("Circle area: ", circle_area(user_radius))

user_hight = int(input("Enter the cylinder hight to calculate its volume: "))
print("Cylinder voume: ", cylinder_volume(user_radius, user_hight))

#-------------------------------------------------------------------------------#
#WAF which receives a list of numbers and returns another list with its squares

my_list = {2, 3, 5, 6, 8, 9}
squares = []

def squares_list(list):
    for i in list:
        values = pow(i, 2)
        squares.append(values)
    return squares

print(f"Its squares are: {squares_list(my_list)}")