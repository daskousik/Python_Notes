# Python – Insertion at the beginning in OrderedDict.....
# Given an ordered dict, write a program to insert items in the beginning of the ordered dict.
#
# Examples:
#
# Input:
# Dictionary that remembers insertion order

from collections import OrderedDict , Counter
# Dict subclass for counting hashable items. Sometimes called a bag or multiset.
# Elements are stored as dictionary keys and their counts are stored as dictionary values.

original_dict = {'a':1, 'b':2}
item = {'c', '3'}
#
# Output:  {'c':3, 'a':1, 'b':2}
#original_dict.update()

# initialising ordered dict....
ini_ordered_dict = OrderedDict(original_dict)

ini_ordered_dict.update(item)
print()
