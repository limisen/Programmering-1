#Input för Ord.Pris vilket sedan intergeras för att kunna användas
ordPris = input("Ange ordinarie pris: ")
ordPris = float(ordPris)

#uträkning av extrapriset
extrapris = ordPris * 0.85
int(extrapris)

#utskrift på vad som ska betalas 
print("Pris med rabatt: {:1.2f}kr".format(extrapris))