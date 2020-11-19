tal_1 =int(input("Ange första talet: "))
tal_2 =int(input("Ange andra talet: ")) 

for i in range(0,2):
    if tal_1 >= tal_2:
        for i in range(tal_1, tal_2):
            print(i)
    elif tal_2 >= tal_1:
        for i in range(tal_2, tal_1):
            print(i)