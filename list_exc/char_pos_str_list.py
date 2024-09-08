# Python program to find the character position of Kth word from a list of strings

# Input : test_list = [“geekforgeeks”, “is”, “best”, “for”, “geeks”], K = 21
# Output : 0
# Explanation : 21st index occurs in “geeks” and point to “g” which is 0th element of word.
#
# Input : test_list = [“geekforgeeks”, “is”, “best”, “for”, “geeks”], K = 15
# Output : 1
# Explanation : 15th index occurs in “best” and point to “e” which is 1st element of word.

str_list = ['geekforgeeks', 'is', 'best', 'for', 'geeks']
k = 21
count = 0
for ele in str_list:

    for ch in range(len(ele)):

        count = count + 1
        if count == k + 1:
            print('Find the character position of Kth word from a list of strings using loop', ch)


# --------------------------------------------------------------------------------------------------------------
# Method #1 : Using enumerate() + list comprehension
#
# In this, we use nested enumerate() to check indices for words,
# and strings in the list, list comprehension is used to encapsulate logic in 1 liner.

res = [ele[0] for ele in enumerate(str_list) for ch in enumerate(ele[1])]
res = res[k]

print(res)

# -------------------------------------------------------------------------------------------------------------------

