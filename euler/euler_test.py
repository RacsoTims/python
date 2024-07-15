# For test purposes

import sys
sys.path.append("/home/oscar/tools/")

import utils

primes = utils.get_primes(including = 3000)
print(primes.index(2969))
