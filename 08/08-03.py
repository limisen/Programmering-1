amount = int(input("Ange tal du vill mata in: "))

tal = []
for i in range(1,amount+1):
    tal.append(int(input("Ange tal " + str(i) + ": ")))

for i in range(1, len(tal)):
    y = tal[i] + tal[i-1]
    print(y)

#Inte klar!