import re
# 1. re.search():
# Searches for the first occurrence of a pattern in a string.
pattern = r'\d+'  # This pattern looks for one or more digits
text = "There are 42 apples"
match = re.search(pattern, text)
if match:
    print("Found:", match.group())

# Output: Found: 42

# ---------------------------------------------------------------------------------------------------------
# re.findall():
# Finds all occurrences of a pattern in a string and returns them as a list.

pattern = r'\d+'  # This pattern looks for one or more digits
text = "There are 42 apples and 55 oranges"
matches = re.findall(pattern, text)
print(matches)
# Output: ['42', '55']

# --------------------------------------------------------------------------------------------------
# 3. re.match():
# Attempts to match a pattern starting from the beginning of the string

pattern = r'\d+'  # Looks for digits at the beginning of the string
text = "42 apples"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())

# Output: Match found: 42

# -------------------------------------------------------------------------------------------------------

# 4. re.sub():
# Replaces occurrences of a pattern with a replacement string.

pattern = r'apples'
replacement = 'bananas'
text = "I love apples and apples are great!"

result = re.sub(pattern, replacement, text)
print(result)

# Output: I love bananas and bananas are great!

# ----------------------------------------------------------------------------------------------------------

#  re.split():
# Splits a string based on a pattern.

pattern = r'\s+'  # Splits on one or more spaces
text = "Split this sentence into words"

result = re.split(pattern, text)
print(result)

# Output: ['Split', 'this', 'sentence', 'into', 'words']

# -----------------------------------------------------------------------------------------------------