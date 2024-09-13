# initializing lists
test_list = ["geeksforgeeks is best for geeks"]

# printing original list
print("The original list : " + str(test_list))

# char list
chr_list = ['e', 'b', 'g']

# initializing dictionary for result
res = {}

# loop through each character in the test_list and count their frequency
for char in "".join(test_list):
    if char in chr_list:
        if char in res:
            res[char] += 1
        else:
            res[char] = 1

# printing result
print("Specific Characters Frequencies : " + str(res))
