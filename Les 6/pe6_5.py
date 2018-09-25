lijst = [4,5,3,-81]
def kwadraten_som(grondgetallen):
    result = 0
    for item in grondgetallen:
        if item > 0:
            result = item ** 2 + result
    return result

print(kwadraten_som(lijst))
