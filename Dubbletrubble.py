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
    berekening_4 = max(blauw_DS,rood_DS,wit_DS) - min(blauw_DS,rood_DS,wit_DS)
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
        if checkingtheindex(Blauw_SB,positie,uitkomsten[index_1]):
           Blauw_SB[positie -1] = uitkomsten[index_1]
        else:
            print("there is already a value in the chosen index")
            print(Blauw_SB)
            position_lijst(lijst_kleur,index_1) 
    elif lijst_kleur == "rood":
        positie = int(input('in welke positie van de rode lijst wil je het hebben?  '))
        if checkingtheindex_2(Rood_SB,positie,uitkomsten[index_1]):
            Rood_SB[positie -1] = uitkomsten[index_1]
        else:
            print("there is already a value in the chosen index ")
            print(Rood_SB)
            position_lijst(lijst_kleur,index_1)

def checkingtheindex_2(lijst,index__1,nummer):

    if nummer in lijst or lijst[index__1-1] != "":
        return False

    index__1 = index__1-1 
    for val in lijst[:index__1+1]:
        if val != "":
            if val < nummer:
                return False
    for val in lijst[index__1:]:
        if val != "":
            if val > nummer:
                return False
    lijst[index__1] = nummer
    return True

def checkingtheindex(lijst,index_2,nummer):
    
    if nummer in lijst or lijst[index_2-1] != "":
        return False 
    
    index_2 = index_2 -1 
    for val in lijst[:index_2+1]:
        if val != "":
            if val > nummer:
                return False
    for val in lijst[index_2:]:
        if val != "":
            if val < nummer:
                return False
    lijst[index_2] = nummer
    return True


def index_berekenenlijst(blauw_lijst,Rood_lijst):
    subtotaal_1 = blauw_lijst[0] * Rood_lijst[0] + blauw_lijst[1] * Rood_lijst[1] + blauw_lijst[2] * Rood_lijst[2] + blauw_lijst[3] * Rood_lijst[3] + blauw_lijst[4] * Rood_lijst[4] + blauw_lijst[5] * Rood_lijst[5] + blauw_lijst[6] * Rood_lijst[6] + blauw_lijst[7] * Rood_lijst[7] + blauw_lijst[8] * Rood_lijst[8] + blauw_lijst[9] * Rood_lijst[9] 
    return subtotaal_1


def check_in_index_for_True_or_False(lijst,index):
    
    for val in lijst[index+1:]:
        if val == "":
            return True
    for val in lijst[:index]:
        if val  == "":
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
    print("D:",maximum,"-",minimun,"=",uitkomsten[3])
    print("\n")
    gekozen_nummer = keuzen()
    uitkomsten[gekozen_nummer]
    gekozen_lijst = bepaal_lijst_kleur(blauw,rood)
    position = position_lijst(gekozen_lijst,gekozen_nummer)
    if gekozen_nummer == 2 or gekozen_nummer == 3:
        Wit_SB[poswit] = wit
        poswit+=1
    check_True_or_False = check_in_index_for_True_or_False(gekozen_lijst,position)
    if check_True_or_False == False:
        print(index_berekenenlijst(Blauw_SB,Rood_SB))


