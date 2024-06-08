def primes(lower, upper, step):
    
    primes_list = [2]

    for i in range(lower, upper, step):
        for prime in primes_list:
            if i % prime == 0:
                break
        else:
            primes_list.append(i)
    
    return primes_list


lower = int(input("Lower bound > "))  # must be three for now
upper = int(input("Upper bound > "))
step = int(input("Step size > "))  # must be two for now

list_of_primes = primes(lower, upper, step)
print(list_of_primes)
