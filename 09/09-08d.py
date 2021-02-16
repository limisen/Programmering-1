def fib(x):
    """Skriver ut alla tal i fibonatchi's talföljd up till angivet antal"""
    list = [0, 1]
    for n in range(0, x-1):
        z = list[n] + list[n + 1]
        list.append(z)
    list.pop(0)
    
    for n in range(1,len(list)):
        print(str(list[n]), end=", ")
        

print(fib(5))

#Inte klar. Får med en "none" samt vet inte hur jag ska få bort sista kommat.