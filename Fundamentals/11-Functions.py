# definition of function
def my_function():
    print("Hey!")
#-------------------------------------------------------------------------------#

# calling of function
my_function() #Output: Hey!


#Example:
def numbers():
    print(1, end=" - ")
    print(2, end=" - ")
    print(3)

numbers() #Output: 1 - 2 - 3
#-------------------------------------------------------------------------------#

#Function arguments

def indore(a):
    print(a)

indore("A") # a = "A"
indore(10)  # a = 10


#Example 1
def add(a, b):
    print("Number ", a)
    print("Number", b)
    print("Sum:", a + b)

add(3, 5)

#Example 2
def add_one(x):
    x += 1
    print(x)

add_one(5)
# print(x): Here code shows the error (it's not definided) because X is'nt global. It's local

#Example 3
number = 3         # c is a global variable
def add1(number):  # c is a local variable
    number += 1
    print(number)

add1(7)
print(number) #Being a gobal variable I can print them without problems

#-------------------------------------------------------------------------------#

#Return statement 

#Example 1
def largest(x, y):
    if (x >= y):
        return x
    else:
        return y

print("largest number:", largest(10, 5))

largest_number = largest(4, 6) # We can assign function to a variable
print("Largest:", largest_number)

#Example 2
def printing():
    print(1)
    print(2)
    return 
    print(3)
    print(4) #Code is unreachable. All before return it's going to be NULL and ignored

printing()

#-------------------------------------------------------------------------------#

#Default arguments

def say(msg, times = 1): 
    print(msg * times)

say("Hello!") #Output one time (by default)
say("Wi! ", 2) #Output twice because users specify in arguments

""" 
Times is a local variable that by default it's gonna print the string only one time, but if the user changes that value,
it's gonna be printed as many times as user specified in arguments.
"""

def numbers(a=2, b=3, c=4):
    print(a)
    print(b)
    print(c)

numbers() 
numbers(1, 2, 3)
numbers(3, 4)
#I can use the default values or I can change them, modifying the arguments



