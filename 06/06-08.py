Rows = int(input("Ange rader: "))

X = 0
Y = 1
Star = "*"


if X <= Rows:
    for i in range(0,Rows+1):
        print(Star.center(Y)*X)
        #print(Star*(Y))
        #Y -=1
        X += 1
    #print()
else:
    for i in range(Rows, 0, -1):
        print(Star.center(Y)*X)
        X -= 1
