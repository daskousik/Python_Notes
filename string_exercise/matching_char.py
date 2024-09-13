# Python | Count the Number of matching characters in a pair of string
# Input : str1 = 'abcdef'
#         str2 = 'defghia'
# Output : 4
# (i.e. matching characters :- a, d, e, f)
#
# Input : str1 = 'aabcddekll12@'
#         str2 = 'bb2211@55k'
# Output : 5
# (i.e. matching characters :- b, 1, 2, @, k)

str1 = 'abcdef'
str2 = 'defghia'
res =''
count = 0
for ch in str1:
    if ch in str2:
        res = res + ch
        count = count + 1

print('Matching count is ...', count)
print('Matching charecters...', res)

