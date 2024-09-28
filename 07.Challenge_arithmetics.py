"""Challenge, we are going to practice performing arithmetic operations in Python. Two variables have been provided to perform operations on, and put the result in the variable named `result` to be printed to the console. 
"""

# x, y, and result variables for you to perform operations and store the values
x = 25
y = 3
result = None
# Add the variables x and y together
result = x + y
print(result)  # Output 28
# Subtract y from x
result = y - x
print(result)  # Output -22
# Multiply y and x together
result = y * x
print(result)  # Output 75
# Use regular division to divide x by y
result = x / y
print(result)  # Output 8.333333333333334
# Use floor division to divide x by y
result = x // y
print(result)  # Output 8
## Use the modulo operator to get the remainder of x divided by y
result = x % y
print(result)  # Output 1
## Use exponentiation to raise y to the power of x
result = y**x
print(result)  # Output 847288609443
## Use multiple operators to perform complex operations to understand the order of precedence
result = x + y / (x - y) ** y
## Print the result to the console
print(result)  # Output 25.000281743050337
