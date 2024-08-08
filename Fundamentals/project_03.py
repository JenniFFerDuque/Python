# Practice while loop

# WAP to print the following serie: 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100
i = 1
while i <= 10:
    print(i*i, end =" ")
    i += 1
print("\n")

# WAP to print the following serie: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
i = 1
while i <= 10:
    if i < 10:
        print(i, end=" + ")
    else:
        print(i)
    i += 1
print("\n")

# WAP to ask user their age and print one by one the number of years that they have turned so far
user_age = int(input("Enter your age: "))
i = 1
while i <= user_age:
    print(i, end=" ")
    i += 1
print("\n")

# WAP to ask user a positive integer number and output on screen all odd numbers from 1 up to user's number
user_number = int(input("Enter positive integer number: "))
i = 1

if user_number < 0:
    print("Your number is not valid")
else:
    while i <= user_number:
        output = print(i, end=" ") if (i % 2 != 0) else ""
        i += 1
print("\n")