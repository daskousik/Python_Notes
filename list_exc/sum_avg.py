# Find sum and average of List in Python

lst = [4, 5, 1, 2, 9, 7, 10, 8]

lenght= len(lst)

sum = 0
for item in lst:
     sum = sum + item

print('Find sum and average of List in Python --->', sum, sum/lenght)

# ------------------------------------------------------------------------------------------------------------------
# Python | Sum of number digits in List
# Method #1 : Using loop + str()
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]

ori_list = [12, 67, 98, 34, 7]

res = []
# first iterate through the item then convert each item to string element.
for ele in ori_list:
    sum = 0
    for digit in str(ele):
        #print(digit)
        sum = sum + int(digit)
        #print(sum)
    res.append(sum)

print(res)

# --------------------------------------------------------------------------------------
# Multiply all numbers in the list using Traversal

result = 1

for ele in ori_list:

    result = result * ele

print('Multiply all numbers in the list using Traversal', result)






#digit_sum = [ele for ele in lst_str]

#print(digit_sum)
