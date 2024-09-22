# Python – Group Similar items to Dictionary Values List...


# Input : test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
# Output : {4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]}
# Explanation : Similar items grouped together on occurrences.
#
# Input : test_list = [7, 7, 7, 7]
# Output : {7 : [7, 7, 7, 7]}
# Explanation : Similar items grouped together on occurrences.

from collections import Counter
test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]

inorder_list = Counter(test_list)
print(inorder_list)
l =[]
similar_item = {key: [key] *val for key, val in inorder_list.items() }
print(similar_item)



