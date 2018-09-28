def vermenigvuldigen(getal):
    while getal < 11:
        keer1 = getal * 1
        keer2 = getal * 2
        keer3 = getal * 3
        keer4 = getal * 4
        keer5 = getal * 5
        keer6 = getal * 6
        keer7 = getal * 7
        keer8 = getal * 8
        keer9 = getal * 9
        keer10 = getal * 10
        print('1 * {} = {}'.format(getal,keer1))
        print('2 * {} = {}'.format(getal, keer2))
        print('3 * {} = {}'.format(getal, keer3))
        print('4 * {} = {}'.format(getal, keer4))
        print('5 * {} = {}'.format(getal, keer5))
        print('6 * {} = {}'.format(getal, keer6))
        print('7 * {} = {}'.format(getal, keer7))
        print('8 * {} = {}'.format(getal, keer8))
        print('9 * {} = {}'.format(getal, keer9))
        print('10 * {} = {}'.format(getal, keer10))
        getal = getal + 1
    else:
        pass

vermenigvuldigen(1)

