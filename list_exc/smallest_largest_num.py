# Python program to find smallest number in a list
# Input : list1 = [10, 20, 4, 1, 1, 0, 3, 2, 0]
# Output : 4
#
list2 = [20, 10, 20, 1, 100]
# Output : 1

list1 = [10, 20, 4, 1, 1, 0, 3, 2, 0]
# Sorting the list to find smallest number in a list
# In Ascending order

list1.sort()

print('Find smallest number in a list using sort() func asc order --->',list1[0])

list2.sort(reverse=True)

print('Find smallest number in a list using sort() func desc order --->',list2[-1])

# ------------------------------------------------------------------------------------------
# Using min() Method to find smallest number in a list

# --------------------------------------------------------------------------------------------
l1 = [10, 20, 4, 1, 1, 0, 3, 2, 0]
min = l1[0]
max = l1[0]

for i in range(len(l1)):

    if l1[i] < min:
        min = l1[i]

    if l1[i] > max:
        max = l1[i]

print('Find smallest and greatest  value using traversing ', min, max)

# --------------------------------------------------------------------------------------------------------
li1 = [70, 11, 20, 4, 100, 8, 90, 80, 45, 78, 99, 1000, 888, 999, 0]
print(li1)

max1 = li1[0]
max2 = li1[1]

for i in range(len(li1)):
    if li1[i] > max1:
        max2 = max1
        max1 = li1[i]
    else:
       pass

print('Second largest value in list', max2, max1)


