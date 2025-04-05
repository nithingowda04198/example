#name = input("Enter your name: nithin")
#age = int(input("Enter your age: 26"))  # Convert input to integer
#print("Hello, " + name + "! You are " + str(age) + " years old.")

#String Manipulation

first_name = "NITHIN"
last_name = "gowda"
full_name = first_name + " " + last_name

if (first_name[0] == "N"):

    print(first_name)

else:
    print(full_name)  # Output: "Nithin Gowda"


#Repetition: Repeating a string multiple times using the * operator.

greeting = "Nithin! " * 3
print(greeting)  # Output: "Hello! Hello! Hello! "


#String methods

message = "  FUCK, YOU!  "
print(message.strip())  # Output: "Fuck, You!"
print(message.upper())  # Output: "FUCK, YOU!"
print(message.lower())  # Output : "fuck, you"
print(message.replace("FUCK", "LIKE"))  # Output: "Like, you!"
print(message.replace("YOU!", "YOU girl"))


#ccessing String Characters:

text = "Nithingowda"
print(text[0])  
print(text[2]) 
print(text[-1])  
print(text[-3]) 
print(text[0:6])  
print(text[:6])  
print(text[7:]) 
print(text[5:11])
print(len(text))



