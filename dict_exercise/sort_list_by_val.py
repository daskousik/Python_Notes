# Ways to sort list of dictionaries by values in Python – Using itemgetter.......
data_list = [{"name": "Nandini", "age": 20},
             {"name": "Manjeet", "age": 20},
             {"name": "Nikhil", "age": 19}]



for i in data_list:
    print(i)

# Python code to demonstrate the working of sorted()
# and itemgetter
# Ways to sort list of dictionaries by values in Python – Using itemgetter.............
from operator import  itemgetter

print(sorted(data_list, key= itemgetter("age")))

# ----------------------------------------------------------------------------------------------------------------------
# Ways to sort list of dictionaries by values in Python – Using lambda function...........
print(sorted(data_list, key=lambda x: x['age']))
