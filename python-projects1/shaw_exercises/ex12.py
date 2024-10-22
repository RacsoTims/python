age = input("How old are you? ")
height = float(input("How tall are you (m)? "))
weight = float(input ("How much do you weigh (kg)? "))
bmi = weight / (height* height)

print(f"So, you are {age} years old, {height} meters tall and {weight} kg's heavy.")
print(f"Your bmi is {bmi}.")
