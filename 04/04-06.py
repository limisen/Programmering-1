X = float(input("Vänligen ange din ålder: "))
Y = float(input("Vad är din brutto inkomst? "))
Z = (input("Har du några kredit-anmärkningar?(ja eller nej) "))

if Z != "ja" and Z != "nej":
    Z = (input("Svara snälla med ja eller nej, tack!\n Har du några kredit-anmärkningar? " ))
    pass

if X >= 18 and Y >= 120000 and Z == "nej":
    print("Fakturabetalning beviljad")
else:
    print("Tyvär kan vi inte bevilja fakturabetalning")