import numpy as np

for i in range (2, 10, 1):
    for j in np.arange(0.250, 0.999, 0.001):
        if 10**j < i < 10**(j+0.001):
            k = round(j, 3)
            l = round(i - 10**j, 4)
            print(f"{i} is ongeveer gelijk aan 10^{k}. Verschil: {l}")
