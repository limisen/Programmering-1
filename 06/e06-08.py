text = input("Skriv texten: \n")
text = text.strip()
#text = "kalle kanin är en hare så det så"

split = int(len(text) / 2)

text_1 = text[0:split]
text_2 = text[split:len(text)]

#print(text_1, text_2, sep="\n")

i = 0


if text_2[i] in text_2 == " ":
    i += 1
    #print(text_2[i])
elif text_2[i] in text_2 != " ":
    print(text_1, text_2[i:len(text)], sep="\n")

#Jag kan dela på texten men det går inte att säkerst göra så text_2 inte börjar med " "