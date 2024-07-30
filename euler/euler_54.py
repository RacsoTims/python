# URL: https://projecteuler.net/problem=54

import sys
sys.path.append("/home/oscar/tools/")
import utils

hand = ["4C", "TH", "KC", "AC", "4D"]
hand1 = ["8C", "7H", "6C", "5C", "4C"]
hand2 = ["AC", "4H", "3C", "2C", "5C"]
hand3 = ["AC", "TH", "TC", "TD", "TS"]
# print(hand.count("C"))
# print(utils.sort_bySuit(hand))
# print(utils.check_ifFlush(hand))
# print(utils.sort_byValue(hand))
# print(utils.straight(hand2))
# print(utils.highest_straight(hand))
# print(utils.three_of_a_kind(hand3))
print(utils.sort_byValue(hand))
print(utils.sort_bySuit(hand))
