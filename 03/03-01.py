#Anger tal1 och integer talet så att det kan anvöndas
tal1 = input("Ange tal#1: ")
tal1 = int(tal1)

tal2 = input("Ange tal#2: ")
tal2 = int(tal2)

#Variabel för summa och produkt så jag enkelt kan printa
prod = tal1 * tal2
summa = tal1 + tal2

#Utskrift
print(" ")
print("Tal#1: {0}".format(tal1))
print("Tal#2: {0}".format(tal2))
print(" ")
print("Summa = {0}".format(summa))
print("Produkten = {0}".format(prod))