from random import randrange

def tärnings_kast():

    """ Slumpar fram tärnings kast för att sedan skriva ut en frekvenstabell för de olika utfallen """
    resultat = ['dummy', 'dummy', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    kast_för_tärning1 = [] 
    kast_för_tärning2 = []

    for i in range(10):
        kast_för_tärning1.append(randrange(2,12))
        kast_för_tärning2.append(randrange(2,12))
        resultat.insert(((kast_för_tärning1[i]+ kast_för_tärning2[i]), ))
        print(resultat, kast_för_tärning1, kast_för_tärning2)

print(tärnings_kast())