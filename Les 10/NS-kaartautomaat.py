def inlezen_beginstation(stations):
    'Vraag om beginstation'
    while True:
        beginstation = input('Wat is je beginstation?')
        if beginstation in stations:
            break
    return beginstation


def inlezen_eindstation(stations, beginstation):
    'Vraag om eindstation'
    while True:
        eindstation = input('Wat is je eindstation?')
        if eindstation in stations and stations.index(beginstation) < stations.index(eindstation):
            break
    return eindstation


def omroepen_reis(stations, beginstation, eindstation):
    'Print omroep en prijs voor rit'
    afstand = stations.index(eindstation) - stations.index(beginstation)
    prijs = afstand * 5
    beginindex = stations.index(beginstation) + 1
    print('Het beginstation {} is het {}e station in het traject'.format(beginstation, stations.index(beginstation)+1))
    print('Het eindstation {} is het {}e station in het traject'.format(eindstation, stations.index(eindstation)+1))
    print('De afstand bedraagt {} station(s).'.format(afstand))
    print('De prijs van het kaartje is {} euro.'.format(prijs))
    print('Je stapt in de trein in: {}'.format(beginstation))
    while True:
        if beginindex == stations.index(eindstation):
            break
        else:
            print(stations[beginindex])
            beginindex = beginindex + 1
    print('Je stapt uit in {}'.format(eindstation))



stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',
            'Amsterdam Amstel', 'Utrecht Centraal', 'Den Bosch', 'Eindhoven', 'Weert',
            'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
