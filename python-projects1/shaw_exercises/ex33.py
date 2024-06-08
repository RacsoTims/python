"""
i = 0
numbers = []
while i < 6:
    print(f"At the top i is {i}.")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}.")


print("The numbers: ")

for num in numbers:
    print(num)
"""
numbers = []
count = 20
step = 5
def counting(number, numbers, step):
        i = 0
        while i < number:
            print(f"At the top i is {i}.")
            numbers.append(i)

            print("Numbers now: ", numbers)
            i += step
            print(f"At the bottom i is {i}.")
        return numbers    

set = counting(count, numbers, step)

print("The numbers: ")
for num in set:
    print(num)
