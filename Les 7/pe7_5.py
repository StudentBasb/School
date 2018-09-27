def gemiddelde(zin):
    totaal = 0
    for item in zin:
        totaal=totaal + len(zin)
    return totaal


zin = input('Voer een zin in:')
gesplit = zin.split()


print('Het gemiddelde lengte van de woorden zijn:{}'.format(zin))