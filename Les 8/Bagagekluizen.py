print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
print('2: Ik wil een nieuwe Kluis')
print('3: Ik wil even iets uit mijn kluis halen')
print('4: Ik geef mijn kluis terug')


def kiezen(gekozen):
    if gekozen == 4:
        return 'Deze functie werkt niet'
    if gekozen == 3:
        optie3()
    if gekozen == 2:
        return (nieuwe_kluis())
    if gekozen == 1:
        return(toon_aantal_kluizen_vrij())
    else:
        return 'Dit is geen geldige optie'


def toon_aantal_kluizen_vrij():
    with open('Kluizen.txt') as f:
        for i, l in enumerate(f):
            pass
    return 12 -(i + 1)

def nieuwe_kluis():
    kluizenlijst = [1,2,3,4,5,6,7,8,9,10,11,12]
    with open('kluizen.txt', 'r') as f:
        myNames = f.readlines()
        kluizen = myNames.split(';')
        del kluizen[::2]
    return(kluizen)

def kluis_openen():

    
print(kiezen(eval(input('Kies uw optie:'))))
