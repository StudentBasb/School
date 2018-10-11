def hotelberekenen ():
    try:
        aantal = int(input('Met hoeveel personen reis je? '))
        if aantal <= 0:
            raise Exception
        totaal = 4356 / aantal
        return totaal
    except ValueError:
        print('Gebruik cijfers voor het invoeren van het aantal!')
    except ZeroDivisionError:
        print('Delen door nul kan niet!')
    except Exception:
        print('Negatieve getallen zijn niet toegestaan')
    except:
        print('Onjuiste invoer!')

print(hotelberekenen())