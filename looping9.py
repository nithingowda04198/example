#While Loops in Python

i = 1
while i <= 5:
    print(i)
    i+=1
print("------------------------------------------")

sheep_count = 1
while sheep_count <=10:
    print(f"sheep{sheep_count}")
    sheep_count+=1
print("-------------------------------------------")

#using breake in while loop

sheep_count = 1
while sheep_count <=10:
    print(f"sheep{sheep_count}")
    if sheep_count == 5:
        print("that's enough counting!")
        break
    sheep_count+=1
print("---------------------------------------------")

#use continue on while iteration

sheep_count = 1
while sheep_count <=5:
    if sheep_count == 4:
        sheep_count+=1
        continue
    print(f"sheep {sheep_count}")
    sheep_count+=1
print("---------------------------------------------")

#while loop useing input

pin = ""
correct_pin = "0710"
while pin != correct_pin:
    pin = input("enter  your pin!")
    if pin != correct_pin:
        print("incorrect pin. try again!")
print("pin accepted you can proceeded.")
print("---------------------------------------------")
#example 2

availanle_seat = 5
while availanle_seat > 0:
    print(f"{availanle_seat} seats available")
    booking = input("do you want to book a seat? (yea/no):").lower()
    if booking == "yes":
        availanle_seat -=1
        print("seat_booked!")
    else:
        print("seat is not booked")
print("all seats are booed!")
print("--------------------------------------------")

#Nested while loop

snack_available = 3
money = 10

while snack_available > 0 and money > 0:
    print(f"snakes : {snack_available}, money : ${money}")
    buy = input("Do you want buy snacks for $ 5? (yes/No)").lower()
    if buy == "yes" and money >=5:
        snack_available-=1
        money-=5
        print("snack purchased!")
    else:
        print("No purchase made.")
    print("snacks are sould out")

    