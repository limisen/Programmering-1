student = {
    "firstname" : "Lisa",
    "lastname"  : "Spik",
    "age"       : 18
}
#Utifrån följande kod ska du få nedstående utdata. (Lisa Spik, 18)

for items in student:
    for i in range(0,1):
        print(student.get(items), end=" ")