first_name = input("Skriv in ditt förnamn: ")
first_name = first_name.strip()
last_namne = input("Skriv in ditt efternamn: ")
last_namne = last_namne.strip()

full_name = last_namne + " " + first_name

print(full_name[::-1])