# Arithmatic Operators #
""" + Addition = Add operands or concatenates sequences
 - Subtraction = Subract the right operand to the left operand
 * Multiplication = Multiplies operands together to get Sum or Product
 / Division = Divide the left operand by the right operand to produce a Quotient
 // Floor Division = Perform division & return integer in quotient
 % Modulus = Perform division & return the remainder
 ** Exponentiation = Raises the left operand to the power of right operand"""
x = 2
y = 5
result = x + y
print(result)

x = 2
y = 5
result = x - y
print(result)

x = 2
y = 5
result = x * y
print(result)

x = 2
y = 5
result = x / y
print(result)

x = 2
y = 5
result = y // x  # This divide and ans is whole number
print(result)

x = 2
y = 5
result = y % x  # This ans is in remainder
print(result)

x = 2
y = 5
result = y**x  # This power exponent function
print(result)

x = 2
y = 5
result = (
    x + y / x**y
)  # First x**y then y / ans added x (PEMDAS=Parenthesis, Exponent, Multiply, Divide, Add, Subtract )
print(
    result
)  # Addition operator is for Concatenate & Multiplication operator for repeatitions
