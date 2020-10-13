X = float(input("Ge mig ett tall för ditt första prov: "))

Y = float(input("Ge mig ett tall för ditt andra prov: "))

Z = float(input("Ge mig ett tall för ditt tredje prov: "))

medlvärde = (X + Y + Z)/3
#print(medlvärde)

print("Poäng prov 1: {0}".format(X))
print("Poäng prov 2: {0}".format(Y))
print("Poäng prov 3: {0}".format(Z))

if medlvärde >= 90: 
    print("90 Bra jobbat!")