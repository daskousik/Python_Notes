# Python – Extract words starting with K in String List
# nput : test_list = [“Gfg is good for learning”, “Gfg is for geeks”, “I love G4G”], K = l
# Output : [‘learning’, ‘love’]
# Explanation : All elements with L as starting letter are extracted.
#
# Input : test_list = [“Gfg is good for learning”, “Gfg is for geeks”, “I love G4G”], K = m
# Output : []
# Explanation : No words started from “m” hence no word extracted.

str_list = ['Gfg is good for learning', 'Gfg is for geeks', 'I love G4G']
k = 'l'
res = []
temp = []
res2 =[]
for ele in str_list:
    temp.extend(ele.split(' '))
    print(temp)
    ele = ele.split(' ')
    for item in temp:
        if item.startswith(k) or item.startswith(k.lower()) or item.startswith(k.upper()):
            res2.append(item)
    print('extracted word', res2)

    for ch in ele:

        if ch[0].lower() ==  k.lower():
            res.append(ch)


print('Extracted word from str list using loop ', res)

# -------------------------------------------------------------------------------
res2 = [ch for ele in str_list for ch in ele.split(' ') if ch[0].lower() ==  k.lower()]

print('Extracted word from str list using list Comprehension', res2)

# ---------------------------------------------------------------------------------------------------------
res3 = []
for ele in str_list:

    words = ele.split(' ')
    fil = list(filter(lambda x: x[0].lower() == k.lower(), words))
    res3.extend(fil)
print(res3)