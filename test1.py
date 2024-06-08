# verschil tussen 'break' en 'continue'

# Continue: geef alleen even getallen weer
a = 0
while a < 10:
    if a % 2 != 0:
        a += 1
        continue
    else:
        print(a)
    a += 1

# Break: stop zodra je een oneven getal tegenkomt
a = 0
while a < 10:
    if a % 2 != 0:
        a += 1
        break
    else:
        print(a)
    a += 1

# hoe werken functies ook alweer?
b = 2
def vermenigvuldiging (getal):
    return getal * 5
print(vermenigvuldiging(b))