## 8/44 section data sets
my_set = {1, 2, 3, 2, 3}
print(my_set)  # output {1, 2, 3} by ignore (2, 3)
my_set = {}
print(my_set)  # output {}
my_set = set{} # with curly braces { } give error
my_set = set()  # output set()
my_set = set([1, 2, 3])  # output curly braces {1,2,3}

## 8/45 Adding/Removing Elements
my_set = {1, 2, 3}
my_set.add([4]) # Output type error so number must be part of set
my_set.remove(4)  # output keyerror:4
my_set.remove(1) # output {2, 3}
my_set.discard(4)  # output will be remain as {1, 2, 3} [4 is not part of set]
my_set.discard(2)  # output is {1, 3}
my_set.clear()  # output empty set()
del my_set # output is naming error
my_set = {3, 2, 1}  # output is {1, 2, 3}
my_set = set("world")
print(my_set.pop(), my_set)  # output r {'w', 'd', 'l', 'o'}
# output order also change  when run again like w {'l', 'o', 'd', 'r'}
# output order w {'l', 'o', 'r', 'd'} . d {'l', 'r', 'o', 'w'}
my_set = {1, 2, 3}
my_other_set = {3, 4, 5}
my_set.update(my_other_set)  # output {1, 2, 3, 4, 5} union of two sets
print(my_set)

## 8/46 Set Methods
my_set1 = {1, 2, 3, 4}
my_set2 = {3, 4, 5, 6}
my_set3 = {1, 2, 3}
my_set4 = {5, 6, 7, 8}
result = my_set1.difference(my_set2) # output {1, 2}
result = my_set1 - my_set2 # output same with subtraction operator{1, 2}
result = my_set1.intersection(my_set2) # output is {3, 4}
result = my_set1 & my_set2 # output same with operator & = {3, 4}
result = my_set1.union(my_set2)  # output union of sets{1,2,3,4,5,6}
result = my_set1 | my_set2 # output same with pipe as in union
result = my_set1.symmetric_difference(my_set2)  # output only difference of both sets
result = my_set1 ^ my_set2 # same output with symbol ^ (alt+94) {1,2,5,6}
my_set1.difference_update(my_set2)  # output {1, 2}= set1
my_set1 -= my_set2  # with operators same eoutput {1,2}
print(my_set1)
## Below are boolean vakues TRue or False
result = my_set1.isdisjoint(my_set2)  # output false if elements are common in 2 sets
result = my_set1.isdisjoint(my_set4)  # True if elements are not common in 2 sets
result = my_set1.issuperset(my_set3)  # True if elements are common in superset
result = my_set3.issuperset(my_set1)  # False if elements are not in superset
result = my_set3.issubset(my_set1)  # True set3 has less element of set1
result = my_set3.issubset(my_set2)  # False set3 has less element of set2
print(result)

