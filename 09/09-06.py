def calculator(x,y,z):
    """Utför operationen x z y. Till exempel om z = + så addearas x med y"""
    if z == "+":
        return(x + y)
    elif z == "-":
        return(x - y)
    elif z == "/":
        return(x / y)
    elif z == "*":
        return(x * y)

print(calculator(10, 2, '+'))


print(calculator(10, 2, '-'))


print(calculator(10, 2, '/'))


print(calculator(10, 2, '*'))
#klar!