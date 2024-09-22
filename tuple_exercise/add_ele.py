test_list = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
# Output [(5, 7, 8), (6, 8, 10), (7, 12, 5)]

add_ele = 4

res = []

res = [tuple(ele + add_ele for ele in item) for item in test_list]

print(res)