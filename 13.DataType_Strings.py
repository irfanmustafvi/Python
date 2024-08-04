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
space_string = "          Too many space more than ten          "
dash_string = "--- too many dashes---"
symbol_string = "<@>?#% ****** !~ Too many symbols_^~!@#$%^&"
quot = "It is not a bug, it is a feature"
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
my_list = dash_string.strip("-").upper().split()
# print(" ".join(my_list))  # nthis way joined the words
# print("---".join(my_list))
print(" : ".join(dash_string))
