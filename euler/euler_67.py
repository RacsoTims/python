# URL: https://projecteuler.net/problem=67

rows = {}

count = 0
with open('/home/oscar/projects/python/euler_data/euler_67.txt', 'r') as data:
    for row in data:
        rows[count] = list((row.replace("\n", "")).split(" "))
        count += 1

# print(count)
# print(rows)

for x in range(len(rows.keys()) - 2, -1, -1):
    new_row = []
    for y in range(0, len(rows[x])):
        route0 = int(rows[x][y]) + int(rows[x+1][y])
        route1 = int(rows[x][y]) + int(rows[x+1][y+1])
        new_row.append(max([route0, route1]))
    rows[x] = new_row

result = rows[0][0]
print(result)
