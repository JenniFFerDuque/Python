#Second program:

# Enter a number from user and print its absolute value:

# Using normal if-else:
number = int(input("Enter one number: "))
if number >= 0:
    print(number)
else:
    print(-number)

# Using ternary statement:
number = int(input("Enter one number: "))
absolute = number if (number >= 0) else -number
print("Absolute value:", absolute)

#-----------------------------------------------------------------#

# Enter a character from user and check if it is vowel or consonant
char = input("\nEnter one character: ")
if char.lower() == "a" or char.lower() == "e": #and so on with all the vowels...
    print("vowel")
else:
    print("consonant")

#-----------------------------------------------------------------#

# Practice:
water_cups = int(input("\nHow many cups have you drunk (so far) today?"))
objective = "You've done" if water_cups >= 6 else "You're missing:", 6 - water_cups
print(objective)
