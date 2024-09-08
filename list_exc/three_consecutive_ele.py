# Python program to check if the list contains three consecutive common numbers in Python
# Input : [4, 5, 5, 5, 3, 8]
#
# Output : 5
#
# Input : [1, 1, 1, 64, 23, 64, 22, 22, 22]
#
# Output : 1, 22

# Take input list
lst = [4, 5, 5, 5, 3, 8]

# loop through each elements with index start....
# check first ele is  next two ele are same.
for i in range(len(lst) - 2):
    if lst[i] == lst[i+ 1] == lst[i+ 2]:
        print(lst[i])
# ------------------------------------------------------------------------------------------------------------------
# permutations using library function
from itertools import permutations

#This method takes a list as an input and returns an object list of tuples
perm = permutations(lst)
print(perm)
#for i in list(perm):
    #print(i)

# ----------------------------------------------------------------------------------------------------------------------
