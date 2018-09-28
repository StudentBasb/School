def seizoen(maand):
    if maand >= 13:
        return 'Er zijn maar 12 maanden in een jaar.'
    if maand == 12:
        return 'Het is Winter'
    if maand >= 9:
        return 'Het is Herfst'
    if maand >= 6:
        return 'Het is Zomer'
    if maand >= 3:
        return 'Het is Lente'
    if maand >= 1:
        return 'Het is Winter'
    else:
        pass

print(seizoen(eval(input('Hoeveelste maand is het?'))))
