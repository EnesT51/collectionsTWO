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
    print("Blauw_lijst       ",Blauw_SB)
    print("Rood_lijst        ",Rood_SB)
    print("Wit_lijst         ",Wit_SB)
    print('-----------------------------------------------------------------------')

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
        return "rood"
    elif rood < blauw:
        return "blauw"
    keuzen = input("In welke lijst wil je het hebben? Rood / Blauw:? ").lower()
    return keuzen

def position_lijst(lijst_kleur,index_1):
    if lijst_kleur == "blauw":
        positie = int(input('in welke positie van de blauwe lijst wil je het hebben? '))
        if Blauw_SB[positie -1] == "":
           Blauw_SB[positie -1] = uitkomsten[index_1]
        else:
            print("er zit al een waarde in de gekozen index ")
            position_lijst(lijst_kleur,index_1) 
    elif lijst_kleur == "rood":
        positie = int(input('in welke positie van de rode lijst wil je het hebben? '))
        if Rood_SB[positie -1] == "":
           Rood_SB[positie -1] = uitkomsten[index_1]
        else:
            print("er zit al een waarde in de gekozen index ")
            position_lijst(lijst_kleur,index_1)

def checkingtheindex(lijst,index_1,nummer):
    if lijst[index_1 +1] > nummer:
        if lijst[index_1 -1] < nummer:
            if lijst[index_1] =="":
                return True
    return False

actief = True
poswit = 0
while actief:
    intro()
    scoreboard()
    blauw,rood,wit = dobbelsteen()
    uitkomsten = berekening(blauw,rood,wit)
    print("\n","Blauw:",blauw," | ","Rood:",rood," | ","Wit:",wit," | ")
    print("\n")
    print("A:",blauw,"+",rood,"+",wit,"=",uitkomsten[0])
    print("B:",blauw,"+",rood,"-",wit,"=",uitkomsten[1])
    print("C:",blauw,"+",rood,"=",uitkomsten[2])
    minimun = min(blauw,rood,wit)
    maximum = max(blauw,rood,wit)
    totaal = (maximum - minimun)
    print("D:",maximum,"-",minimun,"=",totaal)
    print("\n")
    index = keuzen()
    uitkomsten[index]
    gekozen_lijst = bepaal_lijst_kleur(blauw,rood)
    position = position_lijst(gekozen_lijst,index)
    if index == 2 or index == 3:
        Wit_SB[poswit] = wit
        poswit+=1
    checkingtheindex()
    
    








    



