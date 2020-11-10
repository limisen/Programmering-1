#MED WHILE-loop

start = int(input("Ange startvärde: "))
stop = int(input("Ange stoptvärde: "))+1


while start < stop:
    print(start, end=" ")
    start += 1
