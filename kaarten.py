# import random, itertools

# card = list(itertools.product(range(2,11),["harten", "schoppen", "klaver", "ruiten"]))

# card1 = ["joker", "klaver heer", "harten heer", "schoppen heer", "ruiten heer",
# "klaver boer", "harten boer", "schoppen boer", "ruiten boer", "schoppen aas", "ruiten aas", "harten aas", "klaver aas",
# "harten vrouw", "schoppen vrouw", "klaver vrouw", "ruiten vrouw"]

# kaart = card + card1

# random.shuffle(kaart)

# for i in range (1,8):
#     print("kaart",i,":", kaart[i])
# print("\n","DECK KAARTEN", kaart)

import random

card = ["klaver","schoppen","harten","ruiten"]
card1 = [2,3,4,5,6,7,8,9,10,"boer","vrouw","heer","aas"]
cards = []

for i in card:
    for x in card1:
        cards.append(i + " " +str(x)) 

random.shuffle(cards)

def aantalcards(amount):

    for e in range(1,amount+1):
        index = random.randint(0,len(cards)-1)
        card = cards.pop(index)
        print(f"kaart: {e} {card}")
    
aantalcards(7)

print("\n[DECK]",cards)







 







