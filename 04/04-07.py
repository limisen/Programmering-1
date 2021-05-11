q = 0
X = float(input("Vänligen ange din ålder: "))
while q != 1:
    if X <= 18:
        print("Tyvär kan vi inte bevilja fakturabetalning")
        pass
    Y = float(input("Vad är din brutto inkomst i tusental kronor? "))
    if Y < 120:
        print("Tyvär kan vi inte bevilja fakturabetalning")
        pass
    Z = (input("Har du några betalnings-anmärkningar (J/N)? "))
    if Z == "J":
        print("Tyvär kan vi inte bevilja fakturabetalning ")
        pass
    elif Z != "J" and Z != "N":
        while Z != "J" or Z != "N":
            Z = (input(
                "Svara snälla med J eller N, tack!\n Har du några betalnings-anmärkningar? "))
            if Z == "J":
                q += 1
                print("Tyvär kan vi inte bevilja fakturabetalning ")
                break
            elif Z == "N":
                q += 1
                print("Fakturabetalning beviljad")
                break
    elif Z == "N":
        q += 1
        print("Fakturabetalning beviljad")
#ÄNTLIGEN KLAR!