# Print without print()

# first way
import os
import sys
sys.stdout.write("Hello, World! \n")

# second way
os.write(1, b"Hello, World!\n")

# third way
sys.__stdout__.write("Hello, World!\n")


# Swap numbers

# first way
a, b = 10, 20
print("Before swaping a = {} and b = {} ".format(a, b))
a, b = b, a
print("After swaping a = {} and b = {} ".format(a, b))

# second way
a = 50
b = 25
print(f"Before swaping a = {a} and b = {b} ")
a = a+b
b = a-b
a = a-b
print(f"After swaping a = {a} and b = {b} ")


# third way
a = 90
b = 180
print(f"Before swaping a = {a} and b = {b} ")
a = a*b
b = a/b
a = a/b
print(f"After swaping a = {a} and b = {b} ")


# n Largest of three numbers

# n Even/odd check
# n Factorial (loop)
