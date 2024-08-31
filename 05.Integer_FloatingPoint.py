my_int = int(5.3)
print(my_int)

my_int = int(123)
print(my_int)

my_int = int("123.0")  # when put inverted commas This raise error
my_int = int(20 - 10), (50 / 10), (40 + 25), (25 * 10)
print(my_int)
my_int = int(59658745896541258965 + 32145698745632145698)
print(my_int)

result = abs(-58)  # absolute value result in positive
print(result)

result = min(1, 2, 3, 4, 5, 6, 7)
print(result)

result = max(1, 2, 3, 4, 5, 6, 7)  # cannot be sum without Square Bracket
print(result)

result = min([21, 52, 13, 42, 51, 16, 17])
print(result)

result = sum([21, 52, 13, 42, 51, 16, 17], 22)  # sum is done with square bracket
print(result)

result = pow(5, 3, 17)  # 5*5*5=125/17=6
print(result)

result = divmod(28, 3)  # Result 28/3= whole number, remainder
print(result)

result = divmod(28, 4)  # diviide mod functions
print(result)

# Float Numbers = Float always be with decimal 12 = 12.0 only when in brackets
my_float = 1.2
print(my_float)
my_float = float(65)
print(my_float)
my_float = float(3.4)
print(my_float)
my_float = 6 + 5  # Here no bracket So result =11
print(my_float)
my_float = 6.5 + 8
print(my_float)
my_float = 0.258963147951324568  # float number < 17 after decimal only 17 digit show
print(my_float)
my_float = 123654789.123654987  # Here after decimal last numbers can be rounded off.
print(my_float)
my_float = 1236547891236549889
print(my_float)
my_float = 1236547890123654789 + 123654789  # to convert int function
result = int(my_float)
print(my_float)
x = 0.1
y = 0.2
z = x + y  # if x=0.1 & y=0.2 then result is long value 0.30000000000000004
print(z)
