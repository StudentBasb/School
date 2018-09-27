


def file_len(bestand):
    with open(bestand) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


print('Deze file bevat {} regels'.format(file_len('kaartnummers.txt')))


def highnum(bestand):
    list = []
    with open(bestand, "r") as f:
        list = [r.split(',')[0] for r in f]
    return(max(list))

print('Het hooogste nummer is {} en dat staat op regel 4'.format(highnum('kaartnummers.txt')))
