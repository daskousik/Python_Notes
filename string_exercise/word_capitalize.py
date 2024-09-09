# Python program to capitalize the first and last character of each word in a string..
# Input: hello world
# Output: HellO WorlD
# Input: welcome to geeksforgeeks
# Output: WelcomE TO GeeksforgeekS
s = 'hello world'
result = s[:1].upper() + s[1:-1] + s[-1].upper()
print('Capitalize first and last char using slicing concate...', result)