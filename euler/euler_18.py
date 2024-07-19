# URL: https://projecteuler.net/problem=18

import sys
sys.path.append("C:\\Users\\oscar\\my_stuff\\bash\\tools")
import utils

rows = {}

count = 0
path = utils.determine_path()
with open(f'{path}euler_18.txt', 'r') as data:
    for row in data:
        rows[count] = list((row.replace("\n", "")).split(" "))
        count += 1

for x in range(len(rows.keys()) - 2, -1, -1):
    new_row = []
    for y in range(0, len(rows[x])):
        route0 = int(rows[x][y]) + int(rows[x+1][y])
        route1 = int(rows[x][y]) + int(rows[x+1][y+1])
        new_row.append(max([route0, route1]))
    rows[x] = new_row

result = rows[0][0]
print(result)
