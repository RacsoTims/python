people = 30
cars = 40
trucks = 15


if cars > people: # iff the expression following 'if' is true, then the block of code under it is executed
    print("We should take the cars.")
elif cars < people: # iff the expression following "elif" is true, then it will print the line below
    print("We should not take the cars.")
else: # if, and only if, the above expressions are both false does this piece of code go into effect, i.e., when there are exactly as many cars as people.
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")