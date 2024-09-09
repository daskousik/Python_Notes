# Python program to check whether the string is Symmetrical or Palindrome..
# Given a string. the task is to check if the string is symmetrical and palindrome or not.
# A string is said to be symmetrical if both the halves of the string are the same
# and a string is said to be a palindrome string if one half of the string is the reverse of the other half or if a string appears the same
# when read forward or backward.

# Input: khokho
# Output:
# The entered string is symmetrical
# The entered string is not palindrome
#
# Input:amaama
# Output:
# The entered string is symmetrical
# The entered string is palindrome

# --------------------------------------------------------------------------------------------------------
# Approach 2: Using Slicing
def check_sym_pali(input_str):
    size = len(input_str)
    mid = size//2
    str1 = input_str[:mid]
    str2 = input_str[mid:]
    print(str1)
    print(str2)

    if str1 == str2:
        print('The entered string is symmetrical')
    else:
        print('The entered string is not symmetrical')

    if str1 == str2[::-1]:
        print('The entered string is palindrome')
    else:
        print('The entered string is not palindrome')

# -----------------------------------------------------------------------------------------------------------------------
input_str = 'amaama'


check_sym_pali(input_str)