def standaardprijs(afstandKM):
    if afstandKM >= 80:
        prijs = 15 + 0.60 * afstandKM
        return prijs
    elif afstandKM > 0:
        prijs = afstandKM * 0.80
        return prijs
    else:
        prijs = 0
        return prijs


def ritprijs(leeftijd, weekendrit, afstandKM):
    prijsZonderKorting = standaardprijs(afstandKM)
    if leeftijd >= 65 and weekendrit == true:
        weekend65plus = prijsZonderKorting * 0.65
        return weekend65plus
    elif leeftijd <= 12 and weeekendrit == true:
        weekend12min = prijsZonderKorting * 0.65
        return weekend12min
    elif weekendrit == true:
        kortings_prijs = prijsZonderKorting * 0.60
        return kortings_prijs
    elif leeftijd >= 65:
        prijs65plus = prijsZonderKorting * 0.70
        return prijs65plus
    elif leeftijd <= 12:
        prijs12min = prijsZonderKorting * 0.70
        return prijs12min
    else:
        return prijsZonderKorting


totaalprijs = 0
afstandKM = eval(input('Hoeveel KM reis je?'))
weekendrit = input('Reis je in het weekend?') == 'ja'

aantalpersonen = eval(input('Met hoeveel personen reis je?'))


def leeftijd(aantalpersonen, afstandKM, weekendrit, totaalprijs):
    while aantalpersonen > 0:
        Leeftijd = eval(input('Hoe oud is deze persoon?'))
        totaalprijs = ritprijs(Leeftijd, weekendrit, afstandKM) + totaalprijs
        aantalpersonen = aantalpersonen - 1
    if aantalpersonen == 0:
        return totaalprijs


print(leeftijd(aantalpersonen, afstandKM, weekendrit, totaalprijs))
