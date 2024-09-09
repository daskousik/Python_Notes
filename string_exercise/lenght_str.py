# Find length of a string in python (6 ways)
# Input : 'abc'
# Output : 3
#
# Input : 'hello world !'
# Output : 13
#
# Input : ' h e l   l  o '
# Output :14
# ----------------------------------------------------------------------------------------------------------------------
# In this above we can see string also calculate lenght with space .
in_str = 'hello world !'

# Methods#1: Using the built-in function len.
# The built-in function len returns the number of items in a container.

nos_item = len(in_str)
print(nos_item)

# -----------------------------------------------------------------------------------------------------------------------

# Method 2: Using counter
counter = 0
for ch in in_str:
    counter = counter + 1

print(counter)

# ----------------------------------------------------------------------------------------------------------------------

# Method3 list compresion and sum: iterable and sum.
res = sum([1 for i in in_str])
print(res)

# ----------------------------------------------------------------------------------------------------

# Method 4 : Using enumerate function
s = 0
for i, ch in enumerate(in_str):
    s = s + 1
print(s)
# ----------------------------------------------------------------------------------------------------
# Python – Avoid Spaces in string length
str = 'geeksforgeeks best'
counter = 0
for ch in str:
    if ch.isspace():  # if ch == ' '
        continue
    counter = counter + 1

print(counter)
