#List: collections (arrays) of different type of elements

#      -5  -4   -3  -2  -1 #Index could be negative
list = [10, 20, 30, 40, 50]
#       0   1   2   3    4  #Index starts with zero

print(list[-1])
print(list[0])

list =[10, "a", 5.5] #Elements could be of different types
print(list)

#Print type:
list = ["Jenni"]
print(type(list)) #Type will be: 'class list'

#Print by index:
list = [1, 2, 3, 4, 5]
print(list[0]) #If index is out of range, it'll show error

#Print element types
list = (1, "uno", 2, "dos")
print(type(list[0]))

#-------------------------------------------------------------------------------#

#We can reassign a value using index:
list = [1, 2, 3, 4]
list[3] = 5
print(list) #output: [1, 2, 3, 5]

#We can print a list interval: [start : end] includes the start not the end
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list[0:3]) #output: [1, 2, 3] 

print(list[1:3]) #output: [2, 3]

print(list[:5]) #output: [1, 2, 3, 4, 5] <- uses zero as default

print(list[7:]) #output: [8, 9] <- from the start to the end (including the end)

print(list[:]) #output: All the list

print(list[-4:-1]) #output: [6, 7, 8]

print(list[:-1]) #output: [1, 2, 3, 4, 5, 6, 7, 8]

#We can also select the steps: [start : end : steps]
print(list[::2]) #output: [1, 3, 5, 7, 9]

#This step gonna print the list inside out
print(list[::-1]) #output: [9, 8, 7, 6, 5, 4, 3, 2, 1]

print(list[::-2]) #output [9, 7, 5, 3, 1]

#Steps are basically how the list must to be printed
#-------------------------------------------------------------------------------#
#List functions:

#len: Knows list length <- starts to count in one
list = [1, 8, 11, 4, 6]
print(len(list)) #output: 5

#sum: Makes a sum of the list values
print(sum(list)) #output: 30

s = sum(list)
print(s) #output: 30

#max: shows the max (biggest) value in the list
print(max(list)) #output: 11

biggest_value = max(list)
print(biggest_value) #output: 11

#min: shows the min (smallest) value in the list
print(min(list)) #output: 1

smallest_value = min(list)
print(smallest_value) #output: 1

#Help function: shows us how a function works
help(len)
help(min)
help(max)
help(sum)
#-------------------------------------------------------------------------------#
#List metods:

# class list{
#   append()
#   index()
#   insert()
#   remove()
#   pop()
#   reverse()
#   sort()
#   clear()
#   count
# }

#Append: add a new item to the end of the list
list = [1, 2, 3, 4, 5]
list.append(6) 
print(list) #output: [1, 2, 3, 4, 5, 6]

#Index: Shows the first index of an specific value
index = list.index(3)
print(index) #output: 2

#Insert: Insert a value before an index [index, value]
list.insert(0, 9)
print(list) #output: [9, 1, 2, 3, 4, 5, 6]

#Remove: remove first occurrence of a value
list.remove(9)
print(list) #output: [1, 2, 3, 4, 5, 6]

"""Pop: remove an item by negative index (last as default = -1)
also can return the value that was delete"""
list.pop()
print(list) #output: [1, 2, 3, 4, 5]

number_deleted = list.pop(-5)
print(number_deleted)  #output: 1 <- number that was delete

#Reverse: It just modifies the order of the list and doesn't return any value
list.reverse()
print(list) #output: [4, 3, 2, 1]

"""Sort: sort list in ascending or descending order, the list itself is modified.
The order of two equal elements is mantained. To print in descending order, 
reverse parameter as boolean type is required"""
list.sort() # (reverse = False) as default
print(list)

list.sort(reverse = True) # reverse is a keyword, must to be that and another is not allowed
print(list) # <- descending order

#Clear: clear all the values of the list
list.clear()
print(list) #Output: [] <- empty list

#Count: return number of occurrences of value.
list = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7, 7, 8, 9]
print(list.count(4))









