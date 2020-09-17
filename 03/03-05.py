#Angivning av pris och tank
bensin= input("Ange tankad volym: ")
float(bensin)

prisL = input("ange priset/liter: ")
float(prisL)

#Uträkning
bensin = float(bensin)
prisL = float(prisL)
betala = (bensin * prisL)
bensin = round(bensin)
prisL = round (prisL, 2)
betala = round (betala, 2) 


#KVITTOT!
print("+--------------------------------------+")
print("|    {:^}                            |".format("TANKAT"))
print("|    {:<} {:12.2f} {:<}   |".format("Tankad volym", bensin, "liter"))
print("|    {:<} {:12.2f} {:<}    |".format("Pris per liter", prisL, "kr"))
print("|    {:<} {:12.2f} {:<}     |".format("Betalt kronor", betala, "kr"))
print("|    {:<}                                  |".format(""))
print("|    {:<}              |".format("Tack för besöket och"))
print("|    {:<}                   |".format("välkommen åter!"))
print("+--------------------------------------+")