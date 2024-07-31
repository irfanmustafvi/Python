# This is Exercise=1 for Input & Output
print("this is exercise file in python")
name = input("Enter user name    ")  # We can get user input
print(
    "My Name is " + name
)  # add both string {alpha numeric} that is my name is AND +name


# This is Exercise=2 for Name and Age of user input
print("This is Exercise=2 input variables")
name = input("Enter name ")
age = input("Enter age ")
print("My name " + name + " and my age is  " + age)


# This is Exercise=3 for add two number user input
print("This is Exercise=3 Add two numbers in python as input with output")
n1 = int(input("enter 1st number"))  # should be '4'  ->use integer for 4 number
n2 = int(input("nter 2nd number"))  # should be '5'  ->use integer for 5 number
result = n1 + n2
print("Sum of both number =" + result)

# ERROR Handling
print("This is Exercise=3 Add two numbers in python as input with output")
n1 = int(input("enter 1st number "))  # should be '4'  ->use integer for 4 number
n2 = int(input("enter 2nd number "))  # should be '5'  ->use integer for 5 number
result = n1 + n2
print("Sum of both number =" + str(result))  # result is also convert string number
