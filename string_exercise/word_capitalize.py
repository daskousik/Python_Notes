# Python program to capitalize the first and last character of each word in a string..
# Input: hello world
# Output: HellO WorlD
# Input: welcome to geeksforgeeks
# Output: WelcomE TO GeeksforgeekS
s = 'hello world'
result = s[:1].upper() + s[1:-1] + s[-1].upper()
print('Capitalize first and last char using slicing concate...', result)

# ---------------------------------------------------------------------------------------------------------------------
# Python program to check if a string has at least one letter and one number
# Input: welcome2ourcountry34
# Output: True
#
# Input: stringwithoutnum
# Output: False

s = 'welcome2ourcountry34'
if s.isalpha() or s.isdigit():
    print('True')
# def isalpha(self) -> bool
# Return True if the string is an alphabetic string, False otherwise.
# A string is alphabetic if all characters in the string are alphabetic and
# there is at least one character in the string.
print(s.isalpha())
# def isdigit(self) -> bool
# Return True if the string is a digit string, False otherwise.
# A string is a digit string if all characters in the string are digits and
# there is at least one character in the string.
print(s.isdigit())

flag_alp = False
flag_digi = False

for ch in s:
    if ch.isalpha():
        flag_alp = True
    if ch.isdigit():
        flag_digi = True
if flag_alp and flag_digi:
 print('True')

import  re
match = re.search(r'[A-Za-z]+', s) and re.search(r'\d+', s)
if match:
    print('True')