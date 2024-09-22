# Python – Replace String by Kth Dictionary value.........

# Input : test_list = [“Gfg”, “is”, “Best”], subs_dict = {“Gfg” : [5, 6, 7], “is” : [7, 4, 2]}, K = 0
# Output : [5, 7, “Best”]
# Explanation : “Gfg” and “is” is replaced by 5, 7 as 0th index in dictionary value list.
#
# Input : test_list = [“Gfg”, “is”, “Best”], subs_dict = {“Gfg” : [5, 6, 7], “Best” : [7, 4, 2]}, K = 0
# Output : [5, “is”, 7]
# Explanation : “Gfg” and “Best” is replaced by 5, 7 as 0th index in dictionary value list.

test_list = ['Gfg', 'is', 'Best']

subs_dict = {'Gfg' : [5, 6, 7], 'is' : [7, 4, 2]}
k = 0

for i, ele in enumerate(test_list):
    if ele in subs_dict:
        test_list[i] = subs_dict[ele][k]

print(test_list)