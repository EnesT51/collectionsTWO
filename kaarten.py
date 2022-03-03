import random, itertools

card = list(itertools.product(range(2,11),["harten", "schoppen", "klaver", "ruiten"]))

card1 = ["joker", "klaver heer", "harten heer", "schoppen heer", "ruiten heer",
"klaver boer", "harten boer", "schoppen boer", "ruiten boer", "schoppen aas", "ruiten aas", "harten aas", "klaver aas",
"harten vrouw", "schoppen vrouw", "klaver vrouw", "ruiten vrouw"]

kaart = card + card1

random.shuffle(kaart)

for i in range (1,8):
    print("kaart",i,":", kaart[i])
print("\n","DECK KAARTEN", kaart)







 







