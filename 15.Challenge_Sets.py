"""Challenge, to practice working with sets and their methods.
"""

# A set containing the elements 1-4
set1 = {1, 2, 3, 4}

# Create a set containing the elements 3-6
set2 = {3, 4, 5, 6}

# Create a set containing the elements 7-9
set3 = {7, 8, 9}

# Union(add) of all the sets
print(set1.union(set2, set3))  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Intersection of set1 and set2
print(set1 & set2)  # (& used for intersection) so Output {3, 4}
# Symmetric difference between set1 and set2
print(set1 ^ set2)  # (The hat symbol used for symmetric) so output {1, 2, 5, 6}
# Output the difference between set1 and set2, and set2d and set1
print(set1.difference(set2))  # Output: {1, 2}
print(set2 - set1)  # Output: {5, 6}
# Add element 5 in set1 & Remove element 6 from set2
set1.add(5)
set2.remove(6)

# Boolean value of whether the set1 is a superset of set2
print(set1.issuperset(set2))  # Output: True
# Boolean value of whether set2 is a subset of set1
print(set2.issubset(set1))  # Output: True
# Boolean value of whether set1 is a subset of set2
print(set1.issubset(set2))  # Output: False
# Boolean value of whether set3 has no common elements with union of set1 and set2
print(set3.isdisjoint(set1 | set2))  # Output: True

# Modify the set1 in place by adding set2 and set3 to it and (Output should not be None)
set1.update(set2, set3)  # Output: {1, 2, 3, 4, 5, 7, 8}
print(set1)
# Remove all the elements from set2 and print it (Output should not be None)
set2.clear()  # Output: set()
print(set2)
# Delete set3
del set3
