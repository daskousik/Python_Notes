# Python – Least Frequent Character in String
# The original string is : GeeksforGeeks
# The minimum of all characters in GeeksforGeeks is : f

from collections import  Counter
s = 'GeeksforGeeks'

count = Counter(s)

for item, value in count.items():
    if value == 1:
        print('The minimum of all characters in GeeksforGeeks is :', item)
        break

freq_dict = {ch: s.count(ch) for ch in s}
min_val = min(freq_dict.values())
print(min_val)
print(freq_dict)

all_freq = {}
for ch in s:
    all_freq[ch] += 1
    if ch in all_freq:
        all_freq[ch] += 1
    else:
        all_freq[ch] = 1

print(all_freq)




