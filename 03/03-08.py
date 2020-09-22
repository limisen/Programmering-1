#Vikgt i meter, Längd i kg
vikt = input("Ange vikt: ")
längd = input("Ange längd: ")

vikt = float(vikt)
längd = float(längd)

#uträkning av BMI
#Formel för BMI: Bmi=Vikgt/längd**2
Bmi = (vikt/(längd**2))


print("Vikt:",vikt)
print("Längd:",längd)
print("BMI={0:4.2f}".format(Bmi))


print("Raw output:",Bmi)