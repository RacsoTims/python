for x in range (1,9000):
    divisors = []
    for y in range (1, x):
        if(x%y == 0 and x/y != 1):
            divisors.append(y)
    if(sum(divisors) == x):
        print(x, divisors, int(sum(divisors)))
