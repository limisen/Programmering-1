#kasta en tärning (T6) 10 gånger och skriv ut resultatet kommaseparerat.
import random

def dicethrower(x):
    """ Throws a D6 for a given amount of time and returns each throw, printed out continuasly """
    for i in range(0,x - 1):
        y = random.randint(1,6)
        print(y, end=", ")
    z = random.randint(1,6)
    print(z)

dicethrower(10)