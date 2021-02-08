word = input("Skriv in ett ord med sju tecken eller mer och udda antal tecken: ")

word_len = len(word)

if word_len >= 7 and word_len % 2 == 0:
    print(word[3:6])
else:
    print(word[::-1]) 

#Should be output: Errolf if input = teknik
