leeftijd = eval(input('Geef je leeftijd:'))
nlpaspoort = input('Bezit je een Nederlands paspoort?')


if leeftijd > 17 and nlpaspoort == 'ja':
    print('Gefeliciteerd, je mag stemmen!')
else:
    print('Je mag helaas niet stemmen.')