try:
    from random import randint

    def magicalformula(x):
        """This is a magical formula
        Args:
            x (float): number

        Returns:
            float: magical number
        """
        magic = x / randint(0, 2)
        return magic

    print(magicalformula(5.5))
    # print(magicalformula('kaka'))
except ZeroDivisionError:
    print("float division by zero")
except TypeError:
    print("unsupported operand type(s) for /: 'str' and 'int'")
#klar!
