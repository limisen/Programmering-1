#Input för tal#1 vilket sedan görs om till ett flyttal för att kunna användas senare
tal1 = input("Ange tal#1: ")
tal1=float(tal1)

#Input för tal#2 vilket sedan görs om till ett flyttal för att kunna användas senare
tal2 = input("Ange tal#2: ")
tal2 =float(tal2)

#Input för tal#3 vilket sedan görs om till ett flyttal för att kunna användas senare
tal3 = input("Ange tal#3: ")
tal3 =float(tal3)

summa = (tal1 + tal2 + tal3)

#Centrerar tal#1-3 så att de ser fint ut
print("    {0:>4.2f}".format(tal1))
print("    {0:>4.2f}".format(tal2))
print("+   {0:>4.2f}".format(tal3))
print("==========")
print("    {0:>0.2f}".format(summa))