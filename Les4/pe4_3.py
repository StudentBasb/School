uurloon=input('Wat verdien je per uur?')
werktijd=input('Hoeveel uur heb je gewerkt?')

ontvangenLoon = eval(uurloon) * eval(werktijd)

eindzin ='{} uur werken levert je {} euro op!'.format(werktijd, ontvangenLoon)


print(eindzin)
