# Python – Sort String list by K character frequency
# Given String list, perform sort operation on basis of frequency of particular character.
#
# Input : test_list = [“geekforgeekss”, “is”, “bessst”, “for”, “geeks”], K = ‘s’
# Output : [‘bessst’, ‘geekforgeekss’, ‘geeks’, ‘is’, ‘for’]
# Explanation : bessst has 3 occurrence, geeksforgeekss has 3, and so on.
#
# Input : test_list = [“geekforgeekss”, “is”, “bessst”], K = ‘e’
# Output : [“geekforgeekss”, “bessst”, “is”]
# Explanation : Ordered decreasing order of ‘e’ count.
from collections import OrderedDict
test_list = ["geekforgeekss", "is", "bessst"]
k = 'e'
freq_dict = {}

key_item_dict = {item.count(k): item for item in test_list}
sort_key = sorted(key_item_dict.items(), reverse=True)
print(sort_key)
result = [item[1] for item in sort_key]
print(result)










