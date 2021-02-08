num = int(input("Ange månadens nummer (1-12): "))

Monts = ["Months", "Januari", "Februari", "Mars", "April", "Maj", "Juni", "Juli", "Augusti", "eptember", "Oktober", "November", "December"]

if num < 1 or num > 12: 
    print("Felaktigt heltal angivet")
else:
    print(Monts[num])

#Klar!