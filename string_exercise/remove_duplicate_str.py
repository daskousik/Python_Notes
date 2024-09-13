# Remove All Duplicates from a Given String in Python

# Input : geeksforgeeks
# Output : geksfor
res = ''
s = 'geeksforgeeks'
new_str = ''
for ch in s:
    if ch not in res:
        res = res + ch
    else:
        new_str = new_str + ch
print(res)

from collections import Counter

result = Counter(s)
print(result)


