# Python | Multiple indices Replace in String

test_str = 'geeksforgeeks is best'
print("The original string is : " + test_str)
test_list = [2, 4, 7, 10]
repl_char = '*'

temp = list(test_str)
for i in test_list:
    temp[i] = repl_char

res = ''.join(temp)

print(res)