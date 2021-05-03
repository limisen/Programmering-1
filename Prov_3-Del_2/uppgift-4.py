student = [
    {
        "firstname": "Lisa",
        "lastname": "Spik",
        "age": 18
    },
    {
        "firstname": "Sune",
        "lastname": "Smart",
        "age": 19
    }
]
#Utifrån följande kod ska du få nedstående utdata. 
# 1: Lisa Spik, 18
# 2: Sune Smart, 19
print(len(student))
def pep_info(x):
    for items in x:
        for i in range(0,1):
            print("{}", end=" ")
    
    return()

pep_info(student)
