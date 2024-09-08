# Python – List product excluding duplicates
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : " + str(test_list))
# Duplication removal list product : 90
res = []
dup = []

# 1. Check the each item started from first using loop.
# if

for item in test_list:
    if item not in res:
        res.append(item)
    else:
        dup.append(item)
print(dup)