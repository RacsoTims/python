cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car # how many people can be transported today?
average_passengers_per_car = passengers / cars_driven # how to divide the passengers among the cars, all else being equal.


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, " people in each car.")

if average_passengers_per_car > space_in_a_car:
    print("We don't have enough spaces for today.")
else:
    print("We're go to go!")
