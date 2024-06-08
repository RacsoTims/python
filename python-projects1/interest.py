from math import e

def interest(start, rate):
    return start*pow(1+rate, 1/rate)

for x in range (10310, 10311):
    if (interest(100, 1/x)-100*e <= -0.013):
        print("You have found the (almost) optimal rate of interest! At:")
        print(str(1/x*100)+" %"+" every "+str(525600/x)+" minutes.")
        break
    print(interest(100, 1/x), x, interest(100, 1/x)-100*e)