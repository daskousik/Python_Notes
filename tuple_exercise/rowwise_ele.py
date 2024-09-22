# Output : [[(‘Gfg’, 3, 1)], [(‘best’, 1, 2)]]


test_list = [[('Gfg', 3)], [('best', 1)]]

cus_eles = [1, 2]

for ele1, ele2 in zip(test_list, cus_eles):
    for item in ele1:
        print([item, ele2])


