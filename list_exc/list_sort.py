lst = [4, 1, 6]
# ouput = [6, 4, 1]
num = 0

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] < lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

print(lst)