lst = [2, 3, 5, 6, 7]

# Clear a List using Python List clear()
print(lst)
#clr = lst.clear()
#print('Clear list using clear method -->',clr)
# ----------------------------------------------------------------------

# Clear a List by Reinitializing the List
#lst = []
#print(lst)

# -------------------------------------------------------------------------
# Python del can be used to clear the list elements in a range, if we don’t give a range, all the elements are deleted.

del  lst[:1]
print(lst)
# --------------------------------------------------------------------------------
lst.pop(1) # deleted element on passing index number.
print(lst)
# ---------------------------------------------------------------------------------

# delete list using slice ........
lst = lst[:-1] # last one will not  consider.
print(lst)

# ------------------------------------------------------------------------------
