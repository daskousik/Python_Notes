# Python – Remove suffix from string list
# The original list : ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']
# List after removal of suffix elements : ['gfg', 'xit', 'is']

str_list = ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']
res = []
for ele in str_list:
    if ele.endswith('x'):
        continue
    else:
        res.append(ele)

print(res)
