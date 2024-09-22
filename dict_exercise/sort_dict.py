#* Python | Sort Python Dictionaries by Key or Value
#There are two elements in a Python dictionary-keys and values. You can sort the dictionary by keys, values, or both.
myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
mykeys = list(myDict.keys())
mykeys.sort()
sorted_dict = {i : myDict[i] for i in mykeys}
print(sorted_dict)