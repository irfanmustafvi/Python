# SECTION 15/82 Files Fundamentals and Data Working
# 15/83 Error Handling
try:
    my_list = [1, 2, y]  # output Oh no Something went wrong!
    x = 10 / 0  # division by zero
    z = my_list[3]

# except (ZeroDivisionError, IndexError):
# print("You cannot divide by zero or use Index out of range!")
# Output You cannot divide by zero or use Index
# out of range!
except ZeroDivisionError:
    print("You cannot divide by zero!")
except IndexError:
    print("You cannot use index out of range!")
# except:
#     print("Oh no Something went wrong!")
except Exception as e:
    print("Error:", e)
finally:
    print("Done checking for errors")
####################################################
try:
    my_list = [1, 2]

# except (ZeroDivisionError, IndexError):
# print("You cannot divide by zero or use Index out of range!")
# Output You cannot divide by zero or use Index
# out of range!
except ZeroDivisionError:
    print("You cannot divide by zero!")
except IndexError:
    print("You cannot use index out of range!")
# except:
#     print("Oh no Something went wrong!")
except Exception as e:
    print("Error:", e)
finally:
    print("Done checking for errors")
###################################################################
# SECTION 15/83 Files Introductions
"""
With context_manager_expression as variable:
Code block that uses the context_manager 
"""
# try:
#     with open("non_existent_file.txt", "r") as file:
#         data = file.read()  # Does nothing as the file does not exist
# except FileNotFoundError:
#     print("file not found")
######################################################################
try:
    with open("non_existent_file.txt", "r") as file:
        data = file.read()  # Does nothing as the file does not exist
except FileNotFoundError:
    with open("example.txt", "w") as file:
        file.write("Hello, world!")  # file.txt is created with script Hello world
###############################################################################
try:
    with open("example.txt", "x") as file:
        file.write("Hello world")
except FileExistsError:
    print("File already exist")  # Output File already exist
##################################################################################
with open("example.txt", "a") as file:
    file.write(
        "\nAppending additional content."
    )  # output in .txt file Appending additional content.
    file.write("\nAppending even more content.")  # Appending even more content.
##########################################################
# with open("example.txt", "w") as file:
# file.write() # Output is typeError
# file.read() # error file read
# with open("example.txt", "r+") as file:
#     file.write("tested")  #
# output in .txt tested world
# Appending additional content.
# Appending even more content.
###############################################################
# SECTION 15/84 Files reading data
with open("example.txt", "r") as file:
    print(file.read())  # output Hello, world!
###############################################
with open("example.txt", "r") as file:
    print(f"first five: {file.read(5)}")
    print(f"second five: {file.read(5)}")
    print(f"third five: {file.read(5)}")
    print(f"fourth five: {file.read(5)}")
    # output will be 5 characters gap (Hello) (, wor) (ld!) (A) (ppend)
##############################################################################
with open("example.txt", "r") as file:
    # print(file.readline()) # output Hello, world!
    print(f"first five: {file.readline(5)}")
    print(f"second five: {file.readline(5)}")
    print(f"third five: {file.readline(5)}")
    print(f"fourth five: {file.readline(5)}")
    # output is first five: Hello
    # second five: , wor
    # third five: ld!
    #
    # fourth five: Appen

##############################################################################
# with open("example.txt", "r") as file:
# print(file.readlines())
# output is ['Hello, world!\n', 'Appending additional content.\n', 'Appending even more content.']
# with open("example.txt", "r") as file:
# print(file.readlines(13))  # Output ['Hello, world!\n']
# print(file.readlines(43))  # ['Appending additional content.\n', 'Appending even more content.']
# print(file.readlines(44))
# output ['Hello, world!\n', 'Appending additional content.\n', 'Appending even more content.']
##############################################################################
# with open("example.txt", "r") as file:
#     print(f"first readlines: {file.readlines(1)}")
#     print(f"second readlines: {file.readlines(1)}")
#     print(f"third readlines: {file.readlines(1)}")  # output
# #first readlines: ['Hello, world!\n']
# #second readlines: ['Appending additional content.\n']
# #third readlines: ['Appending even more content.']
############################################################################
# with open("example.txt", "r") as file:
#     file.seek(7)
#     print(f"7th character seek: {file.read(6)}")  # output 7th character seek: world!
########################################################################
with open("example.docx", "w") as file:
    file.write("Hello Folks")
#################################################################################
# SECTION 15/85 Reading & writing comma separated values
