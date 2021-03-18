from random import shuffle, choice 

def lottodragning():
    """Skapar en slumpad och sorterad lista / (lotto-rad)"""
    lot = [i for i in range(1,36)]
    
    shuffle(lot)
    
    dragning = []
    
    for i in range(7):  
        nr = choice(lot)
        dragning.append(nr)
        lot.remove(nr)
        shuffle(lot)
    dragning = sorted(dragning)

    return dragning

print('Dragning 1:', lottodragning())
print('Dragning 2:', lottodragning())