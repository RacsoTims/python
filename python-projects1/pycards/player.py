"""
Authors: M. Heineman, O. Smit

Date: 2021-05-28

Description:

Defines a game cards

"""
from card import Card
from random import randint

class Player:

    def __init__(self, cards):
        
        self.handlist = cards
        self.score = 0
        namelist = [randint(65,91) for element in range(0, randint(3,8))]
        self.name = "".join(map(chr, namelist))


    def __str__(self):
        return self.name

    def hand(self):
        return " ".join(map(str, self.handlist))

    def getScore(self):
        return str(self.score)

    def setScore(self, score):
        self.score = score
        return True

    def addScore(self, points):
        self.score += points
        return True