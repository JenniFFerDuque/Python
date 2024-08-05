''' User imput: The information input by user always will be a string type. To change that
must be necessary use (casting) sentence '''

# Structure: var = casting(input("message"))

#Examples: 
name = input("Enter you name: ")
print("Name:", name) #Using normal print

age = input("Enter your age: ")
print(f"Age: {age}") #using f-string (more fancy)

# Casting: 
phone = int(input("Enter you phone number updated: "))
print("Phone:", phone)#Must use normal print when casting

savings = float(input("Enter how much savings do you have: "))
print ("Savings:", savings)