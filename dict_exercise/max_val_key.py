# The original dictionary is : {'gfg': {'Manjeet': 5, 'Himani': 10},
# 'is': {'Manjeet': 8, 'Himani': 9}, 'best': {'Manjeet': 10, 'Himani': 15}}
# The required key is : best

test_dict = {'gfg': {'Manjeet': 5, 'Himani': 10},
'is': {'Manjeet': 8, 'Himani': 9}, 'best': {'Manjeet': 10, 'Himani': 15}}

for key, value in test_dict.items():
    print(value)
    for nk, nv in value.items():
        print(nv)

