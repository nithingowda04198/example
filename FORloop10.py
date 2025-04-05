print(" before start this topic veryfiy")
pin = ""
correct_pin = "1111"
while pin != correct_pin:
    pin = input("enter  your pin!")
    if pin != correct_pin:
        print("incorrect pin. try again!")
print("pin accepted you can proceeded.")
print("---------------------------------------------")

#The Basic Structure of a for Loop

citys = ["bangaluru", "mysuru", "mandya", "hassan"]
for city in citys:
    print(city)
print("------------------------------------------------")

#2. Using range() with for Loops

#for i in range(1,10):
#    print(i)

for i in range(1,11,3):
    print(i)
print("--------------------------------------------------")

#3. Looping Over Strings

name = "karnataka"
for letter in name:
    print(letter)
print("---------------------------------------------------")

#4. Nested for Loops

for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
        print()
print("----------------------------------------------------")

#5. Using break in a for Loop

cites = ["bangaluru", "mysuru", "mandya", "hassan"]
pin = ""
for location in cites:
    if location == "mandya":
        print(f"found city {location}")
        break
    print(location)
print("-------------------------------------------------------")


#6. Using continue in a for Loop(SKIP THE [PLACE])

cites = ["bangaluru", "mysuru", "mandya", "hassan"]

for city in cites:
    if city == "mysuru":
        continue
    print(city)
print("--------------------------------------------------------")

#7. Looping Through a List with enumerate()

cites = ["bangaluru", "mysuru", "mandya", "hassan"]
for index, city in enumerate(cites):
    print(f"city {index + 1} : {city}")
print("--------------------------------------------------------")

#8. Using else with for Loops

for city in cites:
    print(city)
else:
    print("no city found")
print("----------------------------------------------------------")

#9. Real-Life Example: Distributing gift

gift = 5
friends = ["anil", "shiva", "sanju", "sharath"]

for friend in friends: 
    if gift > 0: 
        print(f"{friend} got gift!")
        gift -=1
    else:
        print("no gift left")

