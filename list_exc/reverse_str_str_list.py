# Python | Reverse All Strings in String List
# The original list is : ['geeks', 'for', 'geeks', 'is', 'best']
# The reversed string list is : ['skeeg', 'rof', 'skeeg', 'si', 'tseb']
# Takes a string list ....

str_list = ['geeks', 'for', 'geeks', 'is', 'best']

#Method #1 : Using list comprehension
# This method performs the same task in the background as done by the looping constructs.
# The advantage this particular method provides is that this is a one liner and also improves code readability.

# ----------------------------------------------------------------------------------------------------------------------
# lambda_expr        ::=  "lambda" [parameter_list]: expression
# lambda_expr_nocond ::=  "lambda" [parameter_list]: expression_nocond
#
# Lambda expressions (sometimes called lambda forms) are used to create anonymous functions.
# The expression lambda arguments: expression yields a function object.
# The unnamed object behaves like a function object defined with
# def <lambda>(arguments):
#     return expression
#  Note that functions created with lambda expressions cannot contain statements or annotations.
reverse = lambda sub: sub[::-1]
print(reverse)
# ----------------------------------------------------------------------------------------------------------------


# map(func, *iterables) –> map object
# Make an iterator that computes the function using arguments from each of the iterables.
# Stops when the shortest iterable is exhausted.
result = list(map(reverse, str_list))
print('The reversed string list using lambda func and map iterator ',result)
#---------------------------------------------------------------------------------------------------------------------------


res = [sub[::-1] for sub in str_list]

print('The reverse list are using list Comprehension slicing', res)

# ----------------------------------------------------------------------------------------------
res2 = []
for ele in str_list:
    res2.append(ele[::-1])

print('The reversed list are using loop ',res2)
