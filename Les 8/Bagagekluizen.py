print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
print('2: Ik wil een nieuwe Kluis')
print('3: Ik wil even iets uit mijn kluis halen')
print('4: Ik geef mijn kluis terug')


def kiezen(gekozen):
    'Maakt de keuze uit het menu'
    if gekozen == 4:
        return 'Deze functie werkt niet'
    if gekozen == 3:
        return kluis_openen()
    if gekozen == 2:
        return nieuwe_kluis()
    if gekozen == 1:
        return toon_aantal_kluizen_vrij()
    else:
        return 'Dit is geen geldige optie'


def toon_aantal_kluizen_vrij():
    with open('Kluizen.txt') as f:
        for i, l in enumerate(f):
            pass
    return 12 - (i + 1)


def nieuwe_kluis():
    kluizenlijst = [1,2,3,4,5,6,7,8,9,10,11,12]
    with open('Kluizen.txt') as f:
        regels = f.readlines()
    for regel in regels:
        gesplits = regel.split(';')
        kluizenlijst.remove(int(gesplits[0]))
    wachtwoord = input('Kies een wacthwoord:')
    with open('Kluizen.txt','a') as f:
        f.write('{};{}\n'.format(kluizenlijst[0],wachtwoord))
    return 'Je hebt kluisnummer {}. Je wachtwoord is opgeslagen'.format(kluizenlijst[0])


def kluis_openen():
    nummer = input('Voor uw kluisnummer in:')
    wachtwoord = input('Voor het wachtwoord in:')
    combinatie = '{};{}'.format(nummer, wachtwoord)
    if combinatie in open('kluizen.txt').read():
        return 'Je kluis is nu geopend'
    else:
        return 'Deze combinatie is niet bekend bij ons'


print(kiezen(eval(input('Kies uw optie:'))))
