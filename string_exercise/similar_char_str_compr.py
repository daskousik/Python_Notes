# Python – Similar characters Strings comparison
# Given two Strings, separated by delim, check if both contain same characters.
# Input : test_str1 = 'e!e!k!s!g', test_str2 = 'g!e!e!k!s', delim = '!'
# Output : True
# Explanation : Same characters, just diff. positions.
#
# Input : test_str1 = 'e!e!k!s', test_str2 = 'g!e!e!k!s', delim = '!'
# Output : False
# Explanation : g missing in 1st String.

str1 = 'e!e!k!s'

str2 = 'g!e!e!k!s'
delim = '!'

str1_split = str1.split(delim)
str2_split = str2.split(delim)

dict1 = {}
dict2 = {}
res = True
for ch in str1_split:
    if ch in dict1:
        dict1[ch] += 1
    else:
        dict1[ch] = 1

print('dict1..', dict1)

for ch in str2_split:
    if ch in dict2:
        dict2[ch] += 1

    else:
        dict2[ch] = 1

print('dict2..', dict2)

dict3 = dict1 | dict2
print(dict3)
mis=''
for key in dict3:
    if key in dict1 and dict1[key] == dict2[key]:
        continue
    else:
        mis = key
        res = False
        break

print(res, mis)



