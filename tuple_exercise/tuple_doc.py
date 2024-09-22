# Tuples are immutable data type.
# Ordered
# duplicate not allow.
# A list can store the number of various data types.
item_tuple = ("apple", "banana", "cherry", "apple", "cherry")
print(item_tuple)
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

t_to_list = list(item_tuple)
print(t_to_list)
t_to_list[1] = "Chiku"
print(t_to_list)
l_to_tuple = tuple(t_to_list)
print(l_to_tuple)
# --------------------------------------------------------------------------------------------------------------------
# More.....
# Tuple is a collection of Python objects much like a list.
# The sequence of values stored in a tuple can be of any type, and they are indexed by integers.
# Values of a tuple are syntactically separated by ‘commas’.
# Although it is not necessary, it is more common to define a tuple by closing the sequence of values in parentheses.
