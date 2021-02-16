def fib(x):
    """Skriver ut alla tal i fibonatchi's talföljd up till angivet antal (i en lista)"""
    list = [0, 1]
    for n in range(0, x-1):
        z = list[n] + list[n + 1]
        list.append(z)
    list.pop(0)
    return(list)

print(fib(10))
#klar