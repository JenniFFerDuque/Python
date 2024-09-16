#Range function: It used to specify loops range

r = range(10)
#r = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

#Start from cero as default, but you can change it
r = range(2, 10)
print(r) #output: range(2, 10)

r = list(range(10))
print(r) #output:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

r = list(range(0, 10, 2)) # steps
print(r) #output: [0, 2, 4, 6, 8]

#-------------------------------------------------------------------------------#
#WAP to enter a string from user and print length of it
string = input("Enter a string: ")

for i in string:
    print(i, end=" ")
print("\nLenght: ", len(string))

#-------------------------------------------------------------------------------#
#WAP to print all digits between 0-9
for i in range(10):
    print(i, end=", ")

#-------------------------------------------------------------------------------#
#WAP to print all numbers between 100 - 199
for i in range(100, 200):
    print(i, end=", ")

#-------------------------------------------------------------------------------#
#WAP to print all numbers between 5 - 20, step 3
for i in range(5, 20, 3):
    print(i, end=", ")

#-------------------------------------------------------------------------------#
#WAP  to enter a positive integer number and print all the digits between users' enter number and the double of it
user_number = int(input("Enter your number (It must be positive): "))

if user_number < 0:
    print("Error 300... Number must be positive")
else:
    for i in range(user_number, user_number*2):
        print(i)

#-------------------------------------------------------------------------------#
#WAP to enter a quatity, in each iteration ask user a number. At the end show summatory result
quantity = int(input("Enter your quantity: "))
summ = 0

for i in range(quantity):
    user_number = int(input("Enter " + str(i+1) + " number: "))
    summ += user_number
print("Summatory result: ", summ)

#-------------------------------------------------------------------------------#
#WAP to enter by user a phrase and then print them all vocals in it
phrase = input("phrase: ")
print("Vocals in phrase:")

for x in "aeiou":
    if x in phrase:
        print(x)

#-------------------------------------------------------------------------------#
#WAP to enter by user a phrase and output all the vocals in it
phrase = input("Enter your phrase: ")
vocals = 0

for x in "aeiou":
    if x in phrase:
        vocals += 1

print("Vocals in your phrase: ", vocals)

#-------------------------------------------------------------------------------#
#WAP which print the sum between all numbers of 0 up to 100
summ = 0

for i in range(101):
    summ += i
print("Sum result: ", summ)

#-------------------------------------------------------------------------------#
#WAP which print factorial of integer positive number input by user
user_number = int(input("Enter a positive integer to know its factorial: "))
factorial = 1

if user_number < 0:
    print("Number is negative, factorial is undefined.")
elif user_number == 0:
    print("The factorial of 0 is: 1")
else:
    for i in range(1, user_number + 1):
        factorial *= i
    print(f"Factorial of {user_number} is: {factorial}")

#-------------------------------------------------------------------------------#
#WAP to enter a string from user and print length of it
user_string = input("Enter your string: ")
count = 0
for i in user_string:
    count += 1
print("String lenght:", count)

#-------------------------------------------------------------------------------#
#WAP  to enter 5 numbers from user append it into a list and print largest element from it. Without using max function
numbers_list = []


for i in range(5):
    user_numbers = int(input(f"Enter your {i+1} number: "))
    numbers_list.append(user_numbers)

largest = numbers_list[0] #It prevents errors if numbers are negative

for i in numbers_list:
    if i > largest:
        largest = i
print(numbers_list)
print("Largest number: ", largest)

#-------------------------------------------------------------------------------#
#WAP to print number 0-10 in reverse order
my_list = [i for i in range(10)]

for i in reversed(my_list):
    print(i, end=", ")

#-------------------------------------------------------------------------------#
#Loop for-else
for i in range(5):
    print(i)
else: #This part is printed when the for loop is finished without breaks or pass sentences
    print("*")