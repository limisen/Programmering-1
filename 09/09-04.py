def maximum(x, y, z):
    """ Returnerar det största av två tal """
    if x > y and x > z:
        return(x)
    elif y > x and y > z:
        return(y)
    elif z > y and z > x:
        return(z)

x = maximum(15, 18, 10)
print(x)


x = maximum(155.123456, 18.18, 10.95)
print(x)
#Klar!