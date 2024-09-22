d = {'a': 100, 'b':200, 'c':300}

print(len(d))
# The size of a Dictionary means the amount of memory (in bytes) occupied by a Dictionary object.

# Get Size of Dictionary using getsizeof() function..........

import  sys

print(str(sys.getsizeof(d)) + 'bytes')  # 184bytes

# Get Size of Dictionary using __sizeof__() method
# Python also has an inbuilt __sizeof__() method
# to determine the space allocation of an object without any additional garbage value.

print(str(d.__sizeof__()) + 'bytes') # 168bytes
