# dit script berekent de faculteit van een getal

solution = 1
print("Ik bereken voor jou de faculteit van een getal! Vul hieronder een (geheel) positief getal in.")
x = int(input("> "))
for i in range (2, x+1):
    solution *= i
    # print(solution)

print(f"Antwoord: {solution}.")
