import csv
hoogste = 0
with open('gamers.csv', 'r') as CSVBestand:
    reader = csv.reader(CSVBestand, delimiter=';')
    for row in reader:
        if hoogste < int(row[2]):
            hoogste = int(row[2])
            naam = row[0]
            datum = row[1]
        else:
            pass

    print('De hoogste score is: {} op {} behaal door {}'.format(hoogste, datum, naam))