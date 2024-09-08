# Python | Program to print duplicates from a list of integers

# Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# Output : output_list = [20, 30, -20, 60]

lst = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]


dup = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j] and lst[i] not in dup:
            dup.append(lst[j])

print('Find duplicate using two loop',dup)

# -------------------------------------------------------------------------------------------------
uniqe_list  = []
duplicate_list = []
for i in lst:
    if i not in uniqe_list:
        uniqe_list.append(i)
    elif i not in duplicate_list:
        duplicate_list.append(i)

print('Find duplicate using single loop',duplicate_list)

# --------------------------------------------------------------------------------------------------
#Method 3: Using Counter() function from collection modul
from collections import Counter

d =Counter(lst)
print(d)
new_dup_list = [x for x in d if d[x]>1]

print('Method 3: Using Counter() function from collection modul', new_dup_list)

# -------------------------------------------------------------------------------------------------
# Method 5: Using list comprehension method





