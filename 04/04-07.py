X = float(input("Vänligen ange din ålder: "))
if X < 18:
    print("Tyvär kan vi inte bevilja fakturabetalning")
    exit()

Y = float(input("Vad är din brutto inkomst? "))
if Y < 120000:
    print("Tyvär kan vi inte bevilja fakturabetalning")
    exit()

Z = (input("Har du några kredit-anmärkningar?(ja eller nej) "))
if Z == "ja":
    print("Tyvär kan vi inte bevilja fakturabetalning")
    exit()
elif Z != "ja" and Z != "nej":
    Z = (input("Svara snälla med ja eller nej, tack!\n Har du några kredit-anmärkningar? " ))
    next
else:
    print("Fakturabetalning beviljad")