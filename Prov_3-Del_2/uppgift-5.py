def rollDice(x, rollDice=1):
    """ doh """

    import random
    
    for i in random.randint(1, x):
        y = random.randint(1, 6)
        print("{0}", format(y), sep=", ")
        print("")

    try:
        print(rollDice())        # Ett tärningskast
        print(rollDice(0))       # Noll tärningskast
        print(rollDice(10))      # Tio tärningskast
        print(rollDice(4.2))     # Felaktig indata
        print(rollDice('test'))  # Felaktig indata
        help(rollDice())
    except ValueError:
        print("Errolf och Failbert hälsar på")


