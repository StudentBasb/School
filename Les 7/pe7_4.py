infile=open('hardlopers.txt','r+')

def strftime():
    import datetime
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y")
    return s
waarde =''
waarde+=strftime()
waarde+=', '
waarde+=input('Welke tijd heb je gelopen?')
waarde+=', '
waarde+=input('Wat is je naam?')
infile.write(waarde)
