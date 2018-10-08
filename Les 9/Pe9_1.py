def functie():
    list = []
    while True:
        getal=eval(input('Geef een getal:'))
        if getal == 0:
            break
        list.append(getal)
    print('Er zijn {} getallen ingevoerd, de som is: {}'.format(len(list),sum(list)))

functie()

