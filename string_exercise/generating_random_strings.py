# Generating random strings until a given string is generated
# Given the string, the task is to generate the same string using the random combination of special character, numbers, and alphabets.
import string
import random
import time

# all possible characters including
# lowercase, uppercase and special symbols
possibleCharacters = string.ascii_lowercase + string.digits + \
                     string.ascii_uppercase + ' ., !?;:'

# string to be generated
t = "geek"

# To take input from user
# t = input(str("Enter your target text: "))

attemptThis = ''.join(random.choice(possibleCharacters)
                      for i in range(len(t)))

print(attemptThis)