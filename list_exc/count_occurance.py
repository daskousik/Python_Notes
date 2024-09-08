lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10

# ----------------------------------------------------------------------
# Python Count occurrences using a Loop in Python
count = 0

for item in lst:
    if item == x:
        count = count + 1
print('Python Count occurrences using a Loop in Python -->', count)

# ---------------------------------------------------------------------------------------------------
# Python Count Occurences using List Comprehension

#count_comp = sum([1 for item in lst if item == x])

count_comp = [item for item in lst if item == x]  # return with match item in a new list. [10, 10, 10]

print('Python Count Occurences using List Comprehension --->', len(count_comp))

# ------------------------------------------------------------------------------------------------------------
# Python Count using Enumerate Function
j = 0
for i, item in enumerate(lst):
    if item == x:
        j = j +1
print('Python Count using Enumerate Function --->', j)

# -------------------------------------------------------------------------------------------------------------

print('Count occurrences of an element using count() --->',lst.count(x))
# -------------------------------------------------------------------------------------------------------------
#

from collections import Counter
counter = Counter(lst)
print(counter)

# ----------------------------------------------------------------------------------------------
# Use a Dictionary for Counting Elements in a List.

count_dict = {}

for item in lst:
    if item in count_dict:
        count_dict[item] = count_dict[item] + 1
    else:
        count_dict[item] = 1

print('Use a Dictionary for Counting Elements in a List ---->',count_dict)

