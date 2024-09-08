import re
# Basic Syntax and Patterns
# Special Characters in Regular Expressions:

#1 . (Dot): Matches any character except a newline.

if re.search(r'a.b', 'aacca#b'):
    print('Matchs')
else:
    print('Not Match')
#-------------------------------------------------------------------
#2 ^ (Caret): Matches the start of a string.
pattern = r'^Hello'
text = 'Hello World'
if re.search(pattern, text):
    print('Matchs')
else:
    print('Not Match')

# ---------------------------------------------------------------------
# $ (Dollar): Matches the end of a string.
patr = r'Hello$'
text = 'I am Kousik , Hello'
if re.search(patr, text):
    print('Matchs')
else:
    print('Not Match')
#----------------------------------------------------------------------------------
# \d: Matches any digit (equivalent to [0-9]).
re.search(r'\d+', 'Age: 21')  # Matches '21'
# ------------------------------------------------------------------------------

# \D: Matches any non-digit character.
re.search(r'\D+', 'Age: 21')  # Matches 'Age: '

# ------------------------------------------------------------------------------------------------------
# \w: Matches any word character (letters, digits, and underscore).
re.search(r'\w+', 'Hello_123')  # Matches 'Hello_123'
# ------------------------------------------------------------------------------------------------
# \W: Matches any non-word character (opposite of \w).
re.search(r'\W+', '!@#')  # Matches '!@#'

# --------------------------------------------------------------------------------------------------------
# \s: Matches any whitespace (spaces, tabs, line breaks).
re.search(r'\s+', 'Hello World')  # Matches the space

# ------------------------------------------------------------------------------------------------------
# \S: Matches any non-whitespace character.
re.search(r'\S+', '   Hello')  # Matches 'Hello'

#----------------------------------------------------------------------------------------------------
# Quantifiers:
# Quantifiers define how many instances of a pattern you want to match.
#
# * (Zero or more):

re.search(r'Go*gle', 'Gogle')  # Matches
re.search(r'Go*gle', 'Google')  # Matches
re.search(r'Go*gle', 'Ggggle')  # Matches

# -------------------------------------------------------------------------------------------------------
# + (One or more):
re.search(r'Go+gle', 'Google')  # Matches
re.search(r'Go+gle', 'Gogle')  # No match

# ----------------------------------------------------------------------------------------------------------
# ? (Zero or one):
re.search(r'colou?r', 'color')  # Matches
re.search(r'colou?r', 'colour')  # Matches

#------------------------------------------------------------------------------------------------------------

# {m} (Exactly m times):
re.search(r'\d{4}', '123456')  # Matches '1234'

# --------------------------------------------------------------------
# {m,n} (Between m and n times):
re.search(r'\d{2,4}', '12345')  # Matches '1234'

# -------------------------------------------------------------------------------------------------------------------
# Character Classes (Character Sets):
# [ ] (Character Set): Matches any single character inside the brackets.
re.search(r'[aeiou]', 'apple')  # Matches 'a'
re.search(r'[0-9]', '42')  # Matches '4'

# ----------------------------------------------------------------------------------------------------------------
# [^ ] (Negated Character Set): Matches any single character not inside the brackets.
re.search(r'[^aeiou]', 'apple')  # Matches 'p'

# ------------------------------------------------------------------------------------------------------------
# Ranges: You can define ranges inside square brackets.
re.search(r'[a-z]', 'apple')  # Matches 'a'
re.search(r'[A-Z]', 'Apple')  # Matches 'A'

# ---------------------------------------------------------------------------------------------------------------

# Parentheses (): Used to group expressions and capture matches.
match = re.search(r'(\d+)-(\d+)', 'Phone: 123-456')
print(match.group(1))  # '123'
print(match.group(2))  # '456'

# ------------------------------------------------------------------------------------------------------------
# Named Groups: Captures can be named for clarity.
match = re.search(r'(?P<area>\d+)-(?P<number>\d+)', 'Phone: 123-456')
print(match.group('area'))  # '123'
print(match.group('number'))  # '456'

# -----------------------------------------------------------------------------------------------
