import random


def intro():
    print('-----------------------------------------------------------------------')
    print('                      Welcome to Dobbel Trobbel                        ')
    print('-----------------------------------------------------------------------')
    
def scoreboard():    
    print('Position: |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |')
    print('-----------------------------------------------------------------------')
    Blauw_SB = []
    Rood_SB = []
    Wit_SB = []
    return (Blauw_SB,Rood_SB,Wit_SB)
    

# def dobbelsteen(aantal):
# dobbelsteen_lijst = []
#     for i in range(0,aantal):
#         dobbelsteen = random.randint(1,6)
#         witdobbelsteen = [1,1,1,2,2,3]
#         dobbelsteen_lijst.append(dobbelsteen)
#         dobbelsteen_lijst.append(witdobbelsteen)
#     return dobbelsteen_lijst

# print(dobbelsteen(3))

def dobbelsteen():
    blauw_dobbelsteen = random.randint(1,6)
    rood_dobbelsteen = random.randint(1,6)
    witte_dobbelsteen = [1,1,1,2,2,3]
    waarde_witdobbelsteen = random.choice(witte_dobbelsteen)
    return (blauw_dobbelsteen,rood_dobbelsteen,waarde_witdobbelsteen)

def berekening(blauw_DS,rood_DS,wit_DS):
    berekening_1 = blauw_DS + rood_DS + wit_DS
    berekening_2 = blauw_DS + rood_DS - wit_DS
    berekening_3 = blauw_DS + rood_DS
    berekening_4 = berekening_1 - berekening_2
    return (berekening_1,berekening_2,berekening_3,berekening_4)
    
def keuzen():
    keuzenlijst = ["A","B","C","D"]
    keuze = input("kies. A | B | C | D | : ").upper()
    index = keuzenlijst.index(keuze)
    return index

def bepaal_lijst_kleur(blauw,rood):
    if blauw < rood:
        return "Blauw"
    elif rood < blauw:
        return "Rood"
    keuzen = input("In welke lijst wil je het hebben? Rood / Blauw:? ").upper()
    return keuzen 

actief = True
while actief:
    intro()
    Blauw_SB,Rood_SB,Wit_SB = scoreboard()
    blauw,rood,wit = dobbelsteen()
    uitkomsten = berekening(blauw,rood,wit)
    print("\n",blauw," | ",rood," | ",wit," | ")
    print("\n")
    print("A:",blauw,"+",rood,"+",wit,"=",uitkomsten[0])
    print("B:",blauw,"+",rood,"-",wit,"=",uitkomsten[1])
    print("C:",blauw,"+",rood,"=",uitkomsten[2])
    minimun = min(blauw,rood,wit)
    maximum = max(blauw,rood,wit)
    totaal = (maximum - minimun)
    print("D:",maximum,"-",minimun,"=",totaal)
    index = keuzen()
    uitkomsten[index]
    bepaal_lijst_kleur()

    actief = False






    



