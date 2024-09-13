# Python Program to Accept the Strings Which Contains all Vowels
# Given a string, the task is to check if every vowel is present or not.
# We consider a vowel to be present if it is present in upper case or lower case.
# i.e. ‘a’, ‘e’, ‘i’.’o’, ‘u’ or ‘A’, ‘E’, ‘I’, ‘O’, ‘U’ .
# Input : geeksfOrgeeks
# Output : Not Accepted
# All vowels except 'a','i','u' are not present
# ABeeIghiObhkUul
# Output : Accepted
# All vowels are present

s = 'ABeeIghiObhkUul'
vowel = 'aeiou'


accept = ''
res = []
for ch in s.lower():
    if ch in (vowel):
        #print(ch)
        if ch not in accept:
            accept = accept + ch
if len(vowel) == len(accept):
    print('Accepted all vowel in present')
else:
    for ch in vowel:
        if ch not in accept:
            res.append(ch)

    print('Not Accepted')
    print(f'All vowels except  are not present', str(res) )






