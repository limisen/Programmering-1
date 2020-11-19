#Det räcker med att göra en "lösning" med hjälp av EN loop

Pengar = 1
ränta = 1.02
Pengar_efter_ränta = (Pengar * ränta)

for i in range(1,2018):
    Pengar_efter_ränta = (Pengar * ränta)
    Pengar = Pengar_efter_ränta
int(Pengar)


print("{0}kr med 2% ränta i 2017 år blir {1:1.0f}kr".format(1, Pengar_efter_ränta))