#Input för Orenarie Pris vilket sedan integeras för att sedan kunna användas
ordPris = input("Ange ordinarie pris: ")
rabatt = input("Ange rabatten i %: ")

#omvandlar ordPris och rabatt så att de kan användas i uträkningarna nedan
ordPris = float(ordPris)
rabatt = float(rabatt)

#Uträkning
rabatt = (100 - rabatt)
rabatt2 = (rabatt * 0.01)
extrapris = (ordPris * rabatt2)

#Int:ar så att det kan användas i text strängen
float(extrapris)

print("Pris med rabatt: {}kr".format(extrapris))