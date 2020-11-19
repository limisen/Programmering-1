tal = int(input("Ange heltal (1-20): "))

print("Tal      Kvadrat     Kub")
for i in range(1, tal+1):
    print(" {0:>2} {1:>12} {2:>7}".format(i, i**2, i**3))
