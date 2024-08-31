# SECTION 12/66 Functions: Intro
def print_greeting():  # functions signature without parameter
    print("Hello, welcome to functions!")  # body of function


print_greeting()


###################################################
def add(a, b):
    print(a + b)


add(5, 20)


#####################################################
def add(a, b):
    return a + b


result = add(5, 35)
print(result)
#######################################################


# SECTION 12/67
def add():
    pass  # pass kw used to remove error


print("Hi")


###########################################################
def add():
    pass


print(add())  # output is none
###########################################################
if 10 > 20:
    pass  # No output that means no errors
# ###############################################################
for i in range(3):
    pass  # no output means no error


##################################################################
# SECTION 12/68 Keyword Argu,emt, Parameter, Multiple Returns
def greet(name, greeting="Hi"):
    message = f"{greeting}, {name}"
    print(message)


greet("zain")


######################################################################
def greet(name, greeting="Hi"):
    message = f"{greeting}, {name}"
    print(message)


greet("zain", "How are you?")


#######################################################################
def calculate_pyramid_volume(length, width, height=1):
    volume = (length * width * height) / 3
    print(volume)


calculate_pyramid_volume(width=5, length=2, height=5)


#################################################################
def calculate_letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    else:
        return "F"


print(calculate_letter_grade(60))


##################################################################
# >>>> SECTION 12/69 TypeHinting & Docstring
def calculate_pyramid_volume(length, width, height=1):
    return (length * width * height) / 3


result = calculate_pyramid_volume(6, 4, 10)
print(result)


#################################################################
def calculate_pyramid_volume(
    length: "int | float", width: "int | float", height: "int | float"
) -> float:
    return (length * width * height) / 3


result = calculate_pyramid_volume(5, 5, 5)
print(result)


##############################################################################
## Docstring
def calculate_pyramid_volume(
    length: "int | float", width: "int | float", height: "int | float"
) -> float:
    volume = (length * width * height) / 3
    return volume


result = calculate_pyramid_volume(length=5, width=5, height=5)
print(result)


######################################################################################################
# >>> SECTION 12/70 Packing Return Value & Unpacking Args
def get_circle_info(radious):
    pi = 3.14159
    area = pi * radious**2
    circumfrence = 2 * pi * radious
    return area, circumfrence, pi


print(get_circle_info(5))


##################################################################################
def get_circle_info(radious):
    pi = 3.14159
    area = pi * radious**2
    circumfrence = 2 * pi * radious
    return area, circumfrence, pi


# a, c, b = get_circle_info(5.0)
a = get_circle_info(5.0)
print(a)


###################################################################################
##Unpack the calls
def calculate_pyramid_volume(
    length: "int | float", width: "int | float", height: "int | float"
) -> float:
    return (length * width * height) / 3


my_list = [5, 4, 3]
my_tuple = (5, 4, 3)
my_dict = {1: 5, 2: 4, 3: 3}
result = calculate_pyramid_volume(*my_list)
result = calculate_pyramid_volume(*my_tuple)
result = calculate_pyramid_volume(*my_dict)
result = calculate_pyramid_volume(*my_dict.values())
print(result)


######################################################################################
# >>> 12/71 Arguments Syntax
def calculate_sum(*args):
    total = 0
    for num in args:
        total += num
    return total


# result = calculate_sum(1, 2, 3, 4)
result = calculate_sum(1, 2, 3, 4, 5, 6, 16, 32, 6)  # output 75
print(result)


#######################################################################################
def calculate_sum(*args):
    return sum(args)  # same output 75


result = calculate_sum(1, 2, 3, 4, 5, 6, 16, 32, 6)
print(result)


#######################################################################################
def animal_names(species, *names):  # positional args before variable args
    # def animal_names(*names, species):
    # TypeError, animal_names() missing 1 required keyword-only argument: 'species'
    name_str = ",".join(names)
    message = f"{species} names: {name_str}"
    return message


result = animal_names("cat", "whiskers", "mitton", "shadow")
result = animal_names("dog", "max", "bella", "tobi", "luna")
result = animal_names(
    "max", "bella", "tobi", "luna", species="dog"
)  # when put species = dog then output is correct
print(result)


###########################################################################################
## Args positional keyword
def describe_animals(animal_type, *names, habitat="unknown"):
    animal_list = ",".join(names)
    description = (
        f"The {animal_type}animals in the {habitat} habitat are:" f"{animal_list}."
    )
    return description


# result = describe_animals("lion ", "simba", "mufasa", habitat="sawamah")
result = describe_animals("Giraffe ", *["spike", "  melvin"], habitat="grossland")
print(result)


###############################################################################################
def describe_animals(
    animal_type, *names, habitat="unknown"
):  # always use the positional arguments in sequence
    animal_list = ",".join(names)
    description = (
        f"The {animal_type}animals in the {habitat} habitat are:" f"{animal_list}."
    )
    return description


result = describe_animals("monkey ", "coco", "banana")
print(result)


###################################################################################################
def describe_animals(
    animal_type, habitat="unknown", *names
):  # output without the unknown word
    animal_list = ",".join(names)
    description = (
        f"The {animal_type}animals in the {habitat} habitat are:" f"{animal_list}."
    )
    return description


result = describe_animals("monkey ", "coco", "banana")
print(result)


#########################################################################################################
##>>> SECTION 12/72 kwargs syntax (Key Words Argumants)
# kwargs dictionary
def print_details(**kwargs):
    print(f"kwargs: {kwargs}")
    for key, value in kwargs.items():
        print(f"{key}:{value}")


# print_details() # output empty dictionary
print_details(name="asad", age=25, city="manama")


#################################################################
def describe_fish(fish_name, **kwargs):
    color = kwargs.get("color", "unknown color")
    habitat = kwargs.get("habitat", "unknown habitat")
    fins = kwargs.get("fins", 0)
    description = f"A {fish_name} is an {color} fish that inhabitats{habitat}."
    f"It has {fins} fins."

    return description


result = describe_fish("Goldfish")
print(result)


####################################################################################
def describe_fish(
    fish_name, fins=0, **kwargs
):  # correct order of positional args and keywords
    color = kwargs.get("color", "unknown color")
    habitat = kwargs.get("habitat", "unknown habitat")
    description = (
        f"A {fish_name} is an {color} fish that inhabitats {habitat}."
        f"It has {fins} fins."
    )

    return description


result = describe_fish("Goldfish", color="red", habitat="ocean", fins=3)
print(result)


#####################################################################################
def process_data(name, *args, age=0, **kwargs):
    print(f"Processing data: {name}")
    print(f"*args arguments: {args}")
    print(f"Age: {age}")
    print(f"**kwargs arguments: {kwargs}")


# process_data()  # output an error missing name argument
# process_data("data 1") # output empty tuple, dictionary, & 0
# process_data("data 2", 1, 2, 3, 4, age=35, city="NY") # output with positional arguments
process_data("data 2", age=40, city="NY", language="English")
######################################################################################################################################################
