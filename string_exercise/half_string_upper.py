# Python – Uppercase Half String
# Input : test_str = 'geeksforgeek'
# Output : geeksfORGEEK
# Explanation : Latter half of string is uppercased.
test_str = 'geeksforgeek'

size = len(test_str)
middle = size//2
counter = 0
res = ''
for i in range(len(test_str)):

    if i >= middle:
        res = res + test_str[i].upper()
    else:
        res = res + test_str[i]

print('Half letter upper using loop.... ',res)

# -----------------------------------------------------------------------------------------------------------------------

# Method #2 : Using list comprehension + join() + upper()
result = test_str[:middle] + test_str[middle:].upper()
print('Half letter upper using slicing... ',result)

