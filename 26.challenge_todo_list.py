"""In this challenge,
1. Create a todo list by reading from and writing to a text file! 
2. A menu with options to view the tasks, 
3. Add new tasks, and 
4. Quit the program should be displayed to the user. 
The program should continue to run until the user chooses the option to end it.

OPTIONAL TASK (but strongly encouraged): Add error handling. This could be done by 
using try/except blocks to catch exceptions, conditionals to validate input, or 
a combination of both.

OPTIONAL ADVANCED: Add an option to remove tasks from the todo list. It is a 
difficult task to remove a single line from a file. It involves reading the 
file's contents into a list, choosing the element to remove and removing it 
from the list, then overwriting the contents of the file with the remaining 
contents of the list.

HINT: To help with outputs to the console/terminal, the string method `strip()'
removes the '\n' character from the end of a string."""


## 1. Create a function that reads the tasks from the file and outputs them to console.
## If there are no tasks, output a message indicating that.
def view_tasks():
    try:
        with open("todo_list.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found!")
            else:
                index = 1
                print("\nTasks ToDo:")
                for task in tasks:
                    print(f"{index}: {task.strip()}")
                    index += 1
    except FileNotFoundError:
        print("No tasks found!")


"""The `view_tasks` function tries to open a file called 'todo_list.txt' and read its contents. 
If the file does not exist or exists and contains no contents, "No tasks found!" is output. 
Otherwise, a for loop is used to output the contents with an index number next to each item. 
The `strip` method is used on each line of the file to remove any unnecessary white space, 
including the newline character."""


## Create a function that adds a new task to the todo list text file.
def add_task():
    new_task = input("Enter a new task: ")
    with open("todo_list.txt", "a") as file:
        file.write(f"{new_task}\n")
    print("Task added successfully!")


"""The `add_task` function adds an item to the 'todo_list.txt' file. First, it gets input from 
the user to add a task to the file. Then, it opens the file in 'append' mode and appends the 
new task to the end of the file. Finally, it outputs that the task was added successfully."""


## REMOVE a task from the todo list
def remove_task():
    print("\n== Remove a task ==")
    try:
        with open("todo_list.txt", "r") as file:
            tasks = file.readlines()

        index = 1
        for task in tasks:
            print(f"{index}: {task.strip()}")
            index += 1
        print(f"{index}: Return to Main Menu")

        choice = int(input(f"Enter task number to remove: "))
        if choice == index:
            return
        removed_task = tasks.pop(choice - 1)

        with open("todo_list.txt", "w") as file:
            file.writelines(tasks)
            print(f"**{removed_task.strip()}** removed successfully!")
    except:
        print("Something went wrong! Returning to main menu.")
        return


"""The `remove_task` function removes an item from the 'todo_list.txt' file. It uses a try/except 
block that outputs a basic message should any errors occur.
The file is opened in read mode, and a list of the file's contents is populated 
using the `readlines` method. 
It outputs each task and an option to return to the main menu with a number next to it. 
It gets input from the user for a task to remove or return to the main menu. 
If the user chooses to remove a task, the task is popped from the `tasks` list and 
stored in the variable `removed_task`.
The remaining contents of the `tasks` list are written back to the 'todo_list.txt' file, 
and the removed task is output with a message that removal was successful."""

## CREATE a loop that presents the user options to view and add tasks and quit the program.
## It should continue to run until the user chooses to quit.
print("=== To-Do List ===")
while True:
    print("\nMenu Options:")
    print("1. View Tasks")
    print("2. Add New Task")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

"""The while loop continues to run until the user enters '4' to quit. 
Each loop iteration, the user is presented with menu options, and depending on their 
choice, the appropriate function is called, or the program ends."""
