#Conditional Statements in Python: if, elif, and else

print("added new line")

#if
time = 20  # 20 represents 8 PM in 24-hour format
if time == 20:
    print("It's time for dinner!")
    print("----------------------------------------------------")

#else
time = 20  # 20 represents 8 PM in 24-hour format
if time == 18:
    print("It's time for dinner!")
else:
    print("It's not a time for dinner")
    print("----------------------------------------------------")

#else-if

time_for_food = 15

if time_for_food == 8:
    print("its a breakfast time")
elif time_for_food == 13:
    print("its a lunch time")
elif time_for_food == 20:
    print("its a time for dinner")
else:
    print("its not a meal time")
    print("----------------------------------------------------")

#Comparison Operators in if Statements (==, !=, <, >, <=, and >=,)

age = 18
if age >= 18:
    print(" you are elegible to vote")
else:
    print("you are not elegibele to vote")
print("------------------------------------------------------")

#Logical Operators in if Statements (and, or, not)

age = 16
has_student_id = True
if age < 18 and has_student_id:
    print("you are elegible to student discount")
else:
    print("you are not elegible to student discount")
print("-----------------------------------------------------")

#another example

age = 80
if age <5:
    print("ticket is free")
elif age <=12:
    print("you get child discount")
elif age >=65:
    print("you get a seniour citizen discount")
else:
    print("you pay the full fare")
print("-----------------------------------------")
#Nested if Statements

day = "saturday"
is_raining = False

if day == "saturday" or day == "sunday":
    if not is_raining:
        print("Lets visit mysore")
    else:
        print("its raining lets stay home")
else:
    print("its not a week end")
print("------------------------------------------")

