"""
In this challenge, create a simple calculator! The calculator 
should have functions to do addition, subtraction, multiplication, and 
division. Each function will take two integer arguments and perform the 
operation on the integers passed into it. You will create an options menu for 
the user with an option for each operation and to quit the program. If the user 
chooses an operation, the user will be prompted to enter two numbers for the 
operation to work with. The calculator should continue to run until the user 
decides to quit.
"""


# Create a function to perform addition
# Create a function to perform subtraction
# Create a function to perform multiplication
# Create a function to perform division
# Create the loop that will prompt the user for an option and run until the
# user decides to quit
#####################################################################################
# Addition Function
def add(a, b):
    print(f"\n{a} + {b} = {a + b}\n")


# Subtraction Function
def subtract(a, b):
    print(f"\n{a} - {b} = {a - b}\n")


# Multiplication Function
def multiply(a, b):
    print(f"\n{a} * {b} = {a * b}\n")


# Divide Function
def divide(a, b):
    print(f"\n{a} / {b} = {a / b}\n")


# Complete Prompt to operate functions of calculator
while True:
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Quit")
    choice = int(input("Enter an option (1/2/3/4/5): "))

    if 0 < choice < 5:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        if choice == 1:
            add(a, b)
        elif choice == 2:
            subtract(a, b)
        elif choice == 3:
            multiply(a, b)
        elif choice == 4:
            divide(a, b)
    elif choice == 5:
        print("Thank you for using the simple calculator!")
        break
    else:
        print("\nInvalid input! Try again.\n")


"""
The code inside the loop outputs an option menu for the user. If the user 
chooses an option between 1 and 4, then they are prompted to enter two numbers 
to be used with the mathematical operation they chose. After getting input from 
the user, another conditional uses the option they chose to determine which 
function to pass the inputs to. If the user entered 5 for the option, a thank 
you message is output and the loop ends with the break statement. If the user 
entered anything other than 1-5, the user receives an invalid input message and 
the loop goes to the next iteration.
"""
