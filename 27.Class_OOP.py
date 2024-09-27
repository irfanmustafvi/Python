### Section 16/89 Classes, Creating Classes
# class Person:
#     fname = ""
#     lname = ""


# p = Person()
# p.fname = "Jesse"
# p.lname = "warner"
# print(p.fname, p.lname)


##################################################
# class Person:
#     fname = ""
#     lname = ""


# Person.fname = "bob"
# p = Person()
# p.lname = "warner"
# print(p.fname, p.lname)
#######################################################
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.weight = "Unknown"


# dog1 = Dog("Max", 3)
# dog2 = Dog("Bella", 2)


# print(f"{dog1.name} is {dog1.age} years old!")
# print(f"{dog2.name} is {dog2.age} years old!")
####################################################
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.weight = "Unknown"

#     def bark(self):
#         print(f"{self.name} barks!")


# dog1 = Dog("Max", 3)
# dog2 = Dog("Bella", 2)
# dog1.bark()
# dog2.bark()
############################################################
# class counter:
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         counter.count += 1


# counter1 = counter("one")
# print(f"counter {counter1.name} count: {counter1.count}")


# counter2 = counter("two")
# print(f"counter {counter1.name} count: {counter1.count}")
# print(f"counter {counter2.name} count: {counter2.count}")
###################################################################
# class counter:
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         counter.count += 1


# counter1 = counter("one")
# counter2 = counter("two")
# counter2.count = 7
# counter3 = counter("three")
# print(f"counter {counter1.name} count: {counter1.count}")
# print(f"counter {counter2.name} count: {counter2.count}")
# print(f"counter {counter3.name} count: {counter3.count}")
# print(f"counter variable: {counter.count}")
###################################################################
## SECTION 15/90 Classes and Static method
# class date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day


# date1 = date(2024, 3, 17)
# print(f"year: {date1.year}\nmonth: {date1.month}\nday: {date1.day}")
#######################################################################
# class date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day

#     @classmethod
#     def from_string(cls, date_str):
#         year, month, day = map(int, date_str.split("-"))
#         return cls(year, month, day)


# date1 = date.from_string("2024-9-17")
# print(f"year: {date1.year}\nmonth: {date1.month}\nday: {date1.day}")
## output is same year:24 month:9 day:17
####################################################################################
# class date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day

#     @classmethod
#     def from_string(cls, date_str, sep="-"):
#         year, month, day = map(int, date_str.split(sep))
#         return cls(year, month, day)


# date1 = date.from_string("2024/9/17", "/")
# print(f"year: {date1.year}\nmonth: {date1.month}\nday: {date1.day}")
########################################################################
# class date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day

#     @classmethod
#     def from_string(cls, date_str, sep="-"):
#         year, month, day = map(int, date_str.split(sep))
#         return cls(year, month, day)


# date1 = date.from_string("2024$9$17", "$")
# print(f"year: {date1.year}\nmonth: {date1.month}\nday: {date1.day}")
#####################################################################################
## STATIC METHOD
# class mathutility:
#     @staticmethod
#     def add(a, b):
#         return a + b

#     @staticmethod
#     def multiply(a, b):
#         return a * b

#     @staticmethod
#     def square(a):
#         return a**2


# add = mathutility.add(1, 2)
# multiply = mathutility.multiply(3, 4)
# square = mathutility.square(6)


# print(f"add: {add}\nmultiply: {multiply}\nsquare: {square}")
###################################################################
## SECTION 15/91 Class Magic Method
# class Car:
#     def __init__(self, color, make, model, year):
#         self.color = color
#         self.make = make
#         self.model = model
#         self.year = year

#     def __str__(self) -> str:
#         return f"A {self.color} {self.make} {self.model} made in {self.year}"


# car1 = Car("Black", "Chevy", "Silverado", 2023)
# car2 = Car("Red", "Ford", "Explorer", 2020)
# print(car1)  # Output A Black Chevy Silverado made in 2023
# print(car2)  # Output A Red Ford Explorer made in 2020


################################################################################
# class Car:
#     def __init__(self, color, make, model, year):
#         self.color = color
#         self.make = make
#         self.model = model
#         self.year = year

#     def __str__(self) -> str:
#         return f"A {self.color} {self.make} {self.model} made in {self.year}"

#     def __eq__(self, other) -> bool:
#         if isinstance(other, Car):
#             return (
#                 self.make == other.make
#                 and self.model == other.model
#                 and self.year == other.year
#             )
#         return False


# car1 = Car("Black", "Chevy", "Silverado", 2023)
# car2 = Car("Red", "Ford", "Explorer", 2020)
# car3 = Car("Blue", "Chevy", "Silverado", 2023)
# print(car1 == car2)
# print(car1 == car3)
#################################################################################################
## Section 15/92 Inheritance class
# class Desert:
#     def __init__(self, name, flavor):
#         self.name = name
#         self.flavor = flavor

#     def cook(self):  # inheritance derived from class
#         print(f"You bake the {self.flavor} {self.name}!")


# class Cookie(Desert):
#     def dunk(self):
#         print(f"You dunk the {self.name} in milk!")


# pie = Desert("pie", "apple")
# cookie = Cookie("cookie", "chocolate chip")


# pie.cook()  # output You bake the apple pie!
# cookie.cook()  # Output You bake the chocolate chip cookie!
# # pie.dunk() # Output is error Attribute Error
# cookie.dunk() # Output You dunk the cookie in milk!
##############################################################################
# class Desert:
#     def __init__(self, name, flavor):
#         self.name = name
#         self.flavor = flavor

#     def cook(self):  # inheritance derived from class
#         print(f"You bake the {self.flavor} {self.name}!")


# class Cookie(Desert):
#     def __init__(self, name, flavor, price):
#         # Desert.__init__(self, name, flavor)
#         super().__init__(name, flavor)  # output 4.99
#         self.price = price

#     def dunk(self):
#         print(f"you dunk the {self.name} in milk!")

#     def bake_and_sell(self):
#         super().cook()
#         print(f"You sell the {self.flavor} {self.name} for ${self.price}!")


# tart = Cookie("cookie", "cherry tart", 6.99)  # Output You bake the cherry tart cookie!
# cookie = Cookie(
#     "cookie", "chocolate chip", 4.99
# )  # output You bake the chocolate chip cookie!
# tart.bake_and_sell()  # output You sell the cherry tart cookie for $6.99!
# cookie.bake_and_sell()  # output You sell the chocolate chip cookie for $4.99!
############################################################
##Practice all above #####################################################
## Section 16/93 Error Handling
# def positive_value(x):
#     if x < 0:
#         raise ValueError
#     else:
#         print(f"The value {x} is positive")
# try:
#     positive_value(-2)
# except ValueError as e:
#     print("error:", e) # Output Error:
#####################################################################
# print("error:", e)  # Output Error:x should be a positive value!
####################################################################################
## Custom exceptions
# class InvalidEmailError(Exception):
#     def __init__(self, message):
#         super().__init__(f"Invalid email address: {message}")
#         self.message = message


# def validate_email(email):
#     if "@" not in email or "." not in email:
#         raise InvalidEmailError(email)


# try:
#     email = input("Enter an email address: ")
#     validate_email(email)
#     print("Email is valid:", email)
# except InvalidEmailError as e:
#     print("Error:", e)
###############################################################################
## Section 15/94 Classes Polymorphism
## Main class in Object Oriented Program
class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        print(f"{self.name} attacks!")


class Dragon(Monster):
    def __init_(self, name, health, element):
        super().__init__(name, health)
        self.element = element

    def attack(self):
        print(f"{self.name} breaths {self.element}!")


class Goblin(Monster):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon

    def attack(self):
        print(f"{self.name} swings a {self.weapon}!")


class Cat:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print(f"{self.name} attacks the string!")


def attack(monster):
    monster.attack()


rat = Monster("rat", 10)
goblin = Goblin("goblin", 100, "sword")
cat = Cat("Mittens")

attack(rat)  # Output rat attacks!
attack(goblin)  # Output goblin swings a sword!
attack(cat)  # Output Mittens attacks the string!
