
# Python – Convert Lists of List to Dictionary
# The original list is : [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
# The mapped Dictionary : {('a', 'b'): (1, 2), ('c', 'd'): (3, 4), ('e', 'f'): (5, 6)}

lst = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
res = {}
for ele in lst:
    key = tuple(ele[:2])
    value = tuple(ele[2:])
    res[key] = value

print(res)


