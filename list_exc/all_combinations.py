# Python program to find all the Combinations in the list with the given condition
# Input: test_list = [1,2,3]
# Output:
#  [1], [1, 2], [1, 2, 3], [1, 3]
#  [2], [2, 3], [3]

test_list = [1,2,3]

for i in range(len(test_list)):

    for j in range(len(test_list)):

         if i == j:
             print([test_list[i]])
         elif   i != j :
            print([test_list[i], test_list[j]])

           

