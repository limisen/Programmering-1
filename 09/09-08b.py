def fib_kvot(x):
    """Räknar ut kvoten mellan tal n och förgående tal. (Från andra indexen till den sista)"""
    list = [0, 1]
    for n in range(0, x-1):
        z = list[n] + list[n + 1]
        list.append(z)
    list.pop(0)
    list_len = len(list)

    list = list
    for n in range(0, list_len):
        print(list[n])

print(fib_kvot(5))
#Ej klar