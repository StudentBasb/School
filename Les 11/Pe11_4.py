import csv
voorraad = 1000
prijs = 0
totaal = 0
with open('producten.csv', 'r') as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter=';')

    for row in reader:
        totaal = int(row['Voorraad']) +totaal
        if prijs < float(row['Prijs']):
            prijs = float(row['Prijs'])
            maxnaam = row['Naam']
        else:
            pass

        if voorraad > int(row['Voorraad']):
            voorraad = int(row['Voorraad'])
            voorraadnummer = row['Artikelnummer']
        else:
            pass
    print('Het duurste artikel is {} en die kost {}'.format(maxnaam,prijs))
    print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(voorraad, voorraadnummer))
    print('In totaal hebben wij {} producten in ons magazijn liggen'.format(totaal))