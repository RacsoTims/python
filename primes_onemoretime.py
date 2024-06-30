# Prime number generator

primes = [2]

def generate_primes(start, end, step_size):

    for n in range(start, end, step_size):
        for prime in primes:
            if n % prime != 0:
                if prime == primes[-1]:
                    primes.append(n)
            else:
                break
    return primes


start = 3
end = 1000
step_size = 2

result = generate_primes(start, end, step_size)
print(result)
