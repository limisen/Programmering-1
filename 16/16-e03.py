pannkaka = {
    'vetemjöl'  : '2 1/2 dl',
    'salt'      : '1/2 tsk',
    'mjölk'     : '6 dl',
    'ägg'       : '3'
}

pannkaka.update({'vetemjöl' : '5 dl', 'salt' : '1 tsk', 'mjölk' : '12 dl', 'ägg' : '6 st'})

for keys, values in pannkaka.items():
    print(keys, values, sep=" ")