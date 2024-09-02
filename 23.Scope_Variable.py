### >>> 13/77 Scope: Where is my variable?
my_global_var = 10


def modify_global():
    print(f"my_global_var: {my_global_var}")


modify_global()  # output my_global_var: 10
#######################################################
my_global_var = 10


def modify_global():
    global my_global_var
    my_global_var = 20


modify_global()
print(f"my_global_var: {my_global_var}")  # output my_global_var: 20
print(
    globals().keys()
)  # output dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'my_global_var', 'modify_global'])
############################################################
my_global_var = 10


def outer_function():
    my_local_var = 25
    print(f"my_local_var: {my_local_var}")
    print(f"my_global_var: {my_global_var}")

    def inner_function():
        my_inner_var = 50
        print(f"my_inner_var: {my_inner_var}")
        print(f"my_local_var: {my_local_var}")
        print(f"my_global_var: {my_global_var}")

    inner_function()


outer_function()  # Output is in scopes below
# my_local_var: 25
# my_global_var: 10
# my_inner_var: 50
# my_local_var: 25
# my_global_var: 10
###############################################################################
for num in range(1):
    loop_var = "created in the for loop"
if loop_var:
    if_var = "Created in an if conditional!"
print(if_var)
print(loop_var)
#############################################################################
# >>> Built in Functions in Python
# str(my_global_var)
# range(1,10, 2)
# float(5)
# int(2.0)
# tuple([1, 2 5])
#############################################################################
car = "chevy"  # Global scope


def outer_car():
    car = "Ford"
    print(f"outer car: {car}")  # Output outer scope

    def inner_car():
        global car
        car = "Dodge"
        print(f"inner car: {car}")  # output inner scope

    inner_car()
    print(f"outer car: {car}")


outer_car()
print(f"outside my function or class car: {car}")
#####################################################
car = "chevy"  # Global scope


def outer_car():
    car = "Ford"
    print(f"outer car: {car}")  # Output outer scope

    def inner_car():
        nonlocal car
        car = "Dodge"
        print(f"inner car: {car}")  # output inner scope

    inner_car()
    print(f"outer car: {car}")


outer_car()
print(f"outside my function or class car: {car}")
