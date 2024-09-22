# Handling missing keys in Python dictionaries
# In Python, dictionaries are containers that map one key to its value with access time complexity to be O(1). But in many applications, the user doesn’t know all the keys present in the dictionaries.
# In such instances, if the user tries to access a missing key, an error is popped indicating missing keys.
#
d = { 'a' : 1 , 'b' : 2 }
#d['c']  # KeyError: 'c' bcz key 'c' is not here.

# Python Program to Handling Missing keys in Python Dictionaries Using key
if 'c' in d:
    print(d['c'])
else:
    print('Key Not Found')
# -------------------------------------------------------------------------------------------------------------------
# Python Program to Handling Missing keys in Dictionaries Using get()
# get(key,def_val) method is useful when we have to check for the key. If
# the key is present, the value associated with the key is printed, else the def_value passed in arguments is returned.

print(d.get('a', 'Not Found get methods'))
print(d.get('c', 'Not Found get methods'))

# ----------------------------------------------------------------------------------------------------------------------
