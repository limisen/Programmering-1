stopp = int(input("Ange stopp: "))

for i in range(0, stopp+1):
    print(" {0:>3} {1:7} {2:7}".format(i, i**2, i**3))