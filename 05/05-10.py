start = int(input("Ange högsta temperaturen: "))
stop = int(input("Ange lägsta temperaturen: "))



for i in range(start, stop -5):
    farenheit = 32 + i * 9/5
    print(farenheit)