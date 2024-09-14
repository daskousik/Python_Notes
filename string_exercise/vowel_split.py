# Input : test_str = ‘GFGaBst’
# Output : [‘GFG’, ‘Bst’]
# Explanation : a is vowel and split happens on that.
#
# Input : test_str = ‘GFGaBstuforigeeks’
# Output : [‘GFG’, ‘Bst’, ‘f’, ‘r’, ‘g’, ‘ks’]
# Explanation : a, e, o, u, i are vowels and split happens on that.


test_str = 'GFGaBstuforigeeks'
vowels = 'aeiouAEIOU'



result = [ch.split(ch) for ch in test_str if ch in vowels]
res = ''

for ch in test_str:
    if ch in vowels:
        res = res + ','
    else:
        res = res + ch
print(res)

result = res.split(',')

print(result)
