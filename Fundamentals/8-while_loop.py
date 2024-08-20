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
