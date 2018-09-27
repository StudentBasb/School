

def convert(celsius):
    for item in celsius:
        if item == item:
            tempFahrenheit=item*1.8+32
        print('{} {}'.format(tempFahrenheit,item))

convert(range(-30,41,10))