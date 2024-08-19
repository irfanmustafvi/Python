# Section 6/33 lists
my_list = ["cat", "dog"]
my_list = list()  # Empty list
my_list = list("cat")  # This print each character separate if list not found.
my_list = list(["cat"])  # when put square bracket then single item is pronted
my_list = ["cat", "dog"]
my_list.append(1)
my_list.append("cow")
my_list = ["cat", "dog", "cow"]
my_otherlist = ["horse", "duck"]
my_list.insert(1, "duck")  # This onsert before number of character.
my_list = ["cat", "dog", "cow"]
my_otherlist = ["horse", "duck"]
my_list.extend(my_otherlist)  # This combine both lists
my_list += my_otherlist
print(my_list)

## Section 6/34 # Indexing
my_list = ["cat", "dog", "cow", "horse", "duck"]
my_list[0] = "camel"  # Change the name variable in index
print(my_list)
# Slicing
my_list = ["cat", "dog", "cow", "horse", "duck"]
print(my_list[0:4])
print(my_list[0:5:4])  # this give gap in items
print(len(my_list))  # This give total number of items
my_list = ["cat", "dog", "cow", "horse", "duck", "dog"]
print(my_list.remove("dog"))  # Output will be none
del my_list[1]  # from list number(#) item deleted
print(my_list.pop())  # the result is last item (-)
print(my_list.pop(3))  # when put index number of item that should be out of list
print(my_list)
# Removing Elements
my_list.clear()  # result empty list []
print(my_list)

## 6/35 List change order of element
animals = ["dog", "cat", "cow", "horse", "duck", "goat", "chicken"]
print(animals)
print(animals.sort())  # output none
print(animals)  # result is sorted list
print(animals.sort(key=len))  # output is sorted from short to long spelling
print(animals.sort(key=len, reverse=True))  # this will reverse order from long-short
print(animals.reverse())
result = sorted(animals)
result = sorted(animals, key=len)  # sorted by length short - long
result = sorted(animals, key=len, reverse=False)  # sortrd by short -long with false
result = sorted(animals, key=len, reverse=True)  # sorted by long-short with true
result = sorted("Hello , World!")  # This is not perfect function to sort
print(result)

## 6/37 Lists: Multiple Dimensional
matrix = [
    [1, 2, 3],
    [4, [1, 2, [1, 2, 3], 3], 6],
    [7, 8, 9],
]  # List inside a nested list
print(matrix[2][0])
print(matrix[1][1][2][0])

## 6/38 Lists Comprehension
numbers = [1, 2, 3, 4, 5, 6]
new_list = [
    num**2 for num in numbers
]  # Expression is num**2, for num is item, in iterable(numbers)
new_list = [
    num for num in numbers if num % 2 == 0
]  # condition to separate even numbers
print(new_list)
my_list = [0] * 10  # output will be ten zeros
my_list[2] = 4  # This 0 replaces at index 2 with 4
my_list = [[]] * 10  # This create ten empty lists & this is immutable object
my_list = [[] for i in range(10)]  # This also give empty list
my_list[2].append(4)  # this replace 0 at 2 index with 4 & append for immutable objects
print(my_list)
