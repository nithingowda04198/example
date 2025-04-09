#Introduction to OOP Concepts & Classes/Objects

#Classes and Objects

class car:

    #attribute
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    #method
    def car_details(self):
        print(f"The car brand is -{self.brand} model is{self.model}")

#create object
car1 = car("mahindra", "suv500")
car1.car_details()


print("-----------------------------------------------------------------------------")

#Attributes (Instance Variables) and Methods

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def person_details(self):
        print(f"my name is {self.name} and i am {self.age} year old")

#object
person1 = person("nithin", 27)
person2 = person("shiva", 27)

person1.person_details()
person2.person_details()

print("----------------------------------------------------------------------------")


#Creating Multiple Objects from a Class

class dog:
    def __init__(self, name, breade):
        self.name = name
        self.breade =breade
    
    def dog_bio(self):
        print(f"this is {self.name}, breade is{self.breade}")

#object
dog1 = dog("Rex", "Golden Retriever")
dog2 = dog("Bolt", "Beagle")

dog1.dog_bio()
dog2.dog_bio()