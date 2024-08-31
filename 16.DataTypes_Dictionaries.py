## 9/49  Dictionaries
my_dict = {1: "one", 2: "two"}  # output {1: 'one', 2: 'two'}
my_dict = dict(one="one", two=2)  # output {'one': 'one', 'two': 2}
## Iterable
# my_dict = dict([1, "one"])  # TypeError with single square bracket
# my_dict = dict([[1, "one"]])  # output with Double square bracket {1: 'one'}
# my_dict = dict([(1, "one")])  # tuple output {1: 'one'}
# my_dict = dict([(1, "one"), [2, "two"]])
# output with list element {1: 'one', 2: 'two'}
# my_dict = dict([(1, "one"), [2, "two"], set([3, "three"])])  #
# output is {1: 'one', 2: 'two', 3: 'three'} 3=value, three=key
print(my_dict)

## 9/50 Retrieve and Update Values
# person = {"first_name": "eza", "second_name": "asan", "age": 45}
# print(person)  # output {'first_name': 'eza', 'second_name': 'asan', 'age': 45}
# print(person["first_name"])  # output eza
# print(person["jaz"])  # output keyError with not exist
# person["age"] = 36  # output replace the age
# person["job"] = "programmer"  # output added new key value
# print(person)
# result = person.get("job")  # output None
# result = person.get("job", "No job found")  # output No job found
# result = person.setdefault("job", "programmer")  # output programmer
# result = person.update(state="NY", job="Coder")
# result = person.update([["state", "NY"], ["job", "Coder"]])  # output
# {'first_name': 'eza', 'second_name': 'asan', 'age': 45, 'state': 'NY', 'job': 'Coder'}
# new_info = {"job": "Coder", "state": "Florida"}
# print(result)
# person.update(new_info)
# print(person)

## 9/51 Remove Elements
person = {
    "first_name": "eza",
    "second_name": "asan",
    "age": 45,
    "state": "Florida",
    # "job": "Coder",
}  # when remove job, KeyError
# result = person.pop("job")  #
## output {'first_name': 'eza', 'second_name': 'asan', 'age': 45, 'state': 'Florida'}
# result = person.pop("job", "no job here")  # output no job here
# result = person.popitem()  # output last dictionary has no key value
# print(result)
# del person["age"]  # output age is removed
# person.clear()  # output empty curly braces, all items removed
# print(person)

## 9/52 More methods and Comprehension with Key, Value, Items
# print(person.keys())  # output dict_keys(['first_name', 'second_name', 'age', 'state'])
# print(person.values())  # output dict_values(['eza', 'asan', 45, 'Florida'])
# print(person.items())  # output list of tuples
##dict_items([('first_name', 'eza'), ('second_name', 'asan'), ('age', 45), ('state', 'Florida')])

for key in person.keys():
    print(key)  # output is
# first_name
# second_name
# age
# state
for value in person.values():
    print(value)
for key, value in person.items():
    print(key, value)
for k, v in person.items():
    print(k, v)

## Dictionaries Class Method
my_list = [1, 2, 3, 4, 5]
my_dict = dict.fromkeys(my_list, "hello world")  ## Output
##{1: 'hello world', 2: 'hello world', 3: 'hello world', 4: 'hello world', 5: 'hello world'}
my_dict = dict.fromkeys(my_list, [])  # output {1: [], 2: [], 3: [], 4: [], 5: []}
my_dict[1].append(
    "hi"
)  # output {1: ['hi'], 2: ['hi'], 3: ['hi'], 4: ['hi'], 5: ['hi']}
my_dict = {x: [] for x in my_list}  # output {1: [], 2: [], 3: [], 4: [], 5: []}
my_dict = {x: x**2 for x in my_list}  # output {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(my_dict)
