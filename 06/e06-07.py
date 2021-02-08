first_name = input("Skriv in ditt förnamn: ")
first_name = first_name.strip()
last_name = input("Skriv in ditt efternamn: ")
last_name = last_name.strip()

first_name_len = int(len(first_name))
last_name_len = int(len(last_name))

print(first_name[1, first_name_len], last_name[1, last_name_len])