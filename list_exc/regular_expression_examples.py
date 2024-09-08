import re

# 1. Matching a Valid Email Address
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

email = "example.user-123@example-domain.com"
# email = "user@example.com"

# r: raw of string
# ^: Asserts that match must start at the beginning of the string.
# [a-zA-Z0-9_.+-]+: Matches one or more characters that can be lower/Uppercase letters, digits,
# underscore(_),  dot(.), plus(+) or minus(-)

# @: Matches the literal @ symbol (required in email address)
# [a-zA-Z0-9-]+: matches one or more domain name characters that can be lower/Uppercase letters, digits, hyphens.
# \.: Escapes the dot(.) to match a literal dot .
# [a-zA-Z0-9-.]: Matches the domain extension, which can include letters, digits, dots, or hyphens (like .com or .co.in).
# $: Asserts that the match must occur at the end of the string.

if re.match(pattern, email):
    print('Valid Email')
else:
    print('Not a Valid Email')

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Example 2: Phone Number Validation (US)
pattern_phn = r'^\(\d{3}\)\s\d{3}-\d{4}$'
phone = "(123) 456-7890"
# ^: Asserts that the match must start at the beginning of the string.
# \(: Matches the literal opening parenthesis (.
# \d{3} :  Matches exactly three digits (area code).
# \) : Matches the literal closing parenthesis )
# \s :  Matches a whitespace character (space).
# \d{3} :  Matches exactly three digits (first part of the phone number).
# - :  Matches the literal dash -
# \d{4}:  Matches exactly four digits (last part of the phone number).
# $ : Asserts that the match must occur at the end of the string.
if re.match(pattern_phn, phone):
    print("Valid phone number")

# ------------------------------------------------------------------------------------------------------------
# 3. Matching a Date (YYYY-MM-DD format)
pattern_date = r'^\d{4}-\d{2}-d{2}$'
date = "2024-09-08"
# ^ – Asserts that the match must start at the beginning of the string.
# \d{4} – Matches exactly four digits (year).
# - – Matches the literal dash -.
# \d{2} – Matches exactly two digits (month).
# - – Matches the literal dash -.
# \d{2} – Matches exactly two digits (day).
# $ – Asserts that the match must occur at the end of the string.
if re.match(pattern_date, date):
    print("Valid date format")

# --------------------------------------------------------------------------------------------------------------------------
# 4. Matching a URL Example 4: Extracting URLs from Text
# ^https?:\/\/(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(\/[a-zA-Z0-9#]+\/?)*$

pattern_url = r'https?://(?:www\.)?[a-zA-Z0-9./_-]+'

# url = "https://www.example.com/path1/path2"
text = "Visit our website at https://www.example.com or http://example.org for more info."

# https? – Matches either http or https (the ? makes the s optional).
# :// – Matches the literal ://.
# (?:www\.)? – Matches www. if present. the ? makes it optional.
    # and the (?:...) is a non-capturing group (does not store the match).
# [a-zA-Z0-9./_-]+ – Matches one or more characters that can be letters, digits, periods, slashes, underscores, or hyphens. This represents the domain and path of the URL.

