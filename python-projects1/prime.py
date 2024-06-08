primes= []

print("In the given range the following are the prime numbers that are the sum of two other prime numbers:")
#print("Prime numbers in given range are:")
for i in range (2, 10000):
    prime = []
    for j in range (1, i+1):
        k = i % j
        if (k == 0):
            prime.append(i)
    if (len(prime) == 2):
        primes.append(i)
        

for i in primes:
    for j in primes:
        if (j == i):
            continue
        k = i - j
        if k in primes:
            print(f"{i} {j}+{k}")
            