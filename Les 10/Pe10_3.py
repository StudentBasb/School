def code(invoerstring):
    'Zet invoer om in codering'
    s = ''
    for letter in invoerstring:
        omzet = ord(letter)
        bijna = chr(omzet + 3)
        s += bijna
    return(s)

print(code("RutteAlkmaarDen Helder"))
