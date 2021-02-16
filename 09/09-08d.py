def fib(x):
    """Skriver ut alla tal i fibonatchi's talföljd up till angivet antal"""
    list = [0, 1]
    for n in range(0, x-2):
        z = list[n] + list[n + 1]
        list.append(z)
    #return(list)
    for n in range(0,len(list)):
        print(str(list[n]), sep="")

print(fib(5))