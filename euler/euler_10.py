# URL: https://projecteuler.net/problem=10

# OPDRACHT
# Find the sum of all the primes below two million.


def generate_primes(start, end, step_size):

    primes = [2]
    for n in range(start, end, step_size):
        for prime in primes:
            if n % prime != 0:
                if prime == primes[-1]:
                    primes.append(n)
            else:
                break
    return primes


start = 3
end = 2000001
step_size = 2
primes = generate_primes(start, end, step_size)

print(len(primes), sum(primes))
