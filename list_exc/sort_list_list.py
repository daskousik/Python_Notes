# Python – Reverse Row sort in Lists of List
# The original list is : [[4, 1, 6], [7, 8], [4, 10, 8]]
# The reverse sorted Matrix is : [[6, 4, 1], [8, 7], [10, 8, 4]]

lst = [[4, 1, 6], [7, 8], [4, 10, 8]]
for ele in lst:
    #print(ele)
    for i in range(len(ele)):
        for j in range(i + 1, len(ele)):
            if ele[i] < ele[j]:
                temp = ele[i]
                ele[i] = ele[j]
                ele[j] = temp

print('sort list using loop',lst)



