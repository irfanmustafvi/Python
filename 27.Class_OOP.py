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
class Car:
    def __init__(self, color, make, model, year):
        self.color = color
        self.make = make
        self.model = model
        self.year = year

    def __str__(self) -> str:
        return f"A {self.color} {self.make} {self.model} made in {self.year}"


car1 = Car("Black", "Chevy", "Silverado", 2023)
car2 = Car("Red", "Ford", "Explorer", 2020)
print(car1)  # Output A Black Chevy Silverado made in 2023
print(car2)  # Output A Red Ford Explorer made in 2020


################################################################################
class Car:
    def __init__(self, color, make, model, year):
        self.color = color
        self.make = make
        self.model = model
        self.year = year

    def __str__(self) -> str:
        return f"A {self.color} {self.make} {self.model} made in {self.year}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Car):
            return (
                self.make == other.make
                and self.model == other.model
                and self.year == other.year
            )
        return False


car1 = Car("Black", "Chevy", "Silverado", 2023)
car2 = Car("Red", "Ford", "Explorer", 2020)
car3 = Car("Blue", "Chevy", "Silverado", 2023)
print(car1 == car2)
print(car1 == car3)
