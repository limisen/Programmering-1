def fib_kvot(x):
    """Räknar ut kvoten mellan tal n och förgående tal. Från andra indexen till den sista """
    list = [0, 1]
    for n in range(0, x-2):
        z = list[n] + list[n + 1]
        list.append(z)
    
    for 

print(fib_kvot(40))