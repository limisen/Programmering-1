pannkaka = {
    'vetemjöl': '2 1/2 dl',
    'salt': '1/2 tsk',
    'mjölk': '6 dl',
    'ägg': '3'
}

for values in pannkaka:
    print(values)
print("----------------")
for keys in pannkaka:
    print(keys)
print("----------------")
for keys, values in pannkaka.items():
    print(keys, values, sep=": ")
