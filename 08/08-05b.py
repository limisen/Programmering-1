listan = [12, 45, 67, 87, 9, 4, 34, 11, 3, 7, 74, 47, 39, 27, 14, 19, 44]

x = listan[0]
z = 0

for isinstance in listan:
    z += 1

for i in range(0, z):
    y = listan[i]
    if y < x:
        x = y
    print(x)

i = 0

if y != x:
    y = listan[i]
    i +=1
else:
    print(y)

print("Minsta talet är {0} och det återfinns på plats {1}".format(x, y))

#Inte klar!