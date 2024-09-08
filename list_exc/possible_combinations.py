# Given 3 digits a, b, and c. The task is to find all the possible combinations from these digits.
#
# Examples:
#
# Input: [1, 2, 3]
# Output:
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1
# loop through each once two pair are not same then consider from each one loop  value.
# means each one loop  has discrete value. then one only consider.

lst = [1, 2, 3]
for i in range(len(lst)):
    for j in range(len(lst)):
        for k in range(len(lst)):
            if i !=j and j !=k and i != k:
                print((lst[i], lst[j], lst[k]))


from itertools import permutations

comb = permutations(lst)
print(comb)

for i in comb:
    print(i)
