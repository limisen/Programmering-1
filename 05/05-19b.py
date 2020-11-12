rows = int(input("Ange antal rader: "))

for i in range(0,rows):
    for j in range(i):
        print("" ,end="")
    for q in range(rows - i):
        print(q, end=" ")
    print()
