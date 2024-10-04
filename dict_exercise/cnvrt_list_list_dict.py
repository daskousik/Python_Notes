# Python – Convert List to List of dictionaries.......
# Given list values and keys list, convert these values to key value pairs in form of list of dictionaries.

# Input : test_list = [“Gfg”, 3, “is”, 8], key_list = [“name”, “id”]
# Output : [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}]
# Explanation : Values mapped by custom key, “name” -> “Gfg”, “id” -> 3.
#
# Input : test_list = [“Gfg”, 10], key_list = [“name”, “id”]
# Output : [{‘name’: ‘Gfg’, ‘id’: 10}]
# Explanation : Conversion of lists to list of records by keys mapping.

test_list = ['Gfg', 3, 'is', 8]
key_list = ['name', 'id']
result = [ {key: test_list[i]} for key in key_list for i in range(0,len(test_list), 2)]

print(result)


