## 11/60 Range Data Type (used in foreloop conjunction)
my_range = range(4)
print(my_range)
my_range = range(4, 10, 2)
print(list(my_range))
print(len(my_range))
print(sum(my_range))
for i in range(10):
    print(i)

## 11/61 Loops Introduction
## 11/62 Loops While
counter = 0  # Create Variable
while counter <= 5:  # condition
    print(counter)
    counter += 1  # increment counter

counter = 0  # Create Variable
while counter <= 5:  # condition
    if counter % 2 == 0:
        print(counter)
        counter += 1
        continue  # This will continue output as 0 infinit loop until stop by ctrl + c
    counter += 1
else:
    print("done")

counter = 0  # Create Variable
while counter <= 5:  # condition
    if counter == 3:
        break
    print(counter)
    counter += 1
else:
    print("done")  # output 0 1 2 in column

counter = 0
while True:
    if input("enter q to exit: ") == "q":
        break

num1 = 1
while num1 < 3:
    num2 = 1
    while num2 < 2:
        print(num1 * num2)
        num2 += 1
    num1 += 1

## 11/63 Loops if
animals = ["cat", "dog", "goat"]
for animal in animals:
    print(animal)

animals = ["cat", "dog", "goat"]
for animal in animals:
    if animal == "goat":
        break  # if use break then else won't work
    print(animal)

animals = ["cat", "dog", "goat"]
for animal in animals:
    if animal == "goat":
        continue
    print(animal)
else:
    print("done")

animals = ["cat", "dog", "goat"]
for animal in animals:
    animal = "goat"
    print(animal)
print(animals)

animals = ["cat", "dog", "goat"]
for i in range(len(animals)):
    animals[i] = "goat"
    print(animals[i])
print(animals)

animals = ["cat", "dog", "goat"]
for char in ["hello world"]:
    print(char)

for x in range(1, 3):
    for y in range(1, 4):
        print(x * y)
