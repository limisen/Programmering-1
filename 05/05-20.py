rows = int(input("Ange antal rader: "))

q = 1

while q != rows+1:
    for i in range(1,10):
        print("{:>2}".format(i*q), end=" ")
    q += 1
    print()
