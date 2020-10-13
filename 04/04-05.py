X = int(input("Ge mig ett årtal: "))

print(X%4)

print(X%400)

if X%4 == 0:
    print("Det är ett skotår")
elif X%4 == 1:
    print("inte ett skotår")