# Python – Mirror Image of String...........................
# Given a String, perform its mirror imaging, return “Not Possible” if mirror image not possible using english characters.
# nput : test_str = ‘boid’ Output : doib Explanation : d replaced by b and vice-versa as being mirror images.
# Input : test_str = ‘gfg’ Output : Not Possible Explanation : Valid Mirror image not possible.

test_str = 'boid'
print(list(test_str)) # ['b', 'o', 'i', 'd']

print('Input string -->  '   + str(test_str))

mir_dict = {'b':'d', 'd':'b', 'i':'i', 'o':'o', 'v':'v', 'w':'w', 'x':'x'}
res =''
for ch in test_str:
    if ch in mir_dict:
        res = res + mir_dict[ch]
    else:
        print('Mirror Not Possible')
        break
print(res)


