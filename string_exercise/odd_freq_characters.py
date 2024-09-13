# Python – Odd Frequency Characters
# Input : test_str = 'geekforgeeks'
# Output : ['r', 'o', 'f', 's']
# Input : test_str = 'g'
# Output : ['g']
from collections import Counter

# initializing string
test_str = 'geekforgeeks is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# Odd Frequency Characters
# Using list comprehension + Counter()
res = [chr for chr, count in Counter(test_str).items() if count & 1]

# printing result
print("The Odd Frequency Characters are : " + str(res))
# ----------------------------------------------------------------------------------------------------------------------
# Python3 code to demonstrate working of
# Odd Frequency Characters


# initializing string
test_str = 'geekforgeeks is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# Odd Frequency Characters
x = set(test_str)
res = []
for i in x:
    if (test_str.count(i) % 2 != 0):
        res.append(i)
# printing result
print("The Odd Frequency Characters are : " + str(res))

# ----------------------------------------------------------------------------------------------------------------------
def odd_freq_chars(test_str):
    # Create an empty dictionary to hold character counts
    char_counts = {}

    # Loop through each character in the input string
    for char in test_str:
        # Increment the count for this character in the dictionary
        # using the get() method to safely handle uninitialized keys
        char_counts[char] = char_counts.get(char, 0) + 1

    # Create a list of characters whose counts are odd
    return [char for char, count in char_counts.items() if count % 2 != 0]


# Test the function with sample input
test_str = 'geekforgeeks is best for geeks'
print("The original string is : " + str(test_str))
res = odd_freq_chars(test_str)
print("The Odd Frequency Characters are :" + str(res))

# ----------------------------------------------------------------------------------------------------------------------

