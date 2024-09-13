# Split the string into list of strings
#
# Input : Geeks for Geeks
# Output : ['Geeks', 'for', 'Geeks']
#
#
# Join the list of strings into a string based on delimiter ('-')
#
# Input :  ['Geeks', 'for', 'Geeks']
# Output : Geeks-for-Geeks

s = 'Geeks for Geeks'

result = '-'.join([word for word in s.split()])
print(result)