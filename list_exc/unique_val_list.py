# How to count unique values inside a list
# No of unique items are: 5
input_list = [1, 2, 2, 5, 8, 4, 4, 8]
count = 0
for i in  range(len(input_list)):
    for j in range(i + 1, len(input_list)):
        if input_list[i] == input_list[j]:
            count = count + 1
        else:
            count = count + 1

print(count)

res = []
num = 0
# In this method we are going to be using loop and if condition with take an empty list.
for item in input_list:
    if item in res:  # if item not in res:
        pass
    else:
        res.append(item)
        num = num + 1
print(num)

# -----------------------------------------------------------------------------------------------
# We can use another method as set to check no dupicate value.
set_res = set(input_list)
print(set_res)
print(len(set_res))