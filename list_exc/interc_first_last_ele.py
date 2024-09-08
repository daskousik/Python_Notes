# Python program to interchange first and last elements in a list.

# Initialize a list
my_list = [1, 2, 3, 4, 5]
print('original list---------->', my_list)
# Case 1 using index
my_list[0], my_list[-1] = my_list[-1], my_list[0]
print('Process 1 to interchange first and last ele -->', my_list)


# -------------------------------------------------------------------------------------------------------
# Case2 using temp variable.
def swaplist(new_list):
    size = len(new_list)
    temp = new_list[0]
    new_list[0] = new_list[size - 1]
    new_list[size - 1] = temp

    return new_list


print('Process 2 back to original interchange first and last ele -->', swaplist(my_list))

# ----------------------------------------------------------------------------------------
# Cash 3 using tuple variable

def swaptwo(my_list):
    res = []
    if len(my_list) > 1:

        res = my_list[-1:] + my_list[1:-1] + my_list[:1]

    return res




print('process 3 to list slicing using ----->', swaptwo(my_list))

# -----------------------------------------------------------------------------------

last_name = "DASkousik"
last_name = last_name[-1] + last_name[1:-1] + last_name[0]
print('string slicing changes first and last-->{}'.format(last_name))
