#Accessing List Elements

fruits =["apple", "banana", "papaya"]

print(fruits[0])
print(fruits[:2])
print(fruits[-1])
print("----------------------------------------------------------")

#Modifying Lists

fruits[1] = "cherry"
print(fruits)
print("----------------------------------------------------------")


#Adding elements:
fruits.append("grape")
print(fruits)
print("----------------------------------------------------------")

#insert

fruits.insert(1, "kiwi")
print(fruits)  
print("----------------------------------------------------------")

#Removing elements:

friends =["anil", "shiva", "sanju", "kavan", "sharath"]

friends.remove("kavan") #remove perticular string 
print(friends)

friends.pop()  #if we not mention any ondex that will delete last one defauls
print(friends)

friends.pop(2) #delete indext perticular you want
print(friends)

friends.clear() #clear all index
print(friends)
print("----------------------------------------------------------")


#List Functions and Methods

print(len(fruits))  # Output: 3
print("----------------------------------------------------------")


numbers = [5, 2, 9, 1]
print(sorted(numbers))  # Output: [1, 2, 5, 9]   it is rearrenge
print(numbers)  # Original list remains unchanged: [5, 2, 9, 1]
print("----------------------------------------------------------")

number = [1, 6, 3, 4]
print(sum(number))  # Output: 10 sum
print("----------------------------------------------------------")

#index(element): Returns the index of the first occurrence of the specified element.

print(fruits.index("apple"))  # Output: 0
print(fruits.index("papaya"))  # Output: 3
print("----------------------------------------------------------")


#count(element): Returns the number of occurrences of an element in the list.

list = ["bus", "car", "bike", "car", "car", 1, 2, 3, 1, 1, 3, 3, 3, 2]
print(list.count("car"))
print(list.count(1))
print(list.count(2))
print(list.count(3))
print("----------------------------------------------------------")

#reverse(): Reverses the elements of the list in place.

fruits.reverse()
print(fruits)

list.reverse()
print(list)
print("----------------------------------------------------------")


#sort(): Sorts the list in place (ascending by default).

numbe = [5, 2, 9, 1]
numbe.sort()
print(numbe)  # Output: [1, 2, 5, 9]
print("----------------------------------------------------------")

#Nested Lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a nested list
print(matrix[0])  # Output: [1, 2, 3] (first row)
print(matrix[1][1])  # Output: 5 (element in the second row, second column)
print(matrix[2][0])
print(matrix[0][2])

print("----------------------------------------------------------")

#touple --> ()

my_name = ("nithin", "power", "kencha", 1, 1, 1, 1)
print(my_name.index("power"))
print(my_name.count(1))


