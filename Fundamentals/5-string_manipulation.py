# String manipulation:

#1: Print a char using index
name = "jenniffer Duque"
print(name[0]) #It's gonna print first letter
print(name[-1]) #It's gonna print last letter

#2: Concatenate
name_user = "Pedro"
lastname_user = "Escamoso"
print(name_user, lastname_user) #using comma
print(name_user + " " + lastname_user) #using + operator

#3: Print multiple times
name = "Juanito"
print(name * 3)

#4: know how length is a string
name = "Jenniffer"
print(len(name))

#Built-in methods:

#capitalize(): It capitalizes first letter
text = "jenni"
print(text.capitalize())

#title(): It capitalizes first letter in each word
text = "hello world"
print(text.title())

#strip(): It eliminates whitespaces at the begginig and at the end
text = " hello "
print(text.strip())

#replace(): It replaces parts of the string
text = "Hello world"
print(text.replace("world", "python")) #replace(old, new)

#split(separator): It splits the string in a new list, according to separator
text = "Hello,world,Im,Jenni"
print(text.split(","))

#join(): It joins elements of a list in only one string
list = ["Hello","world"]
print(" ".join(list))

#lower() It convert the string to lowercase
text = "HELLO WORLD"
print(text.lower())

#upper() It convert the string to uppercase
text = "hello world"
print(text.upper())

#startswith(prefix) It verify if the string starting with an specific substring
text = "Hello world"
print(text.startswith("Hello")) #This method print True or False

#endswith(sufix) It verify if the string ending with an specific substring
text = "Hello world"
print(text.endswith("world")) #This method print True or False

#Example mixing some built-in methods
name = "CARLA MaRCela"
print(name.lower().title())