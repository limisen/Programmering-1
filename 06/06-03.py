firstname = input("Vad heter du i förnamn? ")
firstname = firstname.strip()

lastname = input("Vad heter du i efternamn? ")
lastname = lastname.strip()

fullname = firstname + " " + lastname

print("Fullständigt namn = {0}".format(fullname))