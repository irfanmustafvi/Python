# Section 6/33 lists
my_list = ["cat", "dog"]
my_list = list()  # Empty list
my_list = list("cat")  # This print each character separate if list not found.
my_list = list(["cat"])  # when put square bracket then single item is pronted
my_list = ["cat", "dog"]
my_list.append(1)
my_list.append("cow")
my_list = ["cat", "dog", "cow"]
my_otherlist = ["horse", "duck"]
my_list.insert(1, "duck")  # This onsert before number of character.
my_list = ["cat", "dog", "cow"]
my_otherlist = ["horse", "duck"]
my_list.extend(my_otherlist)  # This combine both lists
my_list += my_otherlist
print(my_list)
