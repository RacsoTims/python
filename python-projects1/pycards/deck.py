"""
Authors: M. Heineman, O. Smit

Date: 2021-05-22

Description:

Defines a deck of game cards

a deck consists of 52 cards devided into 4 suits, joker is standard excluded
"""
from card import Card
import random

class Deck:

    deck = []

    handlist = []

    def __init__(self, joker=False):
        self.joker = joker
        
        suits = ["hearts", "diamonds", "clubs", "spades"]

        for kind in suits:
            for value in range(1, 14):
                self.deck.append(Card(kind, value))

    def __str__(self):
        deck = self.deck
        return " ".join(map(str, deck))

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self, number):
        handlist = []
        
        for i in range(0, number):
            handlist.append(self.deck.pop())
        
        return handlist 

    def hand(self):
        return " ".join(map(str, self.handlist))

    def getDeck(self):
        return self.deck

    def getHand(self):
        return self.handlist

    def inHand(self):
        suits = ["hearts", "diamonds", "clubs", "spades"]
        result = []
        suit_count = {}

        for card in self.handlist:
            result.append(card.suit)

        for suit in suits:
            suit_count[suit] = result.count(suit)
        return suit_count

    def reset(self):
        self.deck.extend(self.handlist)
        self.shuffle()
        self.handlist = []
