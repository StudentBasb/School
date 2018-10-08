def gemiddelde(zin):
    totaal = 0
    gesplit = zin.split()
    for item in gesplit:
        totaal = totaal + len(item)
    return  len(zin) /totaal


zin = input('Voer een zin in:')



print('Het gemiddelde lengte van de woorden zijn:{}'.format(gemiddelde(zin)))