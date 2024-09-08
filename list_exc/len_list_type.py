# How To Find the Length of a List in Python ?
# The length of a list means the number of elements it has. The len() function is an inbuilt function in Python.
# It can be used to find the length of an object by passing the object within the parentheses.

lst = [1, 2, 3, 9]
print('Find length of the list using len() func --->', len(lst))

# ---------------------------------------------------------------------
# Find the Length of a List Using Naive Method
# In this tech we run a loop and increase the counter till the last elements of the list to know its count.
counter = 0
for ele in lst:
    counter += 1

print('Find length of the list using loop and counter --->' + ' ' + str(counter))

#------------------------------------------------------------------------------

# Find the Length of a List Using a List Comprehension
# In this tech I loop through each one element and assigne 1 per loop and sum to count
length = 0
length = sum([1 for ele in lst])
print('Length of list using list comprehension is' + ' ' + str(length))

#-----------------------------------------------------------------------
# Find the Length of a List Using enumerate() function
# enumerate func generate count -- start at 0 to n and each element in list.
s = 0
for i, ele in enumerate(lst):
    s = s + 1
print('Find the Length of a List Using enumerate() function', s)
