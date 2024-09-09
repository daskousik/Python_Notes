# Python program to print even length words in a string..
# Input: s = "This is a python language"
# Output: This is python language
#
# Input: s = "i am laxmi"
# Output: am

s = "This is a python language"

for ele in s.split():
    if  len(ele) % 2 == 0:
        print(ele)


res = [ele for ele in s.split() if len(ele)%2 == 0]
print(res)
word_start = 0
for i, ch in enumerate(s):
    if ch == ' ':
        word_end = i
        word_lenght = word_end - word_start
        if word_lenght%2 == 0:
            print(s[word_start:word_end])

        word_start = i + 1


