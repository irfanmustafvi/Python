# 7/40 Tuples introduction
# numbers = ()  # Empty parentheses creat empty tuples
# numbers = (1, 2, 3)
# numbers = 1  # output 2 without parentheses
# print(type(numbers)) # putput is class int
# numbers = (1,)
# print(type(numbers)) # output is tuple (1 comma change it tuple)
# numbers = len((1, 2, 3, 4))  # output with single parentheses is error. Double parentheses is correct
# print(numbers)
# numbers = tuple()  # output empty aprentheses ()
# numbers = tuple("Hello")  # output ('H', 'e', 'l', 'l', 'o')
# numbers = tuple([1, 2, 3, 4]) # output (1, 2, 3, 4)
# print(numbers)

# 7/41 Tuple: Method, Ops, & Packing
# my_tuple = (1, 3.14, "hi")  # output (1, 3.14, 'hi')
# print(my_tuple)
# print(my_tuple[2]) #output is 'hi'
# print(my_tuple[2] = 'hello') # output error index 'hello'
# print(my_tuple[0:2])  # Slicing Output is (1, 3.14)
# print(my_tuple[0:3:2]) # output (1, 3.14)
my_other_tuple = 1, 2, 3  # output (1,2,3) Packing a tuple
# a, b, c = my_other_tuple #output is 1,2,3 & Unpacking use correct numbers of variable
# print(a, b, c)
# con_tuple = my_tuple + my_other_tuple
# print(con_tuple) # output (1, 3.14, 'hi', 1, 2, 3)
my_tuple = (1, 3.14, "hi", 1, 2, 3)
# print(my_tuple.count(2)) # output 1
# print(my_tuple.count(1)) # output 2
# print(my_tuple.index(3, 1, 5)) # output error not intuple
# print(my_tuple.index(3, 1, 6))  # output is 5
# print(my_tuple.index("hi")) # output is 'hi'
my_tuple = (1, 2, 3) * 3  # output (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(my_tuple)
