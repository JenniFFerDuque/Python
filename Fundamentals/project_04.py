# Practice lists:

# WAP to enter 5 numbers from user and add them into a list and print it
list = []

while len(list) < 5:
    numbers = int(input("Enter your value: "))
    list.append(numbers)

print(list)

# In Python, lists can't assign values to index that hasn't been created yet.
# So, the right way is by using append method

#---------------------------------------------------------------------------------------------------

# WAP to enter 5 numbers from user, append them into a list and print sum of them, whithout using sum function
my_list = []
summ = 0

while len(my_list) < 3:
    values = int(input("Enter your values: "))
    my_list.append(values)
    summ += values

print(my_list)
print("Summatory is:", summ)

#---------------------------------------------------------------------------------------------------

# WAP which save assigments and scores and print them all
assignments = []
scores = []
user_response = " "
i = 0

while user_response.lower() != "n":
    subject = input("Enter your subject: ")
    assignments.append(subject)
    my_scores = float(input("Enter your last score: "))
    scores.append(my_scores)
    user_response = input("Do you want to append another score? y/n: ")

while i < len(assignments):
    print("In the subject:", assignments[i], "your score was: ", scores[i])
    i += 1

#---------------------------------------------------------------------------------------------------

#WAP which prints index multiples of three in a list that contains the abecedary
abc_list = ["a", "b", "c", "d", "e", "f", "g", "h",
            "i", "j", "k", "l", "m", "n", "ñ", "o",
            "p", "q", "r", "s", "t", "u", "v", "w",
            "x", "y", "z"]

index_deleted = [i for i in range(len(abc_list)-1) if (i+1) % 3 == 0]
#Generates a range of numbers from 0 to len(abc_list)-1, which numbers must to be multiples of three
for index in reversed(index_deleted):
    abc_list.pop(index)
print(abc_list)

#Example of list comprehension:
list_size = 10
number_list = [i for i in range(list_size+1) if i % 2 == 0]
print(number_list)

# It's the same of:
# number_list = []
# for i in range(10):
#    if i % 2 == 0:
#    number_list.append(i)
# print(number_list)

#---------------------------------------------------------------------------------------------------

#WAP which generates a list with the following prices and then output the bigest and the smallest value
prices = [50, 75, 46, 22, 80, 65, 8]
print("The smallest value is: ", min(prices))
print("The biggest value is: ", max(prices))

#---------------------------------------------------------------------------------------------------

#WAP which save the following subjects and print them all as "I study: " where subjects are the list elements
subjects = ["Math", "Fisic", "Chemistry", "History", "Lenguaje"]
for i in range(len(subjects)):
    print("I study: ", subjects[i])

#---------------------------------------------------------------------------------------------------

#WAP which save the primitive lotery numbers, save the into a list and print them sort
lotery_list = []

for i in range(6):
    lotery_number = int(input(f"Enter your {i+1} lotery number: "))
    if lotery_number <= 49:
        lotery_list.append(lotery_number)
        i += 1
    else:
        print("Number out of range... Try again")
        lotery_number = int(input(f"Enter your {i+1} lotery number: "))
        lotery_list.append(lotery_number)
        i += 1
lotery_list.sort()
print("Lotery numbers: ", lotery_list)


#---------------------------------------------------------------------------------------------------

#WAP which save numbers from 1 up 10 and output them on screen in reverse order and separated by comas.
#number_list = [i for i in range(10, 0, -1)] # [starts from 10 (including 10), stop before reaching 0 (no including 0), in reverse order]
#number_list = [i for i in range(1, 11)] #It would be the code If it wasn't in reverse order.

print(", ".join(map(str, number_list)))
"""
Map
The map function in Python is a powerful tool that allows you to apply a function to every item in an iterable, 
such as a list or tuple. In this case is turning each element of the list on a string type.
"""

#WAP which print the product of the following two vectors:
A = [1, 2, 3]
B = [-1, 0, 2]
C = []

i = 0
j = 0
while i < len(A):
    C.append(A[i] * B[j])
    j += 1
    if j == len(B):
        i += 1
        j = 0
print(C)

#---------------------------------------------------------------------------------------------------

i = 3
abc_list = ["a", "b", "c", "d", "e", "f", "g", "h"
            "i", "j", "k", "l", "m", "n", "ñ", "o"
            "p", "q", "r", "s", "t", "u", "v", "w",
            "x", "y", "z"]
while abc_list.index(i):
    abc_list.remove
    i *= 3
print(abc_list)
