# URL: https://projecteuler.net/problem=19

# PROBLEM: How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# 1 jan 1900	ma	1
# 1 feb 1900	do	4
# 1 maart 1900	do	4
# 1 april 1900	zo	7
# 1 mei 1900	do	4
# 1 juni 1900	vr	5
# 1 juli 1900	zo	7
# 1 aug 1900	wo	3
# 1 sep 1900	za	6
# 1 okt 1900	ma	1
# 1 nov 1900	do	4
# 1 dec 1900	za	6

def check_ifLeapYear(year):
    
    is_leap = False
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        is_leap = True
    
    return is_leap


dates = {1: 1, 2: 4, 3: 4, 4: 7, 5: 4, 6: 5,
        7: 7, 8: 3, 9: 6, 10: 1, 11: 4, 12: 6}
counter = 0

for year in range(1901, 2001):
    
    is_leap = check_ifLeapYear(year)
    
    if is_leap:
        for first_of_the_month in dates.keys():
            dates[first_of_the_month] += 2 if first_of_the_month > 2 else 1
    else:
        for first_of_the_month in dates.keys():
            dates[first_of_the_month] += 1
    
    for key in dates.keys():
        if year == 2001:
            continue
        else:
            if dates[key] % 7 == 0:
                counter += 1

print(counter)
