# Create variables to perform conditional operations on
w = -5
x = 5
y = 10
z = 0

# Conditional using an `if` statement where the `if` condition is `True`
if x < y:
    print(f"{x} is less than {y}")  # Output: 5 is less than 10

# Conditional using an `if` statement where the `if` condition is `False` (code
# does not run)
if y < x:
    print(f"{y} is less than {x}")  # Output: No output

# Conditional using the `if` and `elif` statements where the `elif` condition is `True`
if y < x:
    print(f"{y} is less than {x}")
elif y > x:
    print(f"{y} is greater than {x}")  # Output: 10 is greater than 5

# Conditional using the `if` and `elif` statements where no condition is `True`
if y < 10:
    print(f"{y} is less than {x}")
elif y > 10:
    print(f"{y} is greater than {x}")  # Output: No output

# Conditional using the `if`, `elif`, and `else` statements where no condition  is `True`
if z > 0:
    print(f"{z} is positive")
elif z < 0:
    print(f"{z} is negative")
else:
    print(f"{z} is zero")  # Output: 0 is zero

# Conditional using multiple `elif` statements where the third `elif` statement is `True`
if x < 0:
    print(f"{x} is negative")
elif y < 0:
    print(f"{y} is negative")
elif z < 0:
    print(f"{z} is negative")
elif w < 0:
    print(f"{w} is negative")
else:
    print("No negative numbers found")  # Output: -5 is negative

# Conditional with a nested conditional
if x > 0:
    if x % 2 == 0:
        print(f"{x} is positive and even")
    else:
        print(f"{x} is positive and odd")
else:
    print(f"{x} is not positive")  # Output: 5 is positive and odd

# Conditional using the `and` logical operator, so both evaluations must be `True`
if x > 0 and y > 0:
    print(f"Both {x} and {y} are positive")
# Output: Both 5 and 10 are positive
# This conditional evaluates to (True and True), which evaluates to True

# Conditional using the `or` logical operator, so one evaluation must be `True`
if x > 0 or w > 0:
    print(f"Either {w} or {x} is positive")  # Output: Either -5 or 5 is positive
# This conditional evaluates to (True or False), which evaluates to True

# Conditional using the `not` logical operator, so the evaluation immediately
# after the `not` keyword must be false for the entire evaluation to be `True`
if not w > 0:
    print(f"{w} is negative")  # Output: -5 is negative
# This conditional evaluates to (not False), which evaluates to True

# Conditional using the `not`, `and`, and `or` logical operators
if not (x < 0 and w > 0) or (x < 0 and w < 0):
    print(
        f"Either {x} is not negative and {w} is not positive, or {x} is "
        f"negative and {w} is negative"
    )
# Output: Either 5 is not negative and -5 is not positive, or 5 is negative and -5 is negative
# This `if` statement evaluates in the following ways:
# (not (False and False)) or (False and True)
# (not False) or False
# True or False
# True

# Create two variables to use with a ternary operator
a = 10
b = 20
# Set max_value to a if a is greater than b else set max_value to b
max_value = a if a > b else b
print(f"Max value of {a} and {b}: {max_value}")  # Output: Max value of 10 and 20: 20
