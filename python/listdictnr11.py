#Lists and Dictionaries with For Loops, List Comprehension, and Dictionary Comprehension

print(" before start this topic veryfiy")
pin = ""
correct_pin = "1212"
while pin != correct_pin:
    pin = input("enter  your pin!")
    if pin != correct_pin:
        print("incorrect pin. try again!")
print("pin accepted you can proceeded.")
print("---------------------------------------------")

#1. Looping Through Lists

number = [10,20,40,80]
total = 0

for num in number:
    total += num
    print(f"total sum = {total}")

#Example 1: Sum of all numbers in a list

numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print("Total sum:", total)
print("---------------------------------------------")

#Example: Doubling each number in a list

numberss = [10, 20, 30, 40, 50, 60]
doubled = []

for num in numberss:
    doubled.append(num * 2)
print(f"doubled number : {doubled}")
print("-----------------------------------------------")

#Example: Printing Kannada food items

foods = ["edli", "vada", "dhose", "bath"]

for food in foods:
    print(f"food name = {food}")
print("===============================================")


#2. Looping Through Dictionaries

student_marks = {"anil" : 70, "nithin" : 74, "shiva" : 67, "kavan" : 65}

for student in student_marks:
    print(f"name--> {student}")

for students in student_marks.values():
    print(f"marks --> {students}")

for stud in student_marks.items():
    print(f"hear full details :-{stud}")
print("=================================================")

#3. for Loops with range()

#Example: Adding marks to students using index values

students_names = ["Anand", "Geetha", "Kumar"]
marks = [85, 90, 78]

student_marks = {}

for i in range(len(students_names)):
    student_marks[students_names[i]] = marks[i]

print(student_marks)
print("=================================================")

#4. List Comprehension

#Example 1: Squaring numbers in a list

numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)
print("------------------------------------------------")

#Example 2: Filtering even numbers

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
print("------------------------------------------------")

#Example 3: Uppercasing Kannada city names

cit = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
uppercase = [city.upper() for city in cit]
print(uppercase)
print("------------------------------------------------")

#5. Dictionary Comprehension

#Example 1: Creating a dictionary of squares
numbers = [1, 2, 3, 4, 5]
square_dis = {num : num ** 2 for num in numbers}
print(square_dis)
print("------------------------------------------------")

#Example 2: Converting a list of names to a dictionary of name lengths
names = ["Anand", "Geetha", "Kumar"]
length_name = {name : len(name) for name in names}
print(length_name)
print("------------------------------------------------")

#Example 3: Filtering cities with population above 10 lakhs (Localized Example)
city_population = {
    "Bengaluru": 84,
    "Mysuru": 11,
    "Hubballi": 9,
    "Mangaluru": 5
}

large_city = {city : population for city, population in city_population.items() if population > 10}

print(large_city) 
print("======================================================================")

#6. Splitting Strings to Create Lists

#Example 1: Splitting a sentence into words
sentence = "I love coding in Python"
words = sentence.split()
print(words)
print("------------------------------------------------------")

#Example 2: Splitting a string with commas
data = "apple,banana,mango"
fruite = data.split(",")
print(fruite)

#Example 3: Limiting the number of splits
sentence = "Python is fun to learn"
word = sentence.split(" ", 2)
#word = sentence.split(" ", 3) #output ['Python', 'is', 'fun', 'to learn']
#word = sentence.split(" ", 4) #output ['Python', 'is', 'fun', 'to', 'learn']
print(word)
print("-------------------------------THE END----------------------------------")