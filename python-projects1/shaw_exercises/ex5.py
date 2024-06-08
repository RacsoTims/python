name = 'Zad A. Shaw'
age = 35 # not a lie
height_in_inches = 74
height = round(height_in_inches * 2.54) # lengte afgerond op de hele cm
weight_in_lbs = 180
weight = round(weight_in_lbs / 2 - weight_in_lbs * 0.05, 1) # gewicht in kilo's afgerond op 1 decimaal
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} cm tall.")
print(f"He's {weight} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = round(age + height + weight)
print(f"If I add {age}, {height}, and {weight} I get {total}.")