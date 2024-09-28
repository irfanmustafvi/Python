## Section 17/97 Naming convention
## Section 17/98 Mutable Objects: Shallow and Deep Copies
def reverse_list(my_list):
    print(f"my_list before reversing: {my_list}")
    my_list.reverse()
    print(f"my_list after reversing: {my_list}")


cars = ["ford", "chevy", "dodge"]
reverse_list(cars)
print(f"cars list after calling reverse_list: {cars}")
#############################################################
import copy

numbers = [1, 2, 3, [4, 5, 6]]
exact_copy = numbers
shallow_copy1 = numbers.copy()
shallow_copy2 = numbers[:]
shallow_copy3 = copy.copy(numbers)
deep_copy = copy.deepcopy(numbers)


if numbers is exact_copy:
    print("Yes! numbers and exact_copy are the same object!")
#####################################################
if numbers == exact_copy == shallow_copy3 == deep_copy:
    print("all 5 lists have the same values!")
###############################################################
if numbers is shallow_copy1:
    print("numbers and shallow_copy1 are the same object")
else:
    print("numbers and shallow_copy1 are not the same object")
#############################################################
if numbers[3] is shallow_copy1[3]:
    print("The list in numbers and shallow_copy1 are the same object")
####################################################
shallow_copy1[0] = 7
shallow_copy1[3][1] = 8
print(numbers, shallow_copy1)
####################################################
if numbers[3] is deep_copy[3]:
    print("The list in numbers and deep_copy are the same object")
else:
    print("the list in numbers and deep_copy are NOT same object")
#####################################################
deep_copy[0] = 7
deep_copy[3][1] = 8
print(numbers, deep_copy)


########################################################
## Section 17/ 99 Common Pitfalls
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list


print(add_item("dog"))
print(add_item("cat"))
print(add_item("rabbit"))


#####################################################
def add_item(item, my_list=None):
    if my_list == None:
        my_list = []
    my_list.append(item)
    return my_list


print(add_item("dog"))
print(add_item("cat"))
print(add_item("rabbit"))
#######################################################
animals = ["kangaroo", "lion", "tiger", "bear"]
for animal in animals:
    print(animal)
    if animal == ("lion"):
        animals.remove(animal)
###############################################
animals = ["kangaroo", "lion", "tiger", "bear"]
for animal in animals[:]:
    print(animal)
    if animal == "lion":
        animals.remove(animal)

print(animals)  # Output ['kangaroo', 'tiger', 'bear']
###########################################################
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(f"list1 after appending 4 to list2: {list1}")
## Output list1 after appending 4 to list2: [1, 2, 3, 4]

x = 10
y = x
y = 20
print(f"x after changing y to 20: {x}")
## Output x after changing y to 20: 10
#########################################################
x = 0.1
y = 0.2
z = x + y
print(z)  # Output is 0.30000000000000004
