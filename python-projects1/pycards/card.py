"""
Authors: M. Heineman, O. Smit

Date: 2021-05-22

Description:

Defines a card in a game of cards

"""

class Card:

    def __init__(self, suit, value, show=True):

        if (suit in ["hearts", "diamonds", "clubs", "spades"]):

            self.suit = suit
            self.value = value
            self.show = show
	
        if self.suit == "spades":
            self.suit_val=127136
        elif self.suit == "hearts":
            self.suit_val=127152
        elif self.suit == "diamonds":
            self.suit_val=127168
        elif self.suit == "clubs":
            self.suit_val=127184

    def __str__(self):
        return chr(self.suit_val+self.value) if self.show else chr(127136)
        
    def suit(self):
        return str(self.suit)

    def value(self):
        return str(self.value)