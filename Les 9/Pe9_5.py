namen = []

def wordCount(text):
    verbeterd =str(text)
    wordList = verbeterd.split()
    counters = {}
    for word in wordList:
        if word in counters:
            counters[word]+= 1
        else:
            counters[word]=1
    for word in counters:
        if counters[word] == 1:
            print('Er is {} student met de naam {:8}'.format(counters[word],word))
        else:
            print('Er zijn {} studenten met de naam {:8}'.format(counters[word],word))



def namenToevoegen(namen):
    while True:
        naam = input('Volgende naam:')
        if naam == '':
            break
        else:
            namen.append(naam)
            continue
    wordCount(namen)

namenToevoegen(namen)
