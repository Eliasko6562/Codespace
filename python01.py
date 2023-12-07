#!/usr/bin/python3

import math


# <- comment
# USE TABS 

#############   Data types

# str = string ->>> slovo

# int = integer ->>> 12

# float = float ->>> 12.12

#############   variables

x = 1
# int
x = "1"
# string
print(str(x))

#FUNCTIONS

# def = define
# name
def name_of_the_function(a,b):
    soucet = a+b
    return soucet

# call function
print(str(name_of_the_function(1, 1.1)))

y = 5.2 
print(math.ceil(y))
# ceil ->


# list (list!!!!)
pole = []

for i in range(0,10,2):
    pole.append(i)

print(pole)

set0 = ("bla","bla")

dict0 = {"first":10, 
         "second":20, 
         "third":"can be string"
         }
print(dict0.keys())
print(dict0["first"])
for i in dict0.items():
    for j in i:
    print(j)
x=6
if x > 5:
    print(True)
