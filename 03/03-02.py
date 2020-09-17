#Input för basen vilket sedan integeras för att sedan kunna användas
basen = input("Ange basen: ")
basen = float(basen)

#Samma som för basen fast denna gång för höjden
höjden = input("Ange höjden: ")
höjden = float(höjden)

#uträkning för arean följt med en print som skriver ut Arean
area = (höjden * basen /2)
print("Arean på triangeln är {0}".format(area))