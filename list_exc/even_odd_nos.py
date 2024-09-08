
list1 = [10, 21, 4, 45, 66, 93]

# Method 1 : using for loop

for item in list1:
    if item % 2 == 0:
        print('even number using for loop', item)

# -----------------------------------------------------------------------------------------------------------
even_nos = [x for x in list1 if x % 2 == 0]

print('Even number using list comprehension', even_nos)
# ------------------------------------------------------------------------------------------------------------

num = 0
while num < len(list1):

    if list1[num] % 2 == 0:
        print('Even number using while loop', list1[num])

    else:
        pass
    num = num + 1
# -----------------------------------------------------------------------------------------------------------------
