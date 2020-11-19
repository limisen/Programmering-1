Rows = int(input("Ange rader: "))

X = 0
Y = 1
q = 0
Star = "*"

while q != 1:
    if X <= Rows:
        for i in range(0,Rows):
            print((Star*X).center(Rows))
            Y -=1
            X += 1
        for i in range(Rows, 0, -1):
            print((Star*X).center(Rows))
            X -= 1
    q += 1
