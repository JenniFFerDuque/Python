#Functions:

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

#Parameters and arguments:

def indore(a): # a is a parameter
    print(a)

indore("A") # a = "A" # "A" es an argument
indore(10)  # a = 10

#Why use parameters? Because using them, functions will be more flexible:
def greeting():
    name = "Carlos"
    print(f"Hello, {name}")
greeting() #This function just works for Carlos' name

def gretting2(name):
    print(f"Hello, {name}")
gretting2("Jenni") #This function receives any name and works correctly

#When a function receives parameters by arguments, it's not necessary state those values inside the function

#Example 1
def add(a, b): #a, b are the parameters
    print("Number ", a)
    print("Number", b)
    print("Sum:", a + b)
add(3, 5) #3, 5 are the arguments

#Example 2
def add_one(x): #x is a parameter
    x += 1
    print(x)
add_one(5) #5 is the argument
# print(x): Here code shows the error (it's not definided) because X is'nt global. It's local

#Example 3
number = 3         # c is a global variable
def add1(number):  # c is a local variable
    number += 1
    print(number)
add1(7)
print(number) #Being a gobal variable I can print them without problems


#-------------------------------------------------------------------------------#

#Return statement:

#Example 1
def largest(x, y):
    if (x >= y):
        return x
    else:
        return y
print("largest number:", largest(10, 5))

largest_number = largest(4, 6) # We can assign to a variable one function
print("Largest:", largest_number)

#Example 2
def printing():
    print(1)
    print(2)
    return 
    print(3)
    print(4) #Code is unreachable. All before return it's going to be NULL and ignored
printing()
"""
If a function doesn't have a return statement, it'll run but won't print anything ("none" by default). 
In this case, you must use print() function so as to see the result
"""
#-------------------------------------------------------------------------------#

#Default arguments

def say(msg, times = 1): 
    print(msg * times)

say("Hello!") #Output one time (by default)
say("Wi! ", 2) #Output twice because users specify in arguments

""" 
Times is a local variable which by default it's gonna print the string only one time, but if the user changes that value,
it's gonna be printed as many times as user specified in the arguments.
"""

def numbers(a=2, b=3, c=4):
    print(a)
    print(b)
    print(c)

numbers() 
numbers(1, 2, 3)
numbers(3, 4)
#I can use the default values or I can change them, modifying the arguments

#-------------------------------------------------------------------------------#

#Doc string (Documentation string)

# This is a string just before the function that show us the documentation
def summatory(a, b):
    """
    This function receive two arguments and return the absolute value of the sum of them
    """
    sum = a + b
    return abs(sum)

help(summatory) #the function help, it's going to print the string we put below of the statement (must be there)

#-------------------------------------------------------------------------------#

#Lambda Function: is a way to make functions in one line using keyword 'lambda'
# name = lambda_keyword arguments : expression

square_area = lambda size : pow(size, 2)
print(f"{square_area(2)}cm^2")

square_perimeter = lambda size : 4*size
print(f"{square_perimeter(2)}cm")

#This special function also is used along with map function

#-------------------------------------------------------------------------------#

#Filter function: its a tool that help us to filter elements in a list, tuple, etc.
#filter() have two arguments: function which determine the condition and a list or tuple whose it iterates

#Using def function:
numbers = [1, 2, 3, 4, 5]

def pairs(x):
    return x % 2 == 0

pair_list = list(filter(pairs, numbers)) #list() turns the iterables in a list you could print and use its methods
# "Pairs" is passed as an argument, we aren't calling the function, so we dont need to use "()"
print(pair_list)


#Using lambda function:
numbers = [1, 6, 2, 8, 3, 7, 11, 10]
pair_numbers = list(filter(lambda i : i > 5, numbers))
print(pair_numbers)

#-------------------------------------------------------------------------------#

#Map function: applies a defined funtion to each iterable item of a list or tuple.
#It receives two atguments: a function and a list or tuple

numbers = [1, 3, 5, 7, 9]
pow = list(map(lambda i : pow(i, 2), numbers)) #Here we can use lambda function to make it in only one line
print(pow)

#-------------------------------------------------------------------------------#