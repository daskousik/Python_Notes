from collections import  Counter
# Check if element exists in list in Python
# Case 1 using in
val = 3
lst = [1, 3, 4, 3, 7]
print(lst)
def check(val, lst):
    if val in lst:
        return True
    else:
        return False

print('Check if element exists in list in Python using case 1 in -->', check(val, lst))
# ---------------------------------------------------------------------------------------------------------------
# Case 2 using  for loop

for ele in lst:

    if ele == val:
        print('value is exit using for loop')

#-----------------------------------------------------------------------------------------------------------------

#using any method..

result = any([item in lst for item in lst])
print(result)

# -----------------------------------------------------------------
# Check if element exists in list using Counter() function
# The provided Python code uses the Counter class from the collections
# module to calculate the frequency of each element in the test_list.
# Counter({3: 2, 1: 1, 4: 1, 7: 1})  # Return elements count..
freq = Counter(lst)
print(freq)

if freq[15] > 0:
    print('Yes, elements is exist')

else:
    print('Element does not exist')





