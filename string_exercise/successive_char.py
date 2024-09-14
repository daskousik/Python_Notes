# Python – Successive Characters Frequency...........
# a problem in which we need to find the frequency of next character of a particular word in string.
# Input : test_str = 'geeks are for geeksforgeeks', que_word = "geek"
# Output : {'s': 3}
import re
test_str = 'geeks are for geeksforgeeks'
que_word = "geek"
pattern = r'^geek+'
que_len = len(que_word)
#print(que_len)
freq_dict = {}
res = ''
for i in range(len(test_str) ):
    if test_str[i:i+que_len] == que_word:
        #print(test_str[que_len])
        res = test_str[que_len]
        if res in freq_dict:
            #print(freq_dict[res])
            freq_dict[res] += 1
        else:
            freq_dict[res] = 1

print(freq_dict)