"""
For this challenge, we are going to practice performing arithmetic operations 
in Python. Two variables have been provided for you to perform operations on, 
and you should put the result in the variable named `result` to be printed to 
the console. 
"""

# x, y, and result variables for you to perform operations and store the values
x = 25
y = 3
result = None
# Add the variables x and y together
result = x + y
# Subtract y from x
result = y - x
# Multiply y and x together
result = y * x
# Use regular division to divide x by y
result = x / y
# Use floor division to divide x by y
result = x // y
# Use the modulo operator to get the remainder of x divided by y
result = x % y
# Use exponentiation to raise y to the power of x
result = y**x
# Use multiple operators to perform complex operations to understand the order
# of precedence
result = x + y / (x - y) ** y
# Print the result to the console
print(result)
