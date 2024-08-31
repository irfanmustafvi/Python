Greetings = "Hello world, This is Second day with python."
print(Greetings)
## 3/6, 7, 8, 9 (Variable, Input, Output, Syntax)
# Basics of python day two
line01 = "********************"
line02 = "*                  *"
line03 = "*     WELCOME!     *"
line04 = "******************"

# Indentation in python

# Start with blank line
print(" ")
print(line01)
print(line02)
print(line03)
print(line02)
print(line01)


# Naming Rules
## Only contains alphanumeric characters & underscores
## Starts with letters or underscores
## No spaces
## Case-sensitive
## Cannot be python keywords
### name is Age =(assignment operator) & value 36

age = 36
first_name = "yasir"
print(first_name)

x = 7
x = "seven"  # str value
y = 5 * x  # this will print seen 5 times
a, b, c = "apple", "banana", "orange"
a = b = c = "fish"
print(a, b, c)

x = "three"
print(x * 3)


# Key aspects of Python syntax

##Indentation: Python uses indentation to define the structure of code blocks.
###Example of Indentation: if x > 10:  do something

##Statements: A complete instruction that performs an action.
###Example of Statement:  x = 25

##Expression: A combination of values, variables, and operators that produce a result.
###Example of Expression: x + 5
###Statement containing an expression: y = x + 5

##Comments: Add notes that explain the purpose of code.
###Example of Comment: #This is a comment & """This is a multi-line comment"""

x = 5
if x > 4:
    print("x is greater than 5")  # standard 4 space identation
elif x == 5:
    print("x is equal to 5")  # 12 space identation
    print("Hi")
else:
    print("x is less then 5")  # 1 space identation
