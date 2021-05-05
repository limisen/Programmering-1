from random import sample

def chose_volonteers(x):
    klasslista = ['Kalle', 'Ada', 'Lisa', 'Fredrik', 'Charlotte','Ulrika']

    valda = sample(klasslista, k=(x))
    ej_valda = []
    

    print("Ej valda: ", "Valda: ", valda)

print(chose_volonteers(3))
#Ej klar!