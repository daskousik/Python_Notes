# Characteristcs of List .............
    # The lists are ordered, allow duplicate values.
    # The element of lists can access by index.
    # The lists are mutable(we can modify) types.
    # A list can store the number of various data types.

# Access Items

list = ["apple", "banana", "cherry","orange", "kiwi", "melon", "mango"]  # Note: The first item has index 0.

print(list[1])

print(list[-1]) # -1 refers to the last item.

print(list[1:3]) # Note: The search will start at index 1 (included) and end at index 3 (not included).

print(list[:4]) #  beginning to, but NOT including 4
print(list[2:]) # returns the items from 2 to the end.

# Change Item Value.......

list[1] = "Chiku"
print(list)

# Add List Items

list.append("Banana")
print(list)

#For Loop

for x in list:
    print(x)
    