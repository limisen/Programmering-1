x = int(input("Ge mig ett heltal:"))

if x <= 0 or x > 12:
    print("{0} Är ogiltigt".format(x))
else:
    print("{0} Är giltigt".format(x))