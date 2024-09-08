# Python – Convert List to List of dictionaries..
# Input : test_list = [“Gfg”, 3, “is”, 8], key_list = [“name”, “id”]
# Output : [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}]
# Explanation : Values mapped by custom key, “name” -> “Gfg”, “id” -> 3.

lst = ['Gfg', 3, 'is', 8]
key_list = ['name', 'id']
new_list = []
# Method #1 : Using loop + dictionary comprehension
for i in range(0,len(lst), 2):
    new_list.append({key_list[0]: lst[i], key_list[1]:lst[i + 1]})


#mdict = {k:v for (v) in zip(key_list, lst)}
print(new_list)
mdict = {key_list[0]: lst[::2], key_list[1]: lst[1::2]}
print(mdict)








