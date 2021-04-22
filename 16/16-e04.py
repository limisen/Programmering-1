pannkaka = {
    'vetemjöl': '2 1/2 dl',
    'salt': '1/2 tsk',
    'mjölk': '6 dl',
    'banan': '1 st',
    'ägg': '3'
}

pannkaka.pop('banan')

for keys, values in pannkaka.items():
    print(keys, values, sep=" ")