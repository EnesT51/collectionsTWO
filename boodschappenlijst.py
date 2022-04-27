

def boodschappen():
    boodschappenlijst = 10
    list = {}
    for i in range(boodschappenlijst):
        vraag = input("wat heb je nodig? ")
        if not vraag in list: 
            list[vraag] = 1
        else:
            list[vraag] += 1          
    return list 

print(boodschappen())


def boodschappen():
    boodschappenlijst = True
    list = {}
    while boodschappenlijst:
        vraag = input("wat heb je nodig? ")
        if vraag == "klaar":
            boodschappenlijst =False

        elif not vraag in list:
            list[vraag] = 1

        else:
            list[vraag] += 1    
    return list

print(boodschappen())
        
        

