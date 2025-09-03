# Palindrome check
print()
print("Palindrome check")
print()
str = "racecar"

print("** First Way **")
rev_str = str[::-1]

if str == rev_str:
    print(f"{str} is palindrome string")
else:
    print(f"{str} is not palindrome string")

print()
print("** Second Way **")

str = "madam"
rev_str = "".join(reversed(str))

if str == rev_str:
    print(f"{str} is palindrome string")
else:
    print(f"{str} is not palindrome string")

print()
print("##################################")
print()


# Count vowels/consonants

print("Counting vowels/consonants")
str = "Prince"
str = str.lower()
vowel = 0
consonant = 0
for i in str:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowel = vowel + 1
    else:
        consonant = consonant + 1
print(f"{vowel} Vowels are in {str}.")
print(f"{consonant} Vowels are in {str}.")

print()
print("##################################")
print()

# String length without len()

print("String length without len()")
str = "Hello World"
count = 0
for i in str:
    count = count + 1
print(f"Length of {str} is {count}")

print()
print("##################################")
print()

# Remove duplicates from string
print("Remove duplicates from string")
str = "Hello World"
result = ""
for ch in str:
    if ch not in result:
        result = result + ch

print(f"After removing duplicates from {str} is now {result} ")

print()
print("##################################")
print()

# Reverse words in sentence
str = "unconditional"

# First Way
print("** First Way **")
result = str[::-1]
print(f"Reverse of {str} is {result}")
print()

# Second Way
print("** Second Way **")
rev_str = ""
len = len(str)
for i in range(len-1, 0, -1):
    rev_str = str[i]
print(f"Reverse of {str} is {result}")
