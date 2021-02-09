def maximum(x, y):
    """ Returnerar det största av två tal """
    if x > y:
        print(x)
        return(x)
    elif y > x:
        print("{0:.3f}".format(y))
        return(y)

x = maximum(15, 18, 10)
print("{0:.3f}".format(x))
x = maximum(155.123456, 18.18, 10.95)
print("{0:.3f}".format(x))