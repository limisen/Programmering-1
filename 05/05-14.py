password = "Hej"
LÖSEN = input("Ange lösenord (Enter avbryter): ")

if LÖSEN == " " or LÖSEN == "":
    print("Inloggning avbruten")
elif LÖSEN != password:
    print("Felaktigt lösenord")
elif LÖSEN == password:
    print("Lösenord OK!")
