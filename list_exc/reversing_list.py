# Reversing a List in Python..
# Input: list = [4, 5, 6, 7, 8, 9]
# Output: [9, 8, 7, 6, 5, 4]

lst = [4, 5, 6, 7, 8, 9]

size = len(lst)

print('Origanal List ---> ' + str(lst))

# 1. Reverse List Using Slicing Technique..
rev_lst = lst[::-1]
print('Reverse List Using Slicing Technique ---> ', rev_lst)

# ----------------------------------------------------------------------------------------
# 2. Reverse List by Swapping Present and Last Numbers at a Time


def reverse_list(lst, size):

    if size == 1:
        return lst
    elif size == 2:
        lst[0] = lst[-1]
        lst[-1] = lst[0]
        return lst
    else:
        i = 0
        for i in range(size//2):
            if lst[i] != lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[size - i -1]
                lst[size - i -1] = temp
            i = i + 1
        return lst


print('Reverse List Using Swap Technique --->', reverse_list(lst, size))

# --------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------

# 4. Reverse a List Using a Two-Pointer Approach






new_list = [4, 5, 6, 7, 8, 9, 1, 2, 5, 6]
print('Original new List ----> ', new_list)
def reverse_two_pointer(new_list):

    left = 0
    right = len(new_list) - 1

    while left < right:
        temp = new_list[left]
        new_list[left] = new_list[right]
        new_list[right] = temp
        left = left + 1
        right = right - 1

    return new_list


print('Reverse a List Using a Two-Pointer Approach -----> ', reverse_two_pointer(new_list))

# -------------------------------------------------------------------------------------------------

# 5. Reverse a List Using the insert() Function

l5 = [1, 2, 3, 4, 5]
l = []
for i in l5:
    l.insert(0, i)
print('5. Reverse a List Using the insert() Function--->', l)

# ------------------------------------------------------------------------------------------------------
# 6. Reverse a List Using List Comprehension
l6 = [15, 14, 13, 12, 11, 10]
l6 = [i for i in l6]