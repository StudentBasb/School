import datetime
import csv

bestand = 'inloggers.csv'

def registreren ():
    with open('inloggers.csv', 'w', newline='') as CSVbestand:
        while True:
            naam = input('Wat is je achternaam')
            if naam == 'einde':
                break
            else:
                voorl = input("Wat zijn je voorletters? ")
                gbdatum = input("Wat is je geboortedatum? ")
                email = input("Wat is je e-mail adres? ")
                writer = csv.writer(CSVbestand, delimiter=';')
                writer.writerow((datetime.datetime.now(), voorl, naam, gbdatum, email))



registreren()