invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

lijst = invoer.split('-')

def optellen(lijst):
    som = 0
    for item in lijst:
        som= eval(item)+som
    return som

def gemiddelde(lijst):
    gem = optellen(lijst)/len(lijst)
    return gem

print('Gesorteerde lijst van ints: {}'.format(lijst))
print('Grootste getal: {} en Kleinste getal: {}'.format(max(lijst),min(lijst)))
print('Aantal getallen: {} en Som van de getallen: {}'.format(len(lijst),optellen(lijst)))
print('Het gemiddelde is: {}'.format(gemiddelde(lijst)))

