from random import sample

def lottodragning():
    """Skapar en slumpad och sorterad lista / (lotto-rad)"""
    lot = sorted(sample(range(1,36), 7))
    return lot

print('Dragning 1:', lottodragning())
print('Dragning 2:', lottodragning())