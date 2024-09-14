# Python – Convert Snake case to Pascal case....
# Input : geeks_for_geeks Output : GeeksforGeeks
# Input : left_index Output : leftIndex

s = 'geeks_for_geeks'
s_pascal = s.title().replace('_', '')
print(s_pascal)
res = ''
counter = 0
for ind, ch in enumerate(s):

    if ind == 0:
        res = res + ch.upper()

    elif ch == '_':
        res = res + ch.replace('_', '')
        counter = ind
        print(counter)
    elif counter + 1 == ind:
        res = res + ch.upper()
    else:
        res = res + ch
print(res)

from functools import reduce
res_f = reduce(lambda a, b: a + b.title(), s.split("_"))
print(res_f)

