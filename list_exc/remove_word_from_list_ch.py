 # Python – Remove words containing list characters
# The original list is : ['gfg', 'is', 'best', 'for', 'geeks']
# The character list is : ['g', 'o']
# The filtered strings are : ['is', 'best']

str_list = ['gfg', 'is', 'best', 'for', 'geeks']
ch_list = ['g', 'o']
res = []
flag = 1
for ele in str_list:
    for ch in ch_list:
        if ch not in ele:
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        res.append(ele)

print('Return list of words  where sub list chars are not present using loop...' ,res)

# ----------------------------------------------------------------------------------------------------------------

res2 = [ele for ele in str_list if all(ch not in ele for ch in ch_list)]
print('Return list of words  where sub list chars are not present using List Comprehension...' ,res2)

# ----------------------------------------------------------------------------------------------------------------

res3 = []
x = []
for ele in str_list:
    x = ele
    for ch in ch_list:
        ele = ele.replace(ch, '')

    if len(ele) == len(x):
        res3.append(ele)
print('Return list of words  where sub list chars are not present using replace...', res3)

# ------------------------------------------------------------------------------------------------------------------------
# using filter() and lambda function.


res4 = list(filter(lambda word: not any(ch in word for ch in ch_list), str_list))
print('Return list of words  where sub list chars are not present using filter and lambda...', res4)