# Print without print()

# first way
import os
import sys
print("** First Way **")
sys.stdout.write("Hello, World! \n")

# second way
print()
print("** Second Way **")
os.write(1, b"Hello, World!\n")

# third way
print()
print("** Third Way **")
sys.__stdout__.write("Hello, World!\n")


print()
print("##################################")
print()

# Swap numbers

# first way
print()
print("** First Way **")
a, b = 10, 20
print("Before swaping a = {} and b = {} ".format(a, b))
a, b = b, a
print("After swaping a = {} and b = {} ".format(a, b))

# second way
print()
print("** Second Way **")
a = 50
b = 25
print(f"Before swaping a = {a} and b = {b} ")
a = a+b
b = a-b
a = a-b
print(f"After swaping a = {a} and b = {b} ")


# third way
print()
print("** Third Way **")
a = 90
b = 180
print(f"Before swaping a = {a} and b = {b} ")
a = a*b
b = a/b
a = a/b
print(f"After swaping a = {a} and b = {b} ")


print()
print("##################################")
print()


# Largest of three numbers
a, b, c = 40, 20, 30

# first way
print()
print("** First Way **")

print(f"Finding largest in {a} ,{b}, {c}")

if a > b:
    if a > c:
        print(f"{a} is the largest number.")
    else:
        print(f"{c} is the largest number.")
elif b > c:
    print(f"{b} is the largest number.")
else:
    print(f"{c} is the largest number.")

# second way
print()
print("** Second Way **")
print(f"{max(a, b, c)} is the largest number")


print()
print("##################################")
print()


# Even/odd check

n = 13

# first way
print()
print(f"Finding if {n} is even or odd.")

if n % 2 == 0:
    print(f"{n} is even number.")
else:
    print(f"{n} is odd number.")

print()
print("##################################")
print()


# n Factorial (loop)

x = 5
print(f"Finding factorial of {x}")
n = x
res = 1
while x > 0:
    res = res * x
    x = x-1

print(f"factorial of {n} is {res}.")

print()
print("##################################")
print()
