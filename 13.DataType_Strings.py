# String multi line function
# greeting = "Hello: "
# question = " How are you?"
# message = greeting + question
# print(message)

# greeting = "Hello:"
# question = "How are you?"
# message = greeting + " " + question
# print(message)

# Repeating variable
# laugh = "ha"
# laugh *= 3
# print(laugh)

# multi-line string variable  ## """"ad """ three quotes are used to write multi line code i string
# multi_line = """"This is multi line transcript to
# evaluate the script in string"""
# print(multi_line)

# built in length function
# password = "password123456"
# pw_length = len(password) # total item in password are sum up
# print(pw_length)

# Indexing # here number of item {letter} is printed as mention as my_string[8]
# my_string = "Hello world"
# print(my_string[0])

# Slicing # here we put {colon} is printed as complete string
# my_string = "Hello world"
# print(my_string[:])
# my_string = "Hello world"  # Ranges left side of colon and right side of colon
# print(my_string[:5])
# my_string = "Hello world!"  # Ranges left side of colon and right side of colon
# print(my_string[-6:])
# my_string = "Hello world!"
# print(my_string[1:10:1])

### All from (Docs Python.org) @ String Methods
# my_string = "hello world!"  # When we put dot in print function > different types of functions are listed.
# print("this is long string".capitalize())  # this will change first letter capital

# my_string = "Hello World!"  # casefold function
# print(my_string.casefold())  # this will change first letter to lowercase

# Section 26 Count String
# my_string = "abababababa"
# print(my_string.count("aba", 4, 7))
# my_string = "you know as you do"
# print(my_string.find("z"))
# my_string = "you know as you do"
# print(my_string.index("z"))
# my_string = "you know as you do"  # True value the key word yes
# print("you" in my_string)
# my_string = "you know as you do"  # False value the key word no
# print("your" in my_string)

# Section 27
# space_string = "          Too many space more than ten          "
# dash_string = "--- too many dashes---"
# symbol_string = "<@>?#% ****** !~ Too many symbols_^~!@#$%^&"
# quot = "It is not a bug, it is a feature"
# print(space_string.strip())  # This string move left side
# print(dash_string.lstrip("-")) #left side dashes are removed
# print(dash_string.rstrip("-"))
# print(symbol_string.strip("<@>?#%*^&"))
# print(quot.startswith("It"))
# print(quot.endswith("re"))
# print(quot.replace(" ", "-")) # this convert (It-is-not-a-bug,-it-is-a-feature)
# print(quot.replace(" ", "-", 3))  # This convert in (It-is-not-a bug, it is a feature)
# print(quot.split())  # ['It', 'is', 'not', 'a', 'bug,', 'it', 'is', 'a', 'feature']
# print(quot.split("is"))  # this will remove "is" & replace with commas
# print(dash_string.strip("-").upper().split()) # all convert to uppercase.
# my_list = dash_string.strip("-").upper().split()
# print(" ".join(my_list))  # nthis way joined the words
# print("---".join(my_list))
# print(" : ".join(dash_string))

# Section 28 Escape Character in String
# my_string = "Hello,wo\\rld!" # back slash function
# print(my_string)
# my_string = "Hello,'world!'"  # Double quotes
# my_string = "hello, 'world'"
# my_string = "Hell0 \nworld, this is line \nseparation"  #  New line character \n
# my_string = "Hell0 \tworld, this is line \tseparation"  # \t for tab space in line
# my_string = "Hello \rworld"  # \r line starts from here, before words are deleted
# my_string = "Hell0 world, \bthis is \tseparation"  # \b remove backspace character
# my_string = "Hell0 \x0aworld, "  # This also separate line
# my_string = "Hell0 world, \u263a"  # this will add smile face
# my_string = "Hell0 world, \N{snowman}"
# print(my_string)

# Section 29 Formating of string CHECK From Py Docs
# name = "zia"
# age = 28
# job = "developer"
# person_string = "Manager name is {}, {} is age {}; and job {}"
# person_string = (
#     "Manager name is {2}, {2} is age {0}; and job is {1}"  # Indexing the variable
# )
# person_string = "Manager name is {_name}, {_name} is age {0}; and job {1}"  # Key variable(name changed) pair
# # print(person_string.format(age, job, name))  # Format function is used for
# # print(person_string.format(age, job, _name="Dasmon"))
# person_string = f"Manager name is {name}, {name} is age {age}; and job {job}"  # Best method for format
# # print(person_string)
# pi = 3.141592
# pi_str = f"the value of pi approximately {pi:0.4f}"  # 0.4f present digit after decimal
# pi_str = f"the value of pi approximately {pi:>20}"  # :> increases space
# print(pi_str)

# Section 30- Mad Lib Challenge
"""
In this challenge, going to create a mad lib generator! You should 
start by printing a welcome message to the console. Then, get user input for a 
noun, verb, adjective, and adverb and store the values in variables. After 
that, format a string to tell a short story using the user's inputs and store 
it in a variable. Finally, output the story to the console.
"""

# Print a welcome message to the console

# Get inputs for a noun, verb, adjective, and adverb and store them in variables

# Format a string be a story with the 4 user inputs and store in in a variable

# Print the formatted story string to the console
