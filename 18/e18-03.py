def numberOfLines(filepath):
    try:
        import os
        if os.path.exists(filepath):
            print('Filen finns, räknar rader...')
            with open(filepath, "r", encoding = 'UTF-8') as f:
                nr_lines = 0
                for lines in f.readlines():
                    nr_lines += 1
        else:
            print('Filen finns inte, testa annan filsökväg \n ---------------------------')
    except Exception:
        pass
    finally:
        return(nr_lines)
x = numberOfLines('18\e18.txt')
print('Det är', x, 'rader i filen')