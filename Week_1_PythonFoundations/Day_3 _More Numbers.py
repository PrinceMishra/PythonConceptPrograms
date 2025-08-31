# Generate primes 1–100

print("Generate primes 1–100")


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True


for i in range(1, 100):
    if is_prime(i):
        print(f"{i} ", end="")
print()
print("##################################")
print()

# n GCD & LCM


n1 = 60
n2 = 30
print("GCD and LCM of {} and {}".format(n1, n2))
lst = []

for i in range(1, n2+1):
    if n1 % i == 0 and n2 % i == 0:
        lst.append(int(i))

gcd = max(lst)

greater = max(n1, n2)

while True:
    if greater % n1 == 0 and greater % n2 == 0:
        lcm = greater
        break
    greater += 1


print("{} and {} of GCD is {} and LCM is {}.".format(n1, n2, gcd, lcm))

print()
print("##################################")
print()

# n Armstrong number
num = 153
print("Finding armstrong number of {}".format(num))


def armstrong(n):
    count = len(str(n))
    # temp = n
    # while temp > 0:
    #     count = count + 1
    #     temp = temp // 10
    # print(count)
    res = 0
    while n > 0:
        rem = n % 10
        res = res + pow(rem, count)
        n = n // 10
    return res


n = armstrong(num)
print(n)
if num == n:
    print(f"{num} is an armstrong number.")
else:
    print(f"{num} is not an armstrong number.")

print()
print("##################################")
print()

# Strong number

num = 145
print(f"finding whether {n} is a strong number.")


def fact(n):
    if n <= 1:
        return 1
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact


temp = num
res = 0
while temp > 0:
    rem = temp % 10
    res = res + fact(rem)
    temp = temp // 10


if num == res:
    print(f"{num} is a strong number.")
else:
    print(f"{num} is not a strong number.")

print()
print("##################################")
print()


# Decimal to binary, octal, hex

num = 10
temp = num
print(f"Finding Decimal --> binary , octal, hex")
print("")

print("** Decimal --> Binary **")
lst = []
while num > 0:
    rem = num % 2
    lst.append(rem)
    num = num // 2

binary_num = lst[::-1]

print(f"Binary number of {temp} is {binary_num}")
print()

num = 52
temp = num
print("** Decimal --> Octal **")
lst = []
while num > 0:
    rem = num % 8
    lst.append(rem)
    num = num // 8

octal_num = lst[::-1]
print(f"Octal number of {temp} is {octal_num}")
print()
num = 52
temp = num
print("** Decimal --> hex **")
lst = []
while num > 0:
    rem = num % 16
    lst.append(rem)
    num = num // 8

hex_num = lst[::-1]
print(f"hex number of {temp} is {hex_num}")
print()
