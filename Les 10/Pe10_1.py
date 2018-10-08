
bruin = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Helmond Hout', 'Helmond', 'Helmond Brouwhuis', 'Deurne'}
groen = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}


gezamenlijktraject = bruin.intersection(groen)

alleenbruin = bruin.difference(groen)
alleengroen = groen.difference(bruin)

print('Alle treinen gaan naar:{}'.format(gezamenlijktraject))
print('Bruine treinen gaan naar {}'.format(alleenbruin))
print('Groene treinen gaan naar {}'.format(alleengroen))

