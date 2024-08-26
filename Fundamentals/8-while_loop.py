# While loop

"""To enter in this loop correctly, it's necessary have a variable iterator that changes;
if we hasn't, it gonna be infinitive."""

# Example using basic while loop
number = 1
while number <=5:
    print(number)
    number += 1

# Print while loop in only one line
i = 0
while i<=10:
    print(i, end= " ")
    i+=2
print("\n")

# print while loop until user chooses
option = "y"
while option == "y":
    print("❤")
    option = input("\nDo you want print a heart: y/n ")

#-------------------------------------------------------#

# Break: WAP to guess a number by user and say if it is smaller or bigger
key_number = 19
response = ""

while response.lower != "me rindo":
    user_number = int(input("Try guess the number: "))
    
    if (user_number < key_number):
        print("The number is bigger")
    elif (user_number > key_number):
        print("The number is smaller")
    else:
        print("Yeah, it is!")
        break
    response = input("Are you giving up? (type 'me rindo' to give up): ")

# Break: WAP to enter numbers until user types '0'. To the show number summatory
number = int(input("Enter one number: "))
summ = 0

while number != 0:
    summ += number
    number = int(input("Enter one number: "))
print("Summatory is", summ)