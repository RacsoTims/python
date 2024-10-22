solution = False

for x in range (9, 1, -1):
    for i in range (10, 3000):
        j = int(str(i)[::-1])
        k = j-x*i
        if (k == 0):
            print(i, j, k , str(x) + "x")
            solution = True

if not solution:
    print("There are no solutions for the choosen range.")
