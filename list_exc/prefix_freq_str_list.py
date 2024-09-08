import  re
test_list = ['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS', 'Gcourses']

# printing original list
print("The original list is : " + str(test_list))

# Initializing substring
test_sub = 'gfg'
count = 0
res = 0
res2 = 0

for ele in test_list:
    # S. find(sub[, start[, end]]) -> int
    # Return the lowest index in S where substring sub is found.
    if ele.find(test_sub) == 0:
        res = res + 1
    # S. startswith(prefix[, start[, end]]) -> bool
    # Return True if S starts with the specified prefix, False otherwise. With optional start, test S beginning at that position.
    # With optional end, stop comparing S at that position. prefix can also be a tuple of strings to try.
    if ele.startswith(test_sub):  # ele.find(test_sub) == 0

        count = count + 1
    # Try to apply the pattern at the start of the string, returning a Match object, or None if no match was found.
    if re.match(f'^{test_sub}', ele):
        res2 = res2 + 1
print("Strings count with matching frequency using loop anf if startsWith : ", count)
print("Strings count with matching frequency using loop anf if find : ", res)
print("Strings count with matching frequency using loop anf if match : ", res2)

# --------------------------------------------------------------------------------------------------------------------

