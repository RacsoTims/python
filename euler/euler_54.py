# URL: https://projecteuler.net/problem=54

import sys
sys.path.append("/home/oscar/tools/")
import utils

wins_total = 0
path = utils.determine_path()


def get_data():
    
    hands = []
    
    with open(f"{path}euler_54.txt", "r") as data:
        for line in data:
            hands.append(line.split(" ")[0:5])
            hands.append(((line.replace("\n", "")).split(" "))[5:10])
    
    return hands


hands = get_data()
for i in range(0, len(hands), 2):
    hand1 = hands[i]
    hand2 = hands[i+1]
    if utils.play_round(hand1, hand2):
        wins_total += 1

print(wins_total)
