x = ['kalle', 'Lina', 'Bo', 'Eje']
#Här ska du skapa ne funktion som slumpar fram och skriver ut en person från listan X

import random
def Slump_vald_person(x):
    """ Slumpar fram en variabel/person i angiven lista """
    y = print(random.choice(x))
    return(y)

Slump_vald_person(x)