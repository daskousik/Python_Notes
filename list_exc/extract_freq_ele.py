# Python – Extract elements with Frequency greater than K
# Given a List, extract all elements whose frequency is greater than K.
#
# Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
# Output : [4, 3]
# Explanation : Both elements occur 4 times.
#
# Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2
# Output : [4, 3, 6]
# Explanation : Occur 4, 3, and 3 times respectively.
from collections import Counter
test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3

# In this method we are going to be use Counter method after using loop fetch the list of value.
res = []
dict_count = Counter(test_list)
print(dict_count)
for key, value in dict_count.items():
    if value > k:
        break
        res.append(key)

print('Using Counter and loop simple',res)

# --------------------------------------------------------------------------
# using list Comprehension and counter..
result_comp = [ele for ele , cnt in dict_count.items() if cnt > k]

print('Using list Comprehension', result_comp)

#-----------------------------------------------------------------------------

# using simple loop and count variable.
import  numpy as np
unique_elements, counts = np.unique(test_list, return_counts=True)
print(unique_elements, counts)
print(unique_elements[counts>k])

lambda_func = lambda ele: dict_count[ele]> k
print(list(filter(lambda_func, dict_count)))

