import random

def monopolyworp():
    dobbel1 = random.randrange(1,7)
    dobbel2 = random.randrange(1,7)
    if dobbel1 == dobbel2:
        print('{} + {} = {} (Dubbel)'.format(dobbel1, dobbel2, dobbel1+dobbel2))
        monopolyworp2()
    else:
        print('{} + {} = {}'.format(dobbel1, dobbel2, dobbel1+dobbel2))

def monopolyworp2():
    dobbel1 = random.randrange(1,7)
    dobbel2 = random.randrange(1,7)
    if dobbel1 == dobbel2:
        print('{} + {} = {} (Dubbel)'.format(dobbel1, dobbel2, dobbel1+dobbel2))
        monopolyworp3()
    else:
        print('{} + {} = {}'.format(dobbel1, dobbel2, dobbel1 + dobbel2))

def monopolyworp3():
    dobbel1 = random.randrange(1, 7)
    dobbel2 = random.randrange(1, 7)
    if dobbel1 == dobbel2:
        print('{} + {} = {} (Direct naar de gevangenis)'.format(dobbel1, dobbel2, dobbel1 + dobbel2))
    else:
        print('{} + {} = {}'.format(dobbel1, dobbel2, dobbel1 + dobbel2))


monopolyworp()