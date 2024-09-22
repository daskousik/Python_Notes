# Python program to find the sum of all items in a dictionary....
# Input : {‘a’: 100, ‘b’:200, ‘c’:300}
# Output : 600
#
# Input : {‘x’: 25, ‘y’:18, ‘z’:45}
# Output : 88

# Method #2: Using For loop to iterate through values using values() function
#
# Iterate through each value of the dictionary using values() function and keep adding it to the sum.
d = {'a': 100, 'b':200, 'c':300}

sum = 0

for val in d.values():
    sum = sum + val

print(sum)

# ----------------------------------------------------------------------------------------------------------------------
sum2 = 0
for i in d:
    sum2 = sum2 + d[i]

print(sum2)

# ----------------------------------------------------------------------------------------------------------------------


