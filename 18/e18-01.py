def readme(x):
    try:
        path = "." + x
        f = open(path, "r", encoding="UTF-8")
        text = f.read()
        f.close()
    except FileNotFoundError:
        text = ("Eror 404: File was not located, File may not exist or you may not have the necessary permissions.")
    finally:
        print(text,"\n---------------------------")



readme('e18.txt')  # Filen finns

readme('e18-error.txt')  # Filen finns ej
