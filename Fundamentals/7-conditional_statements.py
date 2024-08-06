# Conditional statements:

# If:
a = 10
if a > 5:
    print("It's a large number")

sky = input("Enter sky color: ")
if sky.lower() == "blue":
    print(True)

# If-else:
a = int(input("First number: "))
b = int(input("Second number: "))
if (a + b) >= 10:
    print("Okey")
else: 
    print("hmm")

# Elif:
number = int(input("Enter one number: "))
if number <= 3:
    print("Too small")
elif number >=5:
    print("Too large")
elif number == 4:
    print("It is!")
else:
    print("Error 404")


"""
The defirence between else and elif
else: When there aren't more options, "el descarte"
elif: indicate what would happen if the first condition doesn't applies
"""

# Ternary statements
# structure: var = value_True if (condition) else (value_false)
status = 1
msg = "Login" if status == 1 else "logout"
print(msg)

a = int(input("First number: "))
b = int(input("second number: "))
largest = "first" if a>b else "second"
print("Largest number is the:", largest)