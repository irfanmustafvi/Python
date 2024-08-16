"""In this activity, you are going to practice working with lists, list methods, 
and list comprehension.
"""

# 1- List to work with
numbers = [20, 50, 35, 45, 125]

# 2-Use Python's built-in `sum` function to get the output of all the numbers in the list
print(sum(numbers))  # Output: 275

# 3-Create a new list by using list comprehension to divide each value in the numbers list by 3 and output the new list.
numbers_div = [num / 3 for num in numbers]
print(
    numbers_div
)  # Output: [6.666666666666667, 16.666666666666668, 11.666666666666666, 15.0, 41.666666666666664]

# 4-Output the sum of the new list.
print(sum(numbers_div))  # Output: 91.66667

# 5-In a single statement, output the value of the sum of the numbers list plus
# the sum of the new list, but you can only call the sum function once, and you
# cannot modify the numbers or new list. HINT: Use c___________n
print(sum(numbers + numbers_div))  # Output: 366.67

# 6-Extend the numbers list with a list containing the values 48, 36, and 3.
new_list = [48, 36, 3]
numbers.extend(new_list)
print(numbers)

# 7-Remove and return the first item in the numbers list and print it to the console.
print(numbers.pop(0))  # Output: 20

# 8-Remove and return the last item in the numbers list using negative indexing and print it to the console.
print(numbers.pop(-1))  # Output: 3

# 9-Output the number of times 36 is in the numbers list
print(numbers.count(36))  # Output: 1

# 10-Output the index of 99 in the numbers list
print(numbers.index(48))  # Output: 4

# 11-Using slice notation, output the second through the second to last item of the numbers list.
print(numbers[1:-1])  # Output: [35, 45, 125, 48]

# 12-Insert the value 50 into the numbers list before index 3 and output the list
numbers.insert(3, 50)
print(numbers)  # Output: [55, 35, 45, 50, 125, 48, 36]

# 13-Reverse the list and output it
numbers.reverse()
print(numbers)  # Output: [36, 48, 125, 50, 45, 35, 50]

# 14-Sort the list in ascending order and output the list
numbers.sort()
print(numbers)  # Output: [35, 36, 45, 48, 50, 50, 125]

# 15-Remove all the items from the numbers list and print the empty list.
numbers.clear()
print(numbers)  # Output: []

# 16-Delete the new list to clear it from memory.
del new_list
