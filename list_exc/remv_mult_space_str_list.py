# The original list is : ['gfg', '   ', ' ', 'is', '            ', 'best']
# List after filtering non-empty strings : ['gfg', 'is', 'best']
# # Remove multiple empty spaces from string List
# # Using list comprehension + strip()
str_list = ['gfg', '   ', ' ', 'is', '            ', 'best']
# Return a copy of the string with leading and trailing whitespace removed.
# if ele.strip() --> check each element has no whitespace with leading and trailing then return element.
res = [ele for ele in str_list if ele.strip()] # if not ele.isspace()
print('Remove multiple empty spaces from string List Using list comprehension + strip()', res)

# ----------------------------------------------------------------------------------------------------------
# Using find()
# S. find(sub[, start[, end]]) -> int
# Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].
# Return -1 on failure.
res2 = []
for ele in str_list:
     if ele.find(' ') == -1:
          res2.append(ele)
print('Remove multiple empty spaces from string List Using find() ', res2)

# -----------------------------------------------------------------------------------------------------------
# filter + Using lambda function

res3 = list(filter(lambda x: x[0].lower() != x[0].upper() , str_list))
print(res3)