import random


Blauw_SB =[-2,"","","","","","","","",""]
Rood_SB  =["","","","","","","","","",-2]
Wit_SB   =["","","","",""]

def intro():
    print('-----------------------------------------------------------------------')
    print('                      Welcome to Dobbel Trobbel                        ')
    print('-----------------------------------------------------------------------')

def scoreboard():    
    print('\nPosition: |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |')
    print('-----------------------------------------------------------------------')
    print(f'Blauw lijst: |{Blauw_SB[0]}   |  {Blauw_SB[1]} |  {Blauw_SB[2]}|  {Blauw_SB[3]} |  {Blauw_SB[4]} |  {Blauw_SB[5]} |  {Blauw_SB[6]} |  {Blauw_SB[7]} |  {Blauw_SB[8]} |  {Blauw_SB[9]}|')
    print(f'Rood lijst:  |{Rood_SB[0]}  |  {Rood_SB[1]}  |  {Rood_SB[2]} |  {Rood_SB[3]}  |  {Rood_SB[4]}  |  {Rood_SB[5]}  |  {Rood_SB[6]}  |  {Rood_SB[7]}  |  {Rood_SB[8]}  |  {Rood_SB[9]} |')
    print(f'wit lijst:                 |  {Wit_SB[0]}   |  {Wit_SB[1]}   |  {Wit_SB[2]}   |  {Wit_SB[3]}   |  {Wit_SB[4]}   |')
    print('-----------------------------------------------------------------------')
    

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

def lijst_index():
    pass

actief = True
while actief:
    intro()
    scoreboard()
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
    keuzen_lijst = bepaal_lijst_kleur()
    lijst_index(keuzen_lijst)
    actief = False






    



