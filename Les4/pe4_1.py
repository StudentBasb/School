cijferICOR = 6.0
cijferPROG = 6.5
cijferCSN =  7.5

gemiddelde = (cijferICOR + cijferPROG + cijferCSN) / 3

beloning = (cijferICOR * 30) + (cijferPROG * 30) + (cijferCSN * 30)


overzicht = 'Mijn Cijfers (gemiddeld een {}) leveren een beloning van € {} op!'.format(gemiddelde, beloning)


print(overzicht)
