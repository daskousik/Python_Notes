# Python – Extract values of Particular Key in Nested Values.......

# Given a dictionary with nested dictionaries as values, extract all the values with of particular key...
# Input : test_dict = {‘Gfg’ : {“a” : 7, “b” : 9, “c” : 12}, ‘is’ : {“a” : 15, “b” : 19, “c” : 20}, ‘best’ :{“a” : 5, “b” : 10, “c” : 2}}, temp = “b”
# Output : [9, 10, 19]
# Explanation : All values of “b” key are extracted.
#
# Input : test_dict = {‘Gfg’ : {“a” : 7, “b” : 9, “c” : 12}, ‘is’ : {“a” : 15, “b” : 19, “c” : 20}, ‘best’ :{“a” : 5, “b” : 10, “c” : 2}}, temp = “a”
# Output : [7, 15, 5]
# Eplanation : All values of “a” key are extracted...

test_dict = {'Gfg': {'a': 7, 'b': 9, 'c': 12},
'is': {'a': 15, 'b': 19, 'c': 20}, 'best': {'a': 5, 'b': 10, 'c': 2}}

temp = 'b'

l =[]

for key , value in test_dict.items():
    # print(value)
    if temp in value:
        l.append(value[temp])

print(l)

