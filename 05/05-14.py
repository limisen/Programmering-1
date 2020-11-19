password = "qwerty"
LÖSEN = input("Ange lösenord (Enter avbryter): ")

while LÖSEN != password:
    if LÖSEN == " " or LÖSEN == "":
        print("Inloggning avbruten")
        exit
    elif LÖSEN != password:
        print("Felaktigt lösenord")
        exit
    elif LÖSEN == password:
        print("Lösenord OK!")
        exit
    LÖSEN = input("Ange lösenord (Enter avbryter): ")
print("Lösenord OK!")
