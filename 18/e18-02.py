def writeme(text, filepath):
    try:
        with open(filepath, "a", encoding="UTF-8") as x:
            x.write("\n" + ny)
    except Exception as e:
        print(e)
    return("Data: " + "\"{0}\"".format(ny) + " skriven till filen")

ny = 'Diana-Dee Dagsdotter '
x = writeme(ny, '18\e18.txt')
print(x)