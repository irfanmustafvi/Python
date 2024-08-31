# >>> SECTION 11/73 Functions: Generators
def generator_even_numbers(limit):
    num = 0
    while num <= limit:
        yield num
        num += 2


evens = generator_even_numbers(4)
# print(evens) # Output <generator object generator_even_numbers at 0x0000020CB50DC940>


for num in evens:
    print(num)


########################################################################################
def generator_primes():
    primes = []
    num = 2
    while True:
        if all(num % prime != 0 for prime in primes):
            yield num
            primes.append(num)
        num += 1


prime_generator = generator_primes()
primes = [next(prime_generator) for i in range(100)]
print(primes)  # output [2, 3, 5, 7, 11]


###########################################################################################
def generator_primes():
    primes = []
    num = 2
    while True:
        print(
            num,
            [num % prime != 0 for prime in primes],
            all([num % prime != 0 for prime in primes]),
        )
        if all(num % prime != 0 for prime in primes):
            yield num
            primes.append(num)
        num += 1


prime_generator = generator_primes()
primes = [next(prime_generator) for i in range(4)]
print(primes)  # output with boolean values
#########################################################################################################
# >>> Function Lambda

square = lambda x: x**2
print(square(5))  # output 25

# def sequence(x):
#     return x**2 # No result/ output
numbers = [1, 2, 3, 4, 5]
square_numbwers = list(map(lambda x: x**2, numbers))  # lambda function
print(square_numbwers)  # output [1, 4, 9, 16, 25]
#####################################################################################
##Lambda used for filter
numbers = [1, 2, 3, 4, 5, 6]
even_numbwers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbwers)
######################################################################################
students = [("alice", 25), ("baba", 20), ("babar", 23)]
students.sort(
    key=lambda x: x[1]
)  # output sorted [('baba', 20), ('babar', 23), ('alice', 25)]
print(students)


##################################################################################################
def apply_operation(x, y, operation=lambda a, b: a + b):
    return operation(x, y)


multiply = lambda a, b: a * b

add = apply_operation(5, 3)
multi = apply_operation(7, 8, multiply)

print(add)
print(multi)
