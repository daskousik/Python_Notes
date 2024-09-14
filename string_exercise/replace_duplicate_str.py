
test_str = 'Gfg is best also . Gfg also has Classes now. \
                Classes help understand better . '

repl_dict = {'Gfg' : 'It', 'Classes' : 'They' }

str_split = test_str.split()
print(str_split)
res = ''

for word in str_split:

    if word in repl_dict and word in res:
        res = res + ' ' + repl_dict[word]

    else:
        res = res + ' '+ word

print(res)

