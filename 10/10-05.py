from random import _sqrt,random

def pi_calculator():
    """ Räknar ut pi genom att först slumpa fram 2 kordinater parvis för att sedan tafram sqrt av (x*x + y*y) och kolla om det är mindre än 1. Är det det så ökar within med 1. 
    Detta görs 10 miljoner gånger. """

    within = 0
    print("Calculating pi...")
    for i in range(1,10000000):
        x = random()
        y = random()
        if _sqrt(x*x + y*y) < 1:
            within +=1
        
        pi = 4 * within/i

    print("Pi är ungefär {0:.3f}".format(pi))

print(pi_calculator())
#klar!