
def num_there(s): #Controle op minstens 1 nummer
    return any(i.isdigit() for i in s)


def new_password(oldpassword, newpassword):
    if num_there(newpassword) is true :
        if oldpassword == newpassword:
            return 'Sorry, je wachtwoord voldoet niet aan de eisen!'
        else:
            return 'Je wachtwoord voldoet aan de eisen'

oudwachtwoord = input('Wat is je oude wachtwoord?')
nieuwwachtwoord = input('Wat is je nieuwe wachtwoord?')

if 6 < len(nieuwwachtwoord):
    print('Minimaal 6 karakters zijn nodig!')
else:
    print(new_password(oudwachtwoord, nieuwwachtwoord))





