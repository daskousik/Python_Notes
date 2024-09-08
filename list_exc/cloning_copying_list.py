# Copy or Clone a List Using Slicing Technique

li1 = [4, 8, 2, 10, 15, 18]
print('Original list   ', li1)

copy_list = li1[:]

print('Copy a list using Slicing   ',copy_list)

# -----------------------------------------------------------------------------
# Clone or Copy Using Python extend() method

l1_copy = li1.extend(li1)

print('Clone or Copy Using Python extend() method ', l1_copy)
#--------------------------------------------------------------------------------------
# Python Copy List Using Assignment Operator
li2 = [4, 8, 2, 10, 15, 18]
l1_assi = li2

print('Python Copy List Using Assignment Operator', l1_assi)
#-------------------------------------------------------------------------------

# Python Cloning or Copying a list Using List Comprehension  to clone or copy a list.

list_comp = [item for item in li2]
print('Python Cloning or Copying a list Using List Comprehension  ', list_comp)

#-----------------------------------------------------------------------------------------

# Python append() to Clone or Copy a list
# This can be used for appending and adding elements to list or copying them to a new list.
# It is used to add elements to the last position of the list.

list_appd = []

for item in li2:
    list_appd.append(item)
print('Python append() to Clone or Copy a list  ', list_appd)

# --------------------------------------------------------------