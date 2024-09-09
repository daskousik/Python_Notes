# Reverse Words in a Given String in Python
# Examples:
#
# Input : str =" geeks quiz practice code"
# Output : str = code practice quiz geeks
# Input : str = "my name is laxmi"
# output : str= laxmi is name my


# ----------------------------------------------------------------------------------------------------------------------
# input string
in_str = "geeks quiz practice code"
print('Input string.... ', in_str)

# reversed the words in list
res = in_str.split(' ')[::-1]
# join each word .
res = ' '.join(res)

print('Reverse the given string using split and join .... ', res)

# ----------------------------------------------------------------------------------------------------------------------
