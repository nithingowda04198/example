#pin = ""
#correct_pin = "9972"
#while pin != correct_pin:
#    pin = input("Enter your pin: -")
#    if pin != correct_pin:
#        print("incorrect pin. try again!")
#print("pin accepted you can proceeded.")
#print("------------------------------------------------")


#Basics of Functions

#Defining a Function

def greet():
    print("hello nithin")

greet()

#Function Parameters

def greet_name(name):
    print(f"myname is :- {name}")
greet_name("nithin")

print("--------------------------------------")

#Returning Values from a Function

def add_number(a, b):
    return a + b

result = add_number(30, 40)
print(f"total = {result}")

print("---------------------------------------")

#Default Parameter Values

def default_name(name = "nithin"):
    print(f"my name is :- {name}")

default_name()
default_name("Janardhan")

#Local and Global Variables

name = "global name"               #if we mention variable outsid the all function its called global variable

def greet():
    name = "local name"            #if we mentioned any variable inside the function its called local variable 
    print(name)

greet()                            #local variable output 
print(name)                        #global variable output


print("====================================================================================")


#Functions - Advanced Concepts

#1.Keyword Arguments  

def display_info(name, age):
    print(f"name : {name}, age : {age}")

display_info(name = "Nithin", age=27)
print("-----------------------------------------------------------")

#Variable-Length Arguments(we can use *args and **kwargs)

#*args
def total_sum(*number):
    result = 0
    for num in number:
        result+= num
    return result

print(total_sum(1,2,3,4))
print("---------------------------------------------------------")

#**KWargs

def student_info(**details):
    for key, value in details.items():
        print(f"{key} : {value}")

student_info(name = "nithin", age = 27, place = "pandavapura")
print("---------------------------------------------------------")

#3. Lambda Functions

double = lambda x: x * 2         
print(double(5))
print("----------------------------------------------------------")


#Recursion

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)  #return 5 * factorial(5-1)  <factorial(4) = 4*3*2*1 =24> 5*24 = 120

print(factorial(5))
print("-------------------------------------------------------------")

#Nested Functions

def first_name(name):
    def second_name():
        print(f"hello! {name}")
    second_name()

result = first_name("nithin")
#print(result)

#In this example, the first_name() is called within second_name() and uses the name parameter of the outer function.