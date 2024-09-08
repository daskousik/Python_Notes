# Python program to find the Strongest Neighbour
# find max value between adjacent  pairs gets
'''Input: 1 2 2 3 4 5
 Output: 2 2 3 4 5

 Input: 5 5
 Output: 5
'''

lst = [1, 2, 2, 3, 4, 5]
size = len(lst)
res = []
# Loop through each elements using index..
# check between adjacent pair max value..

for i in range(size -1):
    item = lst[i]
    if item > lst[i+1]:
        res.append(lst[i])
    else:
        res.append(lst[i+1])

for ele in res:
    print(ele, end=' ')
