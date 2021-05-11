start = int(input("Ange högsta temperaturen: "))
stop = int(input("Ange lägsta temperaturen: "))

for i in range(start, stop):
    print(32 + (i * (9/5)))