#Input för Orenarie Pris vilket sedan integeras för att sedan kunna användas
ordPris = input("Ange ordinarie pris: ")
rabatt = input("Ange rabatten i %: ")

#omvandlar ordPris och rabatt så att de kan användas i uträkningarna nedan
ordPris = float(ordPris)
rabatt = float(rabatt)

#Uträkning
rabatt = float(100 - rabatt)
rabatt2 = float(rabatt * 0.01)
extrapris = float(ordPris * rabatt2)

#Int:ar så att det kan användas i text strängen
float(extrapris)

print("Pris med rabatt: {:1.2f}kr".format(extrapris))