##>>> 14/79 & 80 Modules: Reusable code
# > open in browser (https://pypi.org/)
##>>Search for game development
# 14/80 Importimg Modules

import math

x = math.factorial(5)  # output (1x2x3x4x5=) 120
print(x)
###############################################
import math
from math import sqrt

x = sqrt(16)
print(x)
################################################
import math
from math import sqrt
from math import sin, cos, tan

x = sin(1)
y = cos(1)
z = tan(1)
print(x, y, z)  # Output 0.8414709848078965 0.5403023058681398 1.5574077246549023
#######################################################
import random as r

x = r.randint(1, 10)
print(x)  # evry click random number change in output


###################################################
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


x = add(3, 4)
print(x)
x = sub(3, 4)
print(x)
#######################################################
# import import_me.py


def main():
    print("this is the main function in the import_me.py file")


print("This is a regular statement inside the script")
main()
print("hello")


########################################################
def main():
    print("this is the main function in the import_me.py file")


print("This is a regular statement inside the script")

if __name__ == "__main__":
    main()
print("hello")
#############################################################
##>>>> 14/81 Third party Modules (from Documentation)
import numpy as np

my_array = np.array([1, 5, 2, 3, 4])  # Output [1 5 2 3 4]
my_array.sort()  # output [1 2 3 4 5]
print(my_array)
