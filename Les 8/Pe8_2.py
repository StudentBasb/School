def lijst (list1):
    lijst2=[]
    for item in list1:
        if len(item) == 4:
            lijst2.append(item)
        else:
            pass
    return lijst2




Woorden = input("Geef lijst met minimaal 10 strings: ")

lijst1 = Woorden.split(' ')

print(lijst1)


print('De Nieuw gemaakte Lijst met alle vier-letter strings is:')
print(lijst(lijst1))
