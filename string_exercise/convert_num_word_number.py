# Convert numeric words to numbers
# Given a string S, containing numeric words, the task is to convert the given string to the actual number.
#
# Example:
#
# Input: S = “zero four zero one”
# Output: 0401
#
# Input: S = “four zero one four”
# Output: 4014

S = 'zero four zero one'
help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}
result = ''.join([help_dict[word] for word in S.split()])
print(result)

