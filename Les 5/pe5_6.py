s = "Guido van Rossum heeft programmeertaal Python bedacht."
woord = ''
for letter in s:
    if letter in['a','e','i','o','u']:
        woord+=letter
print(woord)
    
