#Angivning av pris och tank
volym = input("Ange tankad volym: ")
volym = float(volym)

prisLiter = input("ange priset/liter: ")
prisLiter = float(prisLiter)

#Uträkning

betala = (volym * prisLiter)
volym = round(volym)
prisLiter = round(prisLiter, 2)
betala = round(betala, 2)

#KVITTOT!
print("+---------------------------------+")
print("|   {:^}                        |".format("TANKAT"))
print("|   {:<} {:>10.2f}{:<}  |".format("Tankad volym", volym,"liter"))
print("|   {:<} {:>10.2f}{:<}   |".format("Pris per liter", prisLiter, "kr"))
print("|   {:<} {:>10.2f}{:<}    |".format("Betala kronor", betala, "kr"))
print("|                                 |")
print("|   {:<}          |".format("Tack för besöket och"))
print("|   {:<}               |".format("välkommen åter!"))
print("+---------------------------------+")
