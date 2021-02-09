def nettopris(x):
    """Beroende på inmatat värde, räknar ut och returnerar rabatterat pris (<500 ingen rabat, 500<x<=1000 2% rabatt, 1000< 5% rabatt)
    """
    if x >= 500 and x <= 1000:
        x * 0.98
        return(x)
    elif x >= 1000:
        x * .95
        return(x)
    elif x < 500:
        return(x)

bruttopris = 55.66
pris = nettopris(bruttopris)
print('Att betala: {0}kr'.format(pris))

bruttopris = 550.66
pris = nettopris(bruttopris)
print('Att betala: {0}kr'.format(pris))

bruttopris = 1550.66
pris = nettopris(bruttopris)
print('Att betala: {0}kr'.format(pris))
#klar!