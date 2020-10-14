X = int(input("Ge mig ett årtal: "))

if X == 1800:
    print("inte ett skottår")
elif X == 1900:
    print("inte ett skottår")
elif X == 2000:
    print("Det är ett skottår")
elif X == 2400:
    print("Det är ett skottår")
elif (X%4) == 0:
    print("Det är ett skottår")
else:
    print("inte ett skottår")
