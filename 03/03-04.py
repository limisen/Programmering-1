ordPris = input("Ange ordinarie pris: ")
rabatt = input("Ange rabatten i %: ")

ordPris = int(ordPris)
rabatt = float(rabatt)

rabatt = (100 - rabatt)
rabatt2 = (rabatt * 0.01)
extrapris = (ordPris * rabatt2)

int(extrapris)

print("Pris med rabatt: {}kr".format(extrapris))