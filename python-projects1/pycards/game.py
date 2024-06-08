"""
Authors: M. Heineman, O. Smit

Date: 2021-05-28

Description:

Defines a game cards

"""
import deck
from player import Player


class Game:

    def __init__(self, player=1, start=7):

        self.player = player

        self.deck = deck.Deck()

        self.deck.shuffle()

        for i in range(0, player):
            self.players[i] = Player(self.deck.draw(start))

    def __str__(self):
        return " "+self.deck+"\n\n"+" ".join(map(str, self.players))