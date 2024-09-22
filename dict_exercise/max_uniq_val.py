# Python – Key with maximum unique values..
# Given a dictionary with a values list, extract the key whose value has the most unique values....
# Input : test_dict = {"Gfg" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}
# Output : "Gfg"
# Explanation : "Gfg" having max unique elements i.e 5.


# Input : test_dict = {"Gfg" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}
# Output : "Best"
# Explanation : 3 (max) unique elements, 9, 6, 5 of "Best".
from collections import Counter

test_dict = {"Gfg" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}

uniqe_dict = {key: set(value) for key, value in test_dict.items() }
print(uniqe_dict)

max_key = max(uniqe_dict, key= lambda x: len(uniqe_dict[x]))
print(max_key)




