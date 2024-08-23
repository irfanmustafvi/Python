## 10/54 Booloean Comparison Operators
a = 5
b = 10
c = 10
result = a == b  # comparison operator, output False because a is not equal b
result = c == b  # output True
result = c != b  # is not equal, output False
result = a != b  # output True
result = c > b  # False
result = b > a  # True
result = b < a  # False
result = a < b  # True
result = a <= b  # True
result = a >= b  # False
result = c >= b  # True
result = "A" > "a"  # Output False( string comparison)
result = "A" < "a"  # output True
result = "aaz" > "az"  # False
result = "aaz" > "aaz"  # False
result = "a" == "a"  # True (sign operator, is equal)
result = "aaz" > "aaaz"  # True
# print(result)

## 10/55 Logical Operators
a = 5
b = 10
c = 10
d = 15
result = a == b  # output True
result = a != b  # False
result = a < b and b < c  # False with & operator
result = a < b and b > c  # False
result = b == c or c == d  # If right side is true then other sidealso trus
result = b != c or c == d  # False
result = b != c or c < d  # True
result = (a < b) and (c > a) or (a == 5)  # True
result = not (a < b or d < a) or b > d  # False (a<b or d<a are true * not)=False
# print(result)

## Just true and false value
result = (
    True or False and not True
)  # First (false & not true)=False # second (true or false)= True
print(result)

## 10/56 is and in operators
str_one = "Hello"
# str_two = "Hello"
str_two = "googdbye"
result = str_one is str_two
result = id(str_one)  # output (1911254264032) unique ID of an object
# Id number also change every click
print(result, id(str_two))
result = str_one is str_two  # False

list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
result = list_1 is list_2  # output False
result = list_1 is not list_2  # output True
list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
list_3 = list_1
# result = list_1 is list_3 # output True
list_1 = [1, 2, 3]
str_one = "Hello world, how are you?"
# result = "how" in str_one # True
result = "h" in str_one  # True
result = "z" in str_one  # False
result = 1 in list_1  # True
result = 1 not in list_1
# print(result)

## 10/57 Truthy and Falsy value
list_1 = [0, 1, 2, 3]
result = bool(1)  # True
result = bool(0)  # False
result = [0, 1, 2, 3]
result = bool(list_1)  # True
result = bool({})  # False
result = any(list_1)  # True
result = all(list_1)  # False
# print(result)
empty_objects = [
    [],  # list
    0,  # Integer
    0.0,  # Float
    "",  # Empty single qupte
    "",  # Empty double quote
    {},  # Empty Dictionary
    (),  # Empty Tuple
    set(),  # Empty set
    frozenset(),  # Empty frozen set
    None,  # none type
    False,  # false
]
# print(any(empty_objects))  # False
non_empty_objects = [
    [1],  # list
    6,  # Integer
    0.0000000001,  # Float
    "a",  # nonEmpty single qupte
    "hi",  # nonEmpty double quote
    {"name": "zain"},  # nonEmpty Dictionary key value
    (3, 4, 5),  # nonEmpty Tuple
    set([1, 2, 3]),  # nonEmpty set
    frozenset([4, 5, 6]),  # nonEmpty frozen set
    True,  # false
]
# print(all(non_empty_objects)) # True

## 10/58 Conditional Intro
"""Conditionals in Python are used to execute different blocks of code based on 
specific conditions. The main conditional statements in Python are `if`, `elif` (short for "else if"), and `else`.
The basic syntax of a conditional statement is as follows:
    if condition:
        Code to be executed if the condition is True

    elif condition:
        Code to be executed if the preceding condition(s) is False and this 
        condition is True

    else:
        Code to be executed if all preceding conditions are False

Key concepts of conditional statements:
    - `if` Statement: It starts with the keyword `if`, followed by a condition. 
      If the condition evaluates to `True`, the code block indented under the 
      `if` statement is executed. If the condition is `False`, the code block 
      is skipped.

    - `elif` Statement: It stands for "else if" and is used to check additional 
      conditions after the `if` statement. It can be used multiple times to 
      check multiple conditions. If the preceding condition(s) in the `if` or 
      `elif` statements are False, and this condition evaluates to `True`, the 
      code block indented under the `elif` statement is executed.

    - `else` Statement: It is used as a fallback option when all preceding 
      conditions are `False`. If none of the preceding conditions in the `if` 
      or `elif` statements evaluate to `True`, the code block indented under 
      the `else` statement is executed.

    - Nested Conditional Statements: You can use conditional statements inside
      of other conditional statements. This allows you to perform more complex 
      decision-making based on multiple conditions.

    - Ternary Operator: It is a concise way to write conditional statements in 
      Python. It allows you to make decisions and assign values based on a 
      condition in a single line of code.
          Syntax:
              value_if_true if condition else value_if_false
"""
x = 6
y = 10
result = "no true statement"
if x < 3:
    result = "x is less thsn three"
elif x == 4:
    result = "x is four"
elif x == 5:
    result = "x is 5"
else:
    result = "x is not less tan 3 or equal to 4"
    # print(result)
    # if x < 10 or x > 3 and y == 10:
    result = "that is correct"
print(result)

## 10/59/1 Nesting Operations
x = 8
y = 10
if x < 100:
    if x % 2 == 0:
        if x < 10:
            result = "x is even and less than 10"
        # result = "x is even"
    elif x % 2 == 1:
        result = "x is odd"
else:
    result = "x is greater than or equal to 100"
print(result)

## 10/59/2 Ternery Operations
x = 100
y = 10
result = "no true statement"
result = x if x < y else y
print(result)
