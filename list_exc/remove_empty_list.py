# Python – Remove empty List from List
# The original list is : [5, 6, [], 3, [], [], 9]
# List after empty list removal : [5, 6, 3, 9]

lst = [5, 6, [], 3, [], [], 9]

print('The original list is {}'.format(lst))

new_list = []
for ele in lst:
    if ele :       # ele!= []
        new_list.append(ele)

print('Remove empty list in list using single loop and if --> ',new_list)

# -------------------------------------------------------------------------------------------------

#Method 1: Using list comprehension:

l1 = [ele for ele in lst if ele != []]
print('Remove empty list using list Comprehension -- >',l1)

# -------------------------------------------------------------------------------------------------
# filter the empty list with None also and return a object . Then using list method convert it list values.
res = list(filter(None, lst))
print('Remove empty list using filter method ---->',res)

# -----------------------------------------------------------------------------------------------------------------
# with check empty value each iteration of list.
# Here while check condition + looping
while [] in lst:
    lst.remove([])
print(lst)
# -------------------------------------------------------------------------------------------------------------------

