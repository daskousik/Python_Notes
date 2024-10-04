# Use  Python Module.....
import sys
import  keyword
import  operator
import os
from datetime import datetime

# Keywords....
#   Keywords are reserved words in Python and can not be used for identifier..
print(keyword.kwlist)
print(len(keyword.kwlist))

# ======================================================================================================================
# Indentifier...
#   An identifier is a name given to entities like class, function, variable , etc. It helps to diffrenciate
#   one entity from another..
#1var = 10   # # Identifier can't start with a digit.

#val2@ = 10 # Identifier can't use special symbols.

#import = 10 # SyntaxError: invalid syntax... Keywords can't be used as identifiers.

# """
# Correct way of defining an identifier
# (Identifiers can be a combination of letters in lowercase (a to z) or uppercase (
# """

val2 = 10
val_ = 2

# ======================================================================================================================

# Comments in Python....
#  Comments can be used to explain the code for more readabilty.

# single line comments
val = 100
# Multiple
# line
# comments..
val = 20

'''
Multiple line of comments...in python..
'''

# ======================================================================================================================

# Statements.....
#   Instructions that a Python interpreter can execute.

# single line statements..
p = 10 + 10
print(p)
# Multiple line statements..

p1 = 10 + \
    10 + \
    100

print(p1)

# Multiple line statement...

l = [10,
     20,
     50,
     ]

print(l)

# =====================================================================================================================

# Indentation

#Indentation refers to the spaces at the beginning of a code line(4 time backspace). It is very important as Python uses
#   indentation to indicate a block of code.If the indentation is not correct we will end up with
#   IndentationError error.

if p == 10:
    print("Correct Indentation")

if p == 100:
    pass
#print('Wrong Indentation')


for i in range(len(l)):
    print("correct indention")

# ======================================================================================================================

# Docstrings......
#   1) Docstrings provide a convenient way of associating documentation with functions, classes,methods or modules.
#   2) They appear right after the definition of a function, method, class, or module.

def square(num):
    '''Square function:  :- This function will return the square of a number'''
    return  num **2

print(square(2))  # Call function

print(square.__doc__) # # We can access the Docstring using __doc__ method

# ======================================================================================================================

# Variables.....
#  A Python variable is a reserved memory location to store values.
#  A variable is created the moment
#  you first assign a value to it


'''id() function returns the “identity” of the object.
    - The identity of an object - Is an integer
    - Guaranteed to be unique
    - Constant for this object during its lifetime. 
'''
print(id(p))
hex(id(p)) # Memory address of the variable
type(p)    # type of the variable

p = p + 10 # Variable Overwriting

# ======================================================================================================================

# Variable Assigment..
intvar = 10 # Integer variable
floatvar = 2.57 # Float Variable
strvar = "Python Language" # String variable


print(intvar)
print(floatvar)
print(strvar)

# ======================================================================================================================
# Multiple Assignments....
intvar , floatvar , strvar = 10,2.57,"Python Language" # Using commas to separate
print(intvar)
print(floatvar)
print(strvar)

p1 = p2 = p3 = p4 = 44 # All variables pointing to same value
print(p1,p2,p3,p4)

# ======================================================================================================================

# Data Type.........

# Numeric
val1 = 10 # Integer data type
print(val1)
print(type(val1)) # type of object
print(sys.getsizeof(val1)) # size of integer object in bytes
print(val1, " is Integer?", isinstance(val1, int))

# Float

val2 = 92.78 # Float data type
print(val2)
print(type(val2)) # type of object
print(sys.getsizeof(val2)) # size of float object in bytes
print(val2, " is float?", isinstance(val2, float)) # Val2 is an instance of float

# Complex

val3 = 25 + 10j # Complex data type
print(val3)
print(type(val3)) # type of object
print(sys.getsizeof(val3)) # size of float object in bytes
print(val3, " is complex?", isinstance(val3, complex)) # val3 is an instance of complex

# Boolean

# Boolean data type can have only two possible values true or false.

bool1 = True
bool2 = False
print(type(bool1))  #<class 'bool'>

print(type(bool2)) # <class 'bool'>

isinstance(bool1, bool) # True
bool(0)  # False
bool(1) # True

bool(None) # False

# ======================================================================================================================

# Strings...
# String Creation

str1 = "HELLO PYTHON"

# Define String with Single Quotes
mystr = 'Hello World'
print(mystr)
# Define String with double Quotes
mystr = "Hello World"
print(mystr)
# Define String with triple qoutes
mystr = '''Hello
            World'''
print(mystr)

mystr = """Hello 
      World"""
print(mystr)

mystr = ('Happy ' 
         'Birthday ' 
         'Too')
print(mystr)

mystr2 = 'whoo '
mystr2 = mystr2 *5
print(mystr2)

# Length of the strings..
len(mystr2)


# String Indexing......
#  0 --> N    # Forward Indexing
# -N <-- -1   # Backward Indexing
# String Slicing

mystr2[:2]

# Update & Delete String --Both are not support directly means string is immutable

#TypeError: 'str' object does not support item assignment

# NameError: name 'srt1' is not defined

# String concatenation..
mystr3 = mystr + mystr2

print(mystr3)

# Iterating through a String..
mystr1 = "Hello Everyone"
for i in mystr1:
    print(i)

for i in enumerate(mystr1):
    print(i)

list(enumerate(mystr1))

# String Membership

print('Hello' in mystr1)  # # Check whether substring "Hello" is present in string

# String Partitioning
"""
The partition() method searches for a specified string and splits the string into
 - The first element contains the part before the argument string.
 - The second element contains the argument string.
 - The third element contains the part after the argument string.
"""

str5 = "Natural language processing with Python and R and Java"
L = str5.partition("and")
print(L)

L = str5.rpartition("and")
print(L)

# String Functions
mystr4 = '   Hello Everyone    '
print(mystr4)

print(mystr4.strip())  # # Removes white space from begining & end

print(mystr4.rstrip())  # # Removes all whitespaces at the end of the string

print(mystr4.lstrip()) # # Removes all whitespaces at the begining of the string

mystr5 = "*********Hello Everyone***********All the Best**********"

print(mystr5)
print(mystr5.strip('*'))  # Remove all the '*' characters from beginning and end of the string.

print(mystr5.lstrip('*'))  # Remove all the '*' characters from beginning of the string.

print(mystr5.rstrip('*')) # Remove all the '*' characters from end of the string.

mystr6 = '  Hello World      '
print(mystr6)

print(mystr6.upper()) # Return whole string in uppercase.

print(mystr6.lower())  # Return whole string in lowercase.

print(mystr6.replace('He','Ho')) # Replace substring 'He' with 'Ho'

print(mystr6.replace(' ', '')) # Remove whole white space.

mystr7 = "one two Three one two two three"

print(mystr7.count('one')) # # Number of times substring "one" occurred in string.

print(mystr7.startswith('one')) # Return boolean True if string starts with 'one'.

print(mystr7.endswith('three')) # Return boolean True if string end with 'three'.

print(mystr7.split())  # # Split String into substrings.

# Combine string and numbers using format method....

num1 = 10
num2 = 20
num3 = 30

res = 'cost of item1, item2 and item3 are {}, {} and {}'
print(res.format(num1, num2,  num3))

res2 = 'cost of item1, item2 and item3 are {0}, {1} and {2}'
print(res2.format(num1, num2, num3))
print(f"cost of item1, item2 and item3 are {num1}, {num2} and {num3}")


mystr8 = '123456789'
print(mystr8.isalpha()) # return True if all character in the text are letter.
print(mystr8.isalnum()) # return True if a string contains only letter or number.
print(mystr8.isdecimal()) # return True if all characters are decimal
print(mystr8.isnumeric())


mystr9 = 'ABCDEF'
print(mystr9.isupper())   # # Returns True if all the characters are in upper case
print(mystr9.islower()) # # Returns True if all the characters are in lower case


# Using Escape Character..
#Using double quotes in the string is not allowed.
# mystr = "My favourite TV Series is "Game of Thrones""

#Using escape character to allow illegal characters
mystr = "My favourite series is \"Game of Thrones\""

print(mystr)


# List

#   1) List is an ordered sequence of items.
# 2) We can have different data types under a list. E.g we can have integer, float and string items in
# a same list.

# List Creation...

list1 = [] # Create Empty list.

list2 = [10,30,60] # List of integers numbers

list3 = [10.77,30.66,60.89] # List of float numbers

list4 = ['one','two' , "three"] # List of strings

list5 = ['Asif', 25 ,[50, 100],[150, 90]] # Nested Lists

list6 = [100, 'Asif', 17.765] # List of mixed data types

len(list6) #Length of list

# List Indexing
# 0 ----> N     # Forward Indexing.
# -N <---- -1   # Backward Indexing.

list2[0] # Retreive first element of the list

list4[0] # Retreive first element of the list

list4[0][0] # Nested indexing - Access the first character of the first list elem

list4[-1] # Last item of the list

# List Slicing

print(list4)

list4.append('Four') # # Add an item to the end of the list.
print(list4)

list4.insert(1,'two_2')
print(list4)  # Add an item at index location.

list4.remove('two_2') # remove item 'two_2'
print(list4)

list4.pop() # remove last item in the list
print(list4)

list4.pop(1) # remove item at index location 1 in the list.
print(list4)

# # Change value of the list

list4[0] = 1
print(list4)

myslist = [1, 2, 3, 4]
myslist.clear() # # Empty List / Delete all items in the list
print(myslist)

# Copy List..
mylist = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

mylist1 =  mylist  # Create a new list or references 'mylist1'

print(id(mylist), id(mylist1))  # The address both the mylist and mylist1 are the same.

mylist2 = mylist.copy()
print(id(mylist2))  # The address mylist2 will be different

# Assign a value in mylist1
mylist[0] = 1
print(mylist)
print(mylist1)
# mylist1 will also be impacted as it is pointing to the same list.

# # Copy of list mylist2 won't be impacted due to changes made on the original list.
print(mylist2)

# Join Lists..
list1 = ['one', 'two', 'three', 'four']
list2 = ['five', 'six', 'seven', 'eight']

list3 = list1 + list2  # # Join two lists by '+' operator
print(list3)

list1.extend(list2) # #Append list2 with list1


# List Membership
'one' in list1 # check if 'one' exist in list1 list .


# Reverse & Sort List......

list1.reverse() # # Reverse the list
print(list1)

list1[::-1] # # Reverse the list
mylist3 = [9,5,2,99,12,88,34]
mylist3.sort()
print(mylist3) # Sort list in ascending order

mylist3.sort(reverse=True)
print(mylist3)  # Sort list in descending order.

print(sorted(mylist3))  # # Returns a new sorted list and doesn't change original list.

# Loop through a list..
for i in list1:
 print(i) # one, two......

for i in enumerate(list1):
 print(i) # (0, 'eight').....

# count

print(list1.count('one'))  # # Number of times item "one" occurred in the list.

# All / Any
# The all() method returns:
#   True - If all elements in a list are true
#   False - If any element in a list is false

# The any() function returns True if any element in the list is True. If not, any() returns False.

list6 = [1, 2, 5, 0]
print(all(list6))  # # Will Return false as one value is false (Value 0).
print(any(list6)) # # Will Return True as we have items in the list with True value.

# List Comprehensions
# List Comprehensions provide an elegant way to create new lists.
# It consists of brackets containing an expression followed by a for clause, then zero or more for
# or if clauses.
mystring = "WELCOME"
mylist = [i for i in mystring ] # Iterating through a string Using List Comprehe
print(mylist)


# Tuples......
# 1. Tuple is similar to List except that the objects in tuple are immutable which means we cannot
# change the elements of a tuple once assigned.
# 2. When we do not want to change the data over time, tuple is a preferred data type.
# 3. Iterating over the elements of a tuple is faster compared to iterating over a list

# Tuple Creation
tup1 = () # Empty tuple

# Same as list
# But
# # Tuples are immutable which means we can't DELETE tuple items.
# # Tuples are immutable which means we can't CHANGE tuple items.


# Sets......

# 1) Unordered & Unindexed collection of items.
# 2) Set elements are unique. Duplicate elements are not allowed.
# 3) Set elements are immutable (cannot be changed).
# 4) Set itself is mutable. We can add or remove items from it.

# Set Creation..
# myset = {1,2,3,4,5} # Set of numbers.
#myset3 = {10,20, "Hola", [11, 22, 32]} # set doesn't allow mutable items like list in set elements.

myset4 = set() # Create an empty set
myset = {'eight', 'five', 'four', 'one', 'seven', 'six', 'three', 'two'}

print(myset)
myset.add('nine')
print(myset)
'''
add more 


'''

# Dictionary ................
# Dictionary is a mutable data type in Python.
# A python dictionary is a collection of key and value pairs separated by a colon (:) & enclosed in curly braces {}.
# Keys must be unique in a dictionary, duplicate values are allowed..

# Create Dictionary...
mydict = dict() # Empty dictionary.

print(mydict)

mydict = {} # Empty dictionary.

mydict = {1: 'one', 2: 'two', 3: 'three'} # dictionary with integer keys.

print(mydict)

mydict = dict({1: 'one', 2: 'two', 3: 'three'}) # # Create dictionary using dict()

mydict1 = {'A':'one' , 'B':'two' , 'C':'three'} # dictionary with character keys
mydict2 = {1:'one' , 'A':'two' , 3:'three'} # dictionary with mixed keys

print(mydict2.keys())  # # Return Dictionary Keys using keys() method
print(mydict2.values()) # # Return Dictionary Values using values() method.
print(mydict2.items()) # # Access each key-value pair within a dictionary

keys = {'a' , 'b' , 'c' , 'd'}
value = 10
mydict3 = dict.fromkeys(keys, value)
print(mydict3)  # # Create a dictionary from a sequence of keys and value.


# Accessing Items
print(mydict[1])  # # Access item using key

print(mydict.get(1))  # # Access item using get() method

# Add, Remove & Change Items...
mydict[1] = 'ONE_N'  # # Changing Dictionary Items..
mydict[2] = 'TWO_N'

mydict['name'] = 'Kousik'  # # Adding items in the dictionary
print(mydict)

# mydict1.pop('Job') # Removing items in the dictionary using Pop method

# Copy Dictionary
# Same copy use in list..


# Loop through a Dictionary..
for i in mydict:
 print(i , ':' , mydict[i]) # Key & value pair


# Dictionary Membership

'name' in mydict # Test if a key is in a dictionary or not.
# Note : Membership test can be only done for keys.

# Dictionary Comprehension..
double = {i:i*2 for i in range(10)} #double each value using dict comprehension
print(double)


key = ['one' , 'two' , 'three' , 'four' , 'five']
value = [1,2,3,4]

mydict5 = { k:v for (k,v) in zip(key, value)}
print(mydict5)

# String process in dict..
str1 = "Natural Language Processing"
mydict6 = {k:v for (k, v) in enumerate(str1)}
print(mydict6)



# Operators
# Operators are special symbols in Python which are used to perform operations on
# variables/values.

'''
will add later


'''

# ================================================================================================================================

# Functions..........
# A function is a block of organized code written to carry out a specified task.
# Functions help break our program into smaller and modular chunks for better readability.
# Information can be passed into a function as arguments.
# Parameters are specified after the function name inside the parentheses.
# We can add as many parameters as we want. Parameters must be separated with a comma.
# A function may or may not return data.
# In Python a function is defined using the def keyword

# Parameter VS Argument..
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.


def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b
a = 10
b = 20
print(swap(a, b))

def fact(num):     # 5! = 5 *4!
    if num <= 1:
        return 1
    else:
        return num * fact(num -1)


print(fact(5))

#



def fibo(num):
    if num <= 1:
        return  num

    elif num == 2:
        return 1
    else:
        return fibo(num - 1) + fibo(num -2)
for i in range(5):
    print(fibo(i)) # 0 1 1 2 3


# ======================================================================================================================

# args & kwargs...
#  *args

# When we are not sure about the number of arguments being passed to a function then we can
# use *args as function parameter.
# *args allow us to pass the variable number of Non Keyword Arguments to function.
# We can simply use an asterisk * before the parameter name to pass variable length
# arguments.
# The arguments are always passed as a tuple.
# We can rename it to anything as long as it is preceded by a single asterisk (*). It's best
# practice to keep naming it args to make it immediately recognizable.


# **kwargs.....
# **kwargs allows us to pass the variable number of Keyword Arguments to the function.
# We can simply use an double asterisk ** before the parameter name to pass variable length
# arguments.
# The arguments are passed as a dictionary.
# We can rename it to anything as long as it is preceded by a double asterisk (**). It's best
# practice to keep naming it kwargs to make it immediately recognizable.


def add(a, b, c):
    return a + b + c

print(add(10, 20, 30))

def add1(*args):
    return sum(args)

print(add1(1, 2, 3, 4))
print(add1(1,2,3,4))            # *args will take dynamic argument list. So add() function w
print(add1(1,2,3,4,5))
print(add1(1,2,3,4,5,6))
print(add1(1,2,3,4,5,6,7))


def UserDetails(*args):
    print(args)
UserDetails('Asif' , 7412 , 41102 , 33 , 'India' , 'Hindi')

''' For the above example we have no idea about the parameters passed e.g 7412 , 
 In such cases we can take help of Keyworded arguments (**kwargs) '''

def UserDetails(**kwargs):
    print(kwargs)
UserDetails(Name='Asif' , ID=7412 , Pincode=41102 , Age= 33 , Country= 'India' , Language= 'Hindi')


def UserDetails(**kwargs):
    for key,val in kwargs.items():
        print("{} :- {}".format(key,val))
UserDetails(Name='Asif' , ID=7412 , Pincode=41102 , Age= 33 , Country= 'India', Language= 'Hindi')


mydict = {'Name': 'Asif', 'ID': 7412, 'Pincode': 41102, 'Age': 33, 'Country': 'India', 'Language': 'Hindi'}
UserDetails(**mydict)


def UserDetails(licenseNo, *args, phoneNo=0, **kwargs):  # Using all four argument
                                                        # Note: *args MUST come before **kwargs in the argument list
    print('License No :- ', licenseNo)
    j = ''
    for i in args:
        j = j + i
    print('Full Name :-', j)
    print('Phone Number:- ', phoneNo)
    for key, val in kwargs.items():
        print("{} :- {}".format(key, val))


name = ['Asif', ' ', 'Ali', ' ', 'Bhat']
mydict = {'Name': 'Asif', 'ID': 7412, 'Pincode': 41102, 'Age': 33, 'Country': 'India', 'Language': 'Hindi'}
UserDetails('BHT145', *name, phoneNo=1234567890, **mydict)

# ======================================================================================================================

# Lambda, Filter, Map and Reduce

# Lambda
# A lambda function is an anonymous function (function without a name).
# Lambda functions can have any number of arguments but only one expression. The
# expression is evaluated and returned.
# We use lambda functions when we require a nameless function for a short period of time.

addition = lambda a: a + 10  # # This lambda function adds value 10 to an argument
print(addition(5))

product = lambda  a , b: a * b # #This lambda function takes two arguments (a,b)
print(product(3, 4))

res = (lambda *args: sum(args))  ## This lambda function can take any number of arguments.
print(res(1, 2, 4, 5, 6,7))


# Filter..
#  It is used to filter the iterables/sequence as per the conditions.
#  Filter function filters the original iterable and passes the items that returns True for the function provided to filter
#  It is normally used with Lambda functions to filter list, tuple, or sets.

# filter() method takes two parameters:
    # function - function tests if elements of an iterable returns true or false
    # iterable - Sequence which needs to be filtered, could be sets, lists, tuples, or any iterators

list1 = [1,2,3,4,5,6,7,8,9]
odd_num = list(filter(lambda x: x%2!=0, list1))
print(odd_num)


# map ...
#  The map() function applies a given function to each item of an iterable (list, tuple etc.) and
# returns a list of the results.
# map() function takes two Parameters :
# function : The function to execute for each item of given iterable.
# iterable : It is a iterable which is to be mapped.
# Returns : Returns a list of the results after applying the given function to each item of a given
# iterable (list, tuple etc.)

add_num= list(map(lambda x : x+1, list1))
print(add_num)

from functools import reduce

sum = reduce(lambda a, b: a + b, list1)
print(sum)


# ======================================================================================================================
# Classes & Objects....
# A Class is an object constructor or a "blueprint" for creating objects.
# Objects are nothing but an encapsulation of variables and functions into a single entity.
# Objects get their variables and functions from classes.
# To create a class we use the keyword class


# The first string inside the class is called docstring which gives the brief description about the class.

# All classes have a function called __init__() which is always executed when the class is being initiated.
# We can use  __init__() function to assign values to object properties or other operations
# that are necessary to perform when the object is being created.


# The self parameter is a reference to the current instance of the class and
#   is used to access  class variables.
#   self must be the first parameter of any function in the class.


# The super() builtin function returns a temporary object of the superclass that allows us to
# access methods of the base class
# super() allows us to avoid using the base class name explicitly and to enable multiple inheritance.

# ----------------------------------------------------------------------------------------------------------------------

# Create a class with property "var1"
class myclass:
    var1 = 10

obj = myclass()  # # Create an object of class "myclass()"
print(obj.var1)


# Create a "Employee" class

class Employee():
    def __init__(self, name, empid):  # __init__() function is used to assign values
        self.name = name
        self.empid = empid
    def greet(self): # Define a Class method
        print("Thanks for coming here {}".format(self.name))


empobj = Employee('Kousik', '123')

print(empobj.name)
print(empobj.empid)
empobj.greet()


# # Modify Object Properties

empobj.empid = '1234567'
print(empobj.empid)

# # Create an another employee object 'empobj2'..

empobj2 = Employee('Akash', 98765)
print(empobj2.name)
print(empobj2.empid)
empobj2.greet()

empobj2.country = 'India'
print(empobj2.country)  # Instance variable can be created manually.



# Inheritance..
# Inheritance is a powerful feature in object oriented programming.

#  Inheritance provides code reusability in the program because we can use an existing class
#   (Super Class/ Parent Class / Base Class) to create a new class (Sub Class / Child Class /
#   Derived Class) instead of creating it from scratch.

# The child class inherits data definitions and methods from the parent class which facilitates the
#   reuse of features already available. The child class can add few more definitions or redefine a  base class method.

# Inheritance comes into picture when a new class possesses the 'IS A' relationship with an
# existing class. E.g Student is a person. Hence person is the base class and student is derived class.

# Person ---> Student, Teacher
class person():   # Parent Class
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def PersonInfo(self):
        print('Person name {}'.format(self.name))
        print('Person age {}'.format(self.age))
        print('Person Gender {}'.format(self.gender))


class student(person):    # Child Class

    def __init__(self, name, age, gender, studentid, fees):
        person.__init__(self, name, age, gender)
        self.studentid = studentid
        self.fees = fees

    def StudentInfo(self):
        print('Student ID :- {}'.format(self.studentid))
        print('Fees :- {}'.format(self.fees))


class teacher(person):  # Child Class
    def __init__(self, name, age, gender, empid, salary):
        person.__init__(self, name, age, gender)
        self.empid = empid
        self.salary = salary

    def TeacherInfo(self):
        print('Employee ID :- {}'.format(self.empid))
        print('Salary :- {}'.format(self.salary))


stud1 = student('Asif' , 24 , 'Male' , 123 , 1200)
print('Student Details')
print('---------------')
stud1.PersonInfo() # PersonInfo() method presnt in Parent Class will be access
stud1.StudentInfo()
print()


teacher1 = teacher('Basit' , 36 , 'Male' , 456 , 80000)
print('Teacher Details')
print('---------------')
teacher1.PersonInfo() # PersonInfo() method presnt in Parent Class will be acc
teacher1.TeacherInfo()


# # super() builtin function allows us to access methods of the base class.

class person: # Parent Class
    def __init__(self, name , age , gender):
        self.name = name
        self.age = age
        self.gender = gender

    def PersonInfo(self):
        print('Name :- {}'.format(self.name))
        print('Age :- {}'.format(self.age))
        print('Gender :- {}'.format(self.gender))

class student(person): # Child Class
    def __init__(self,name,age,gender,studentid,fees):
        super().__init__(name,age,gender)
        self.studentid = studentid
        self.fees = fees

    def StudentInfo(self):
        super().PersonInfo()
        print('Student ID :- {}'.format(self.studentid))
        print('Fees :- {}'.format(self.fees))

stud = student('Asif' , 24 , 'Male' , 123 , 1200)
print('Student Details')
print('---------------')
stud.StudentInfo()


# Multi-level Inheritance

# In this type of inheritance, a class can inherit from a child class or derived class.
# Multilevel Inheritance can be of any depth in python

class person: # Parent Class
    def __init__(self, name , age , gender):
        self.name = name
        self.age = age
        self.gender = gender

    def PersonInfo(self):
        print('Name :- {}'.format(self.name))
        print('Age :- {}'.format(self.age))
        print('Gender :- {}'.format(self.gender))

class employee(person): # Child Class
    def __init__(self,name,age,gender,empid,salary):
        person.__init__(self,name,age,gender)
        self.empid = empid
        self.salary = salary

    def employeeInfo(self):
        print('Employee ID :- {}'.format(self.empid))
        print('Salary :- {}'.format(self.salary))

class fulltime(employee): # Grand Child Class
    def __init__(self,name,age,gender,empid,salary,WorkExperience):
        employee.__init__(self,name,age,gender,empid,salary)
        self.WorkExperience = WorkExperience

    def FulltimeInfo(self):
        print('Work Experience :- {}'.format(self.WorkExperience))

class contractual(employee): # Grand Child Class
    def __init__(self,name,age,gender,empid,salary,ContractExpiry):
        employee.__init__(self,name,age,gender,empid,salary)
        self.ContractExpiry = ContractExpiry

    def ContractInfo(self):
        print('Contract Expiry :- {}'.format(self.ContractExpiry))

print('Contractual Employee Details')
print('****************************')

contract1 = contractual('Basit' , 36 , 'Male' , 456 , 80000,'21-12-2021')
contract1.PersonInfo()
contract1.employeeInfo()
contract1.ContractInfo()
print('\n \n')


print('Fulltime Employee Details')
print('****************************')
fulltim1= fulltime('Asif' , 22 , 'Male' , 567 , 70000, 12)
fulltim1.PersonInfo()
fulltim1.employeeInfo()
fulltim1.FulltimeInfo()


# Multiple Inheritance.......

# Multiple inheritance is a feature in which a class (derived class) can inherit attributes and
# methods from more than one parent class.
# The derived class inherits all the features of the base case


# Super Class
class Father:
    def __init__(self):
        self.fathername = str()


# Super Class
class Mother:
    def __init__(self):
        self.mothername = str()


# Sub Class
class Son(Father, Mother):
    name = str()
    def show(self):
        print('My Name :- ',self.name)
        print("Father :", self.fathername)
        print("Mother :", self.mothername)

s1 = Son()
s1.name = 'Bill'
s1.fathername = "John"
s1.mothername = "Kristen"
s1.show()


# Method Overriding..........
# Overriding is a very important part of object oreinted programming because it makes
# inheritance exploit its full power.

# Overriding is the ability of a class (Sub Class / Child Class / Derived Class) to change the
# implementation of a method provided by one of its parent classes.

# When a method in a subclass has the same name, same parameter and same return type as
# a method in its super-class, then the method in the subclass is said to override the method in
# the super-class.

# The version of a method that is executed will be determined by the object that is used to
# invoke it.
# If an object of a parent class is used to invoke the method, then the version in the parent class
# will be executed, but if an object of the subclass is used to invoke the method, then the
# version in the child class will be executed.

# ==================================================================================================================

# Encapsulation:
# Definition: The bundling of data and methods that operate on the data into a single unit,
# with controlled access to the internal state.
# Purpose: To protect an object’s internal state and expose a controlled interface.
# Implementation: Achieved through private and protected members.

# What are Private and Protected Members in Python Classes?
# Private Members: Members with double underscores (__) are private. They are intended to be accessed only
# within the class where they are defined.
# Python uses name mangling to make these members harder to access from outside the class.


# Protected Members: Members with a single underscore (_) are protected. They are intended
# for use within the class and its subclasses. This is a convention and does not enforce strict access control.



# Abstraction:
# Definition: The concept of hiding complex implementation details and showing only the essential
# features of an object.
# Purpose: To simplify interaction with objects by focusing on high-level operations rather than
# implementation details.
# Implementation: Achieved through abstract classes and methods, interfaces, and high-level class design.


# ======================================================================================================================

#  Iterable & Iterator.......
# An iterable is an object that can be iterated upon. It can return an iterator object with the
# purpose of traversing through all the elements of an iterable.

# An iterable object implements __iter()__ which is expected to return an iterator object. The
# iterator object uses the __next()__ method.
# Every time next() is called next element in the
# iterator stream is returned. When there are no more elements available StopIteration
# exception is encountered.
# So any object that has a __next()__ method is called an iterator.

mylist = ['Asif' , 'Basit' , 'John' , 'Michael']

list_iter = iter(mylist)  # # Create an iterator object using iter()

print(next(list_iter)) # # return first element in the iterator stream
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
#print(next(list_iter)) # Exception Error StopIteration bcz No more value

#print(list_iter.__next__())

# ======================================================================================================================

# Generator......
# Python generators are easy way of creating iterators. It generates values one at a time from a
# given sequence instead of returning the entire sequence at once.

# It is a special type of function which returns an iterator object.
# In a generator function, a yield statement is used rather than a return statement
# The generator function cannot include the return keyword. If we include it then it will terminate
# the execution of the function.


# Different Between Yield and Return ...

# The difference between yield and return is that once yield returns a value the function is
# paused and the control is transferred to the caller
# Local variables and their states are remembered between successive calls.

# In case of the return statement value is returned and
# the execution of the function is terminated.

# Methods like iter() and next() are implemented automatically in generator function.
# Simple generators can be easily created using generator expressions. Generator
# expressions create anonymous generator functions like lambda.


# The syntax for generator expression is similar to that of a list comprehension ....
# but the only
# difference is square brackets are replaced with round parentheses.
# Also list comprehension
# produces the entire list while the generator expression produces one item at a time which is
# more memory efficient than list comprehension.

# # Simple generator function that will generate natural numbers from 1 to 20.

def mygen():
    for i in range(1, 20):
        yield i

mygen1 = mygen()

for i in mygen1:
    print(i)

# # Store all values generated by generator function in a list
num_gen = list(mygen())
print(num_gen)

list2 = [i**2 for i in range(10)] # List comprehension
gen2 = (i**2 for i in range(10)) # Generator expression
#=======================================================================================================================
# # Decorator......
# When we need to change the behavior of a function without modifying the function itself..
#

# # Decorator is very powerful and useful tool in Python as it allows us to wrap another function
# # in order to extend the behavior of wrapped function without permanently modifying it.


# 1 Treating a function as objects...
def fun(msg):

    print(msg)

msg = fun    # # asssing fun name in a variable or object. Not calling the fun

print(fun('Decorator...............'))

# 2.. Passing the function as argument

def upper(text):
    return text.upper()
def mainfun(func):

    main = func('I am Kouisk Das calling from main function')
    print(main)

mainfun(upper)

# the mainfun function take another function as a parameter(upper). the upper function passed as an argument .
# then upper function called inside the mainfun.

# Returning function from another function.
#
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_15 = create_adder(15)
print(add_15(10))


def hello_decorator(func):
    def inner():
        print('Hello, this is before function execution..')

        func()

        print('This is after function execution')
    return inner

def function_to_be_used():
    print('This is inside function........')

function_to_be_used_val = hello_decorator(function_to_be_used)

function_to_be_used_val()




# ----------------------------------------------------------------------------------------------------------------------
# File Management.............................
# Python has several built-in modules and functions for creating,
# reading, updating and deleting files.
# Order of File operation......
# Open File -----> Read/Write File ---->Close File.

# Open File.......
# fileobj = open('test1.txt') # Open file in read/text mode
# fileobj = open('test1.txt', 'r') # Open file in read mode
# fileobj = open('test1.txt', 'w') # Open file in write mode
# fileobj = open('test1.txt', 'a') # Open file in append mode

# Read File.............
# fileobj.read() #Read whole file. #File cursor is already at the end of the file.

# fileobj.seek(0) # Bring file cursor to initial position.

# fileobj.seek(0)
# print(fileobj.readline()) # Read first line of a file.
# print(fileobj.readline()) # Read second line of a file.
# print(fileobj.readline()) # Read third line of a file.


# fileobj.readlines() # Read all lines of a file.


# # Read first 5 lines of a file using readline()
# fileobj.seek(0)
# count = 0
# for i in range(5):
#  if (count < 5):
#  print(fileobj.readline())
#  else:
#  break
#  count+=1


# Recomendentions this usecase.....use.fileobj.readlines()

# # Read first 5 lines of a file using readlines()
# fileobj.seek(0)
# count = 0
# for i in fileobj.readlines():
#  if (count < 5):
#  print(i)
#  else:
#  break
#  count+=1

# Write File...............................

# fileobj.write("First Line\n")

# Close File......................
# fileobj.close()

# Delete file..................
# os.remove("test3.txt") # Delete file


#=======================================================================================================================

#Error & Exception Handling..................................
# Python has many built-in exceptions (ArithmeticError, ZeroDivisionError, EOFError, IndexError,
# KeyError, SyntaxError, IndentationError, FileNotFoundError etc) that are raised when your
# program encounters an error.

# When the exception occurs Python interpreter stops the current process and passes it to the
# calling process until it is handled. If exception is not handled the program will crash.

# Exceptions in python can be handled using a try statement.
# The try block lets you test a block of code for errors.

# The block of code which can raise an exception is placed inside the try clause. The code that
# will handle the exceptions is written in the except clause.

# The finally code block will execute regardless of the result of the try and except blocks./

# We can also use the else keyword to define a block of code to be executed if no exceptions
# were raised.

# Python also allows us to create our own exceptions that can be raised from the program using
# the raise keyword and caught using the except clause. We can define what kind of error to
# raise, and the text to print to the user.

# A try statement can have more than one except clause.................
# It possible to use try block without except block but we need finally block for this.
# we our raise exception.
try:
    print(100)   # # ZeroDivisionError will be encountered here.

except:
    print(sys.exc_info()[1], 'Exception occured')  # # This statement will be executed if exceptions is occured.

else:
    print('No exception occurred')  # This will be skipped as code block inside if exception occured

finally:
    print('Run this block of code always')  # This will be always executed
