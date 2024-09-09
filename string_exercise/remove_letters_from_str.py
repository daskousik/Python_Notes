# How to Remove Letters From a String in Python......
# Input: 'Geeks123For123Geeks'
# Output: GeeksForGeeks

in_str = 'Geeks123For123Geeks'
# replace()
# Return a copy with all occurrences of substring old replaced by new.
#
# count
# Maximum number of occurrences to replace. -1 (the default value) means replace all occurrences.
# If the optional argument count is given, only the first count occurrences are replaced.

new_str = in_str.replace('123', '', 1) # Output GeeksFor123Geeks
print('Remove letters from string using replace() ' ,new_str)
# ----------------------------------------------------------------------------------------------------------------------
res_str = ''.join([in_str[i] for i in range(len(in_str)) if i != 2])
print('remove letters from string using list comprehension and join() ' ,res_str)