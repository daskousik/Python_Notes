
# K’th Non-repeating Character in Python using List Comprehension and OrderedDict

# Input : str = geeksforgeeks, k = 3
# Output : r
# First non-repeating character is f,
# second is o and third is r.
#
# Input : str = geeksforgeeks, k = 2
# Output : o
#
# Input : str = geeksforgeeks, k = 4
# Output : Less than k non-repeating
#          characters in input.

from collections import  OrderedDict

str1 = 'geeksforgeeks'
k = 2

result = {i: str1.count(i) for i in str1 }
print(result)
count = 0
for key, value in result.items():
    if value == 1:
        count = count + 1
        if count == k:
            print(key)
            break

# OrderedDict returns a dictionary data
        # structure having characters of input

# string as keys in the same order they
        # were inserted and 0 as their default value

dict = OrderedDict.fromkeys(str1, 0)

print(dict)

for i in str1:
    dict[i]+=1
print(dict)
