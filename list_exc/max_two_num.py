# Find Maximum of two numbers in Python...
# Given two numbers, write a Python code to find the Maximum of these two numbers.
#
# Examples:
#
# Input: a = 2, b = 4
# Output: 4
#
# Input: a = -1, b = -4
# Output: -1

# ----------------------------------------------------------------------------------
# Cash 1:
# we will compare two numbers using if-else statement and will print the output accordingly.

a = 2 ; b = 4

if a >= b:
    print('Greater number is Cash 1 using if and else --> ' + str(a))

else:
    print('Greater number is Cash 1 using if and else--> ' + str(b))

# -------------------------------------------------------------------------
# Cash 2:
# Find Maximum of two numbers Using max() function

print('Greater number is Cash 2 using max func-->', max(a, b))

#----------------------------------------------------------------
# Maximum of two numbers Using Ternary Operator
print('Greater number is Cash 3 using ternary operator', a if a >= b else b)

# -------------------------------------------------------------------------------
# Cash 4:
# Maximum of two numbers Using lambda function
maximum = lambda a, b: a if a >= b else b
print('Greater number is Cash 4 using lambda func', maximum(a, b))
# ----------------------------------------------------------------------------------

# Maximum of two numbers Using list comprehension

list_max = [a if a >= b else b]
print(list_max)

