# URL: https://projecteuler.net/problem=7

# OPDRACHT
# What is the 10001st prime number?

primes = [2]
found = 1

start = 3 #check if prime from this number onward; next number is n + 2 (step)
step = 2
limit = 10001 # zie opdracht

iteration = 0

while found < limit:

    candidate = start + (iteration * step)
    divisors = []

    for prime in primes:
        if candidate % prime == 0:
            divisors.append(prime)
            break
        else:
            continue
    
    if len(divisors) == 0:
        primes.append(candidate)
        found += 1

    iteration += 1

# print(primes)
print(primes[-1])
