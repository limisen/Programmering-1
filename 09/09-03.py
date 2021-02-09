def maximum(x, y):
    """ Returnerar det största av två tal """
    if x > y:
        print("{0:.3f}".format(x))
        return(x)
    elif y > x:
        print("{0:.3f}".format(y))
        return(y)

x1, x2 = 5, 10
maximum(x1, x2)

x1, x2 = 15.8877, 10.12345
maximum(x1, x2)
#klar!