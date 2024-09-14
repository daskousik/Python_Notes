# String slicing in Python to Rotate a String.......
# Given a string of size n, write functions to perform following operations on string.


# Input : s = "GeeksforGeeks"
#         d = 2
# Output : Left Rotation  : "eksforGeeksGe"
#          Right Rotation : "ksGeeksforGee"
#
#
# Input : s = "qwertyu"
#         d = 2
# Output : Left rotation : "ertyuqw"
#          Right rotation : "yuqwert"

# --------------------------------------------------------------------------------------------------------------------

# Using slicing..........................................
s = "GeeksforGeeks"

d = 2

L_temp_str = s[:d]
L_rotate = s[d:] + L_temp_str

R_temp = s[-d:]

R_rotate = R_temp + s[:-d]


print(R_rotate)
print(L_rotate)