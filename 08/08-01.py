amount = int(input("Ange tal du vill mata in: "))

tal = []
for i in range(1,amount+1):
    tal.append(float(input("Ange tal " + str(i) + ": ")))

for x in tal:
    print("{0:>0.2f}".format(x), end=", ")