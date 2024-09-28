"""Challenge, use all the assignment operators to change 
the value of a `number` variable, but the final result will be the same as the 
starting number. Feel free to print `number` to the console after each 
operation to see its value."""

## The `number` variable will start as fifty
number = 50
print(number)  # Output 50

## Use the floor division assignment operator to divide `number` by 8
number //= 8  # this return whole number result
print(number)  # Output 6

## Use the addition assignment operator to increase `number` by 29
number += 29
print(number)  # Output 35

## Use the subtraction assignment operator to reduce `number` by 20
number -= 20
print(number)  # Output 15

## Use the multiplication assignment operator to triple `number`
number *= 3
print(number)  # Output 45

## Use the exponentiation assignment operator to raise `number` to the third power
number **= 3
print(number)  # Output 91125

## Use the modulus assignment operator to divide `number` by 727 and get the remainder
number %= 727
print(number)  # Output 250

## Use the division assignment operator to divide `number` by 5
number /= 5
print(number)  # Output 50.0
