Nr = int(input("Ange start värde: "))
Nr2 = int(input("Ange stop värde: "))

if Nr > Nr2:
    for i in range(Nr, Nr2-1, -1):
        print(i, end=" ")
elif Nr2 > Nr:
    print("Ange ett sjunkande värde, snälla!")