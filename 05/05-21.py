tal_1 =int(input("Ange första talet: "))
tal_2 =int(input("Ange andra talet: ")) 

q = 0

if tal_1 <= tal_2:
    for i in range(tal_1, tal_2+1):
        print(i, end=" ")
else:
    for j in range(tal_1, tal_2-1, -1):
        print(j, end=" ")