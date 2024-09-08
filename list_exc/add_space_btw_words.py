# Input : test_list = [“gfgBest”, “forGeeks”, “andComputerScienceStudents”]
# Output : [‘gfg Best’, ‘for Geeks’, ‘and Computer Science Students’]
# Explanation : Words segregated by Capitals.
#
# Input : test_list = [“ComputerScienceStudentsLoveGfg”]
# Output : [‘Computer Science Students Love Gfg’]
# Explanation : Words segregated by Capitals.

test_list = ['gfgBest', 'forGeeks', 'andComputerScienceStudents']

# Method #1 : Using loop + join()
res = []

for ele in test_list:
    temp = ''
    for ch in ele:
        if ch.isupper():
           temp = temp + ' ' + ch
        else:
            temp = temp + ch
    res.append(temp)
print('Add Space btw the words using loop...', res)

# -----------------------------------------------------------------------------------------------------------------
# Method #2 : Using regex() + list comprehension
import  re
