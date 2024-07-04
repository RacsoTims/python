# URL: https://projecteuler.net/problem=37

import sys
sys.path.append("/home/oscar/tools/")

import utils


def truncate_number(number):
    trunks = []
    trunks.append(number)
    text = str(number)
    for i in range(1, len(text)):
        trunk = text[0:len(text) - i]  # truncate from right to left
        trunks.append(int(trunk))

        trunk = text[i:len(text)]      # truncate from left to right
        trunks.append(int(trunk))
        
    return trunks


def check_iftruncatable(trunks, primes):
    truncatable = False
    check = [j for j in trunks if j in primes]

    if len(check) == len(trunks):
        truncatable = True
    return truncatable


start = 3
end = 1000000
step_size = 2
primes = utils.generate_primes(start, end, step_size)

su = 0
count = 0
for prime in primes:
    if prime < 10:
        continue
    else:
        check = check_iftruncatable(truncate_number(prime), primes)
        if check:
            print(f"Prime number {prime} is Truncatable")
            count += 1
            su += prime
        elif count == 11:
            break

print(su)
