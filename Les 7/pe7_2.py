
with open('kaartnummers.txt') as kaartnummers:
    for word in kaartnummers:
        nummer=word.split(',')
        print('{} heeft als klantnummer: {}'.format(nummer[1], nummer[0]))