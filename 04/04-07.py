X = float(input("Vänligen ange din ålder: "))
if X <= 18:
    print("Tyvär kan vi inte bevilja fakturabetalning")
    exit()

Y = float(input("Vad är din brutto inkomst i tusental kronor? "))
if Y < 120:
    print("Tyvär kan vi inte bevilja fakturabetalning")
    exit()

Z = (input("Har du några betalnings-anmärkningar (J/N)? "))
if Z == "J":
    print("Tyvär kan vi inte bevilja fakturabetalning ")
    exit()
elif Z != "J" and Z != "N":
    Z = (input("Svara snälla med J eller N, tack!\n Har du några betalnings-anmärkningar? "))
    next
else:
    print("Fakturabetalning beviljad")