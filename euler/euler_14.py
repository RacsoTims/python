# URL: https://projecteuler.net/problem=14

# OPDRACHT
# Which starting number, under one million, produces the [Collatz] longest chain?

def collatz_chain(number):
    chain = []
    chain.append(number)

    while number > 1:

        if number % 2 == 0:
            next_term = number // 2
        else:
            next_term = number * 3 + 1

        chain.append(next_term)
        number = next_term

    return chain

chains = [[1]]
upper_bound = 1000000 # zie opdracht
for x in range(2, upper_bound):
    result = collatz_chain(x)
    if len(result) > len(chains[0]):
        chains[0] = result
        # print(chains[0])
    else:
        continue

longest = chains[0]
print(longest, len(longest), longest[0])
