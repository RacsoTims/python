# URL: https://projecteuler.net/problem=2

# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

# Fibonacci sequence, first 10 terms
sequence = [1, 2]
length = len(sequence)
limit = 100

max_term = 4000000

while length < limit:

    new_term = sum(sequence[(length - 2):length])

    if new_term <= max_term:
        sequence.append(new_term)
    else:
        break    

    length += 1

# print(sequence)
# print(len(sequence))
answer = sum([i for i in sequence if i % 2 == 0])
print(answer)
