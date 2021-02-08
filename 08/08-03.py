amount = int(input("Ange tal du vill mata in: "))

tal = []
for i in range(1,amount+1):
    tal.append(float(input("Ange tal " + str(i) + ": ")))

x = 1
x = int(x)

for x in tal:
    y = tal[x] + tal[x-1]
    print(y)

#Inte klar!