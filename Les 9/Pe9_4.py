bedrijven = {'Yahoo':'YHOO',
             'Google INC':'GOOG',
             'Harley-Davidson':'HOG',
             'Yamana Gold':'AUY',
             'Sotheby\'s': 'BID',
             'inBev':'BUD'}

def ticker(filename):
    bedrijf = input('Enter company name:')
    ticker = filename[bedrijf]
    print('Ticker symbol: {}'.format(ticker))
    print()
    ticker2 = input('Enter Ticker Symbol:')
    for i in filename:
        if filename[i]==ticker2:
            print('Company name: '+i)

ticker(bedrijven)
