# The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']

str_lst = ['Gfg', 'is', 'best', 'for', 'Geeks']

# Here we need to character swaps .. G to e and e G
# So we are going to use loop + list comprehension . bcz in single line we can get list of changes ele and loop

res = [sub.replace('G', '-').replace('e', 'G').replace('-', 'e') for sub in str_lst]

print('Swap character using list comp  ',res)
# --------------------------------------------------------------------------------------------------------------------------
# form list join each elements . bcz join has itterator also
res2 = ', '.join(str_lst)

res2 = res2.replace('G', '-').replace('e', 'G').replace('-', 'e').split(', ')
print('Using join and split', res2)
# --------------------------------------------------------------------------------------------------------------------------

