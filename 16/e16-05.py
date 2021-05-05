produkter = {
    '3': 'Bragokex',
    '1': 'Blåbärskaka',
    '4': 'Ballerina',
    '2': 'Mariekex',
    '5': 'Singoalla',
}
produkter = sorted(produkter)

for keys, values in produkter.items():
    print(keys, values, sep=": ")