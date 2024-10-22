import numpy as np
import random as rand

lijst1 = [1, 8, 8, 8, 4, 6, 6, 6, 6]

serie_length = int(input("> "))

# zoek en vind de opeenvolgende getallen op basis van 'serie_length'
def vind_serie(aantal, lijst):
    
    resultaat = []
    
    for i in range(len(lijst)- aantal + 1):

        j = 1
        serie = [lijst[i]]

        while j < aantal:
            
            if lijst[i+j] != lijst[i]:
                break
            else:
                serie.append(lijst[i+j])    
                j += 1

        if len(serie) == aantal:
            resultaat.append(serie)
    
    return resultaat

gevonden = vind_serie(serie_length, lijst1)
print(gevonden)

# 2
print(rand.randint(0, 36))
lst = [rand.randint(0, 36) for i in range(100)]
lst.sort()
frequencies = {}
for number in lst:
    if number not in frequencies.keys():
        frequencies[number] = lst.count(number)
    else:
        continue
print(frequencies)
print(frequencies.values())
