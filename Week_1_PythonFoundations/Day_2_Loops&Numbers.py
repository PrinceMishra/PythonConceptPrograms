# Factorial (recursion)
n = 10
print(f"Finding factorial of {n} using recursion.")


def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)


print("Factorial of {} is {}".format(n, factorial(n)))

# n Fibonacci (loop + recursion)

n = 10
print("Fibonacci series till {} using loop and recursion.".format(n))


def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)


x = 0
while x < n:
    res = fibonacci(x)
    print(res, " ", end="")
    x = x + 1


# Sum of digits
n = 5
print("Sum of {} digits".format(n))
sum = 0
for i in range(1, n+1):
    sum = sum + i

print(f"Sum of {n} digits is {sum}")


# Reverse a number
n = 123
print("Reverse this {}".format(n))
temp = n
rev = 0
while n > 0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10

print(f"Reverse of {temp} is {rev}")


# n Prime check
n = 53
print(f"Checking whether {n} is Prime number.")
counter = True
if n <= 1:
    counter = False
elif n > 1:
    for i in range(2, n):
        if n % i == 0:
            counter = False
            break

if counter == True:
    print(f"{n} is a Prime number.")
else:
    print(f"{n} is not a Prime number.")
