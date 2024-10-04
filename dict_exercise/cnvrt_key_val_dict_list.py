# Python – Convert Key-Value list Dictionary to List of Lists......
# The original dictionary is : {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
# The converted list is : [['gfg', 1, 3, 4], ['is', 7, 6], ['best', 4, 5]]

original_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

l = []

for key , value in original_dict.items():

    l.append([key] + value)  # In list add two list .

print(l)


