# Python program to create a list of tuples from given list having number and its cube in each tuple
# Given a list of numbers of list, write a Python program to create a list of tuples having first element as the number and second element as the cube of the number.
# Input: list = [1, 2, 3]
# Output: [(1, 1), (2, 8), (3, 27)]
#
# Input: list = [9, 5, 6]
# Output: [(9, 729), (5, 125), (6, 216)]

in_list = [1, 2, 3]

print('Input list ' , in_list)
res = [(i, i*i*i) for i in in_list]
print(res)

#-----------------------------------------------------------------------------------------------------------------------
# map(func, *iterables) –> map object
# Make an iterator that computes the function using arguments from each of the iterables.
# Stops when the shortest iterable is exhausted.
cube = list(map(lambda x: (x, x**3), in_list))
print(cube)

# ----------------------------------------------------------------------------------------------------------------------
t = (100, 200, 300)

in_list += t  # add tuple in list.
print(in_list)

in_list = in_list + cube   # add two list.
print(in_list)