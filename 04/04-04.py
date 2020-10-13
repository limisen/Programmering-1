bensinPris = float(input("Vad är bensin priserna idag (i kr/liter)? "))

if bensinPris < 0:
    print("NEGATIVT pris!")
elif bensinPris <= 10:
    print("Det var billigt!")
elif (10<bensinPris<15):
    print("Tanka full tank")
elif (15<=bensinPris<20):
    print("Tanka tio liter")
elif bensinPris >= 20:
    print("Nu säljer jag bilen och cyklar i stället")
