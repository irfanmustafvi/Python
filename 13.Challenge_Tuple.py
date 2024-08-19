"""For this challenge, haands-on practice working with tuples. For each activity to 
succeed, always use correct indexing.
"""

# First Tuple containing elements with these data types to work with
tuple1 = ("hello", 50, 3.14, False)
# Here is second tuple by slicing the second and third element from the first tuple
tuple2 = tuple1[1:3]
# Here is third tuple by concatenating the first and second tuple.
tuple3 = tuple1 + tuple2
# Output of three tuples
print(tuple1)
print(tuple2)
print(tuple3)

# Output 1st element in 1st tuple.
print(tuple1[-4])  # > Output: hello

# Using indexing, output the number of times 1st element from 2nd tuple occurs in 3rd tuple
# (should be more than 1) and output it.
print(tuple3.count(tuple2[0]))  # > Output: 2

# Find the index of where 2nd tuple's 2nd element occurs in 1st tuple and output is
print(tuple1.index(tuple2[1]))  # Output: 2

# Concatenate the three tuples and output
print(
    tuple1 + tuple2 + tuple3
)  # Output: ('hello', 50, 3.14, False, 50, 3.14, False, 'hello', 50, 3.14, False, 50, 3.14, False)

# Pack the three tuples into a `result` variable and output
result = tuple1, tuple2, tuple3
print(
    result
)  # Output: (('hello', 50, 3.14, False), (50, 3.14, False), ('hello', 50, 3.14, False, 50, 3.14, False))

# Output the 2nd tuple repeated 3 times
print(tuple2 * 3)  # Output:(50, 3.14, False, 50, 3.14, False, 50, 3.14, False)
