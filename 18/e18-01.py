def readme(filepath):
    try:
        f = open(filepath, "r", encoding="UTF-8")
        text = f.read()
        f.close()
    except FileNotFoundError:
        text = ("Filen kan inte öppnas")
    finally:
        print(text,"\n---------------------------")

readme('18\e18.txt')  # Filen finns

readme('18\e18-error.txt')  # Filen finns ej
