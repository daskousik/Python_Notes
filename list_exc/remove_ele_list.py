# Remove multiple elements from a list in Python...
# Input: [12, 15, 3, 10]
# Output: Remove = [12, 3], New_List = [15, 10]

lst = [12, 15, 3, 10]

remove_list = []
new_list = []

remove = [12, 3]

for ele in lst:
    if ele in remove:
        remove_list.append(ele)
    else:
        new_list.append(ele)

print(f"Remove list output = {remove_list}, new_list = {new_list}")