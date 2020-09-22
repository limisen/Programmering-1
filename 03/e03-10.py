Tempfahren = input("Temperatur i Fahrenheit?\n")
Tempfahren = float(Tempfahren)

#Omvandling från F -> C   Fahrenheit -32 sedan multiplicera med 5 och sist dela med 9
Tempcelcius = (((Tempfahren -32) * 5) /9)

print("{0} Fahrenheit motsvarar {1} Celcius".format(Tempfahren, Tempcelcius))