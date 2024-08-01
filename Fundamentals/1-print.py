# Basic print function
print("Hello world")

# \n - new line
print("Hello \nworld")

# \t - tab
print("Hello \tworld")

#Examples:
print("* \n** \n***")
print("Himanshu \n\tDAVV \n\t\tIndore")
print("\t* \n* \t\t* \n\t*")

# sep: it allows you specify how we'll separate the words
print("Hello", "World", "I'm Jenni", sep="; ")

# end: it allows you printing in the same line the next 'print', it's the contrary of \n
name = "Jenniffer"
last_name = "Duque"
print(name, end=" ")
print(last_name)

# f-strings: it allows you arrange the information in a better way
print(f"Name: {name}, lastname: {last_name}") #variables puts always on '{}'

#Format: it allows you print an specific amount of digits
value = 3.14167
print("Value: {:.2f}".format(value))