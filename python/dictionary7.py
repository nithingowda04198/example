#Dictionarys in python

karnataka_food = {
    "bangaloor" : "palav",
    "mandya" : "ragi muddhe",
    "mysore" : "mysore pak"
}

print(karnataka_food)
print(karnataka_food["mandya"])
print("--------------------------------------------------")

#Adding and Updating dictionary element.

#Adding
karnataka_food["maddur"] = "maddur vada"
print(karnataka_food)

#Updating
karnataka_food["bangaloor"] = "benne edli"
print(karnataka_food)
print("---------------------------------------------------")

#remove element from dictionary(pop(), del(), and clear())

#pop()
mysore_food = karnataka_food.pop("mysore")
print(mysore_food)
print(karnataka_food)

#del()
del karnataka_food["maddur"]

#clear()
karnataka_food.clear()
print(karnataka_food)
print("---------------------------------------------------")

#dictionery methods(.key(), .value(), .items(), and .update)

bio_student = {
    "name" : "nithin",
    "age" : "twenty seven",
    "city" : "mandya"
}
print(bio_student)

#Keys()
print(bio_student.keys())

#values()
print(bio_student.values())

#items()
print(bio_student.items())

#update()
new_data = {"village" : "k bettahalli"}
bio_student.update(new_data)
print(bio_student)
