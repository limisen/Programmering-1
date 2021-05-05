from random import choice

txt = "teknikprogrammet"

def slump_teken():
    """ Slumpar fram ett teken utifrån angiven sträng """

    txt = input("Ange en sträng text du vill ta ut ett tecken ifrån: ")
    txt = choice(txt)
    print("Slumpen gave oss tecknet '{0}'".format(txt))
    return

print(slump_teken())