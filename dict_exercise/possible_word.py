# Possible Words using given characters in Python...

# Given a dictionary and a character array, print all valid words that are possible using characters from the array.
# Note: Repetitions of characters is not allowed.


# Input : Dict = ["go","bat","me","eat","goal","boy", "run"]
#         arr = ['e','o','b', 'a','m','g', 'l']
# Output : go, me, goal.

Dict = ["go","bat","me","eat","goal","boy", "run"]
arr = ['e','o','b', 'a','m','g', 'l']

from collections import Counter

for ele in Dict:
    flag = 1
    for i in range(len(ele)):
        if ele[i] not in arr:
            flag = 0
    if flag == 1:
        print(ele)






