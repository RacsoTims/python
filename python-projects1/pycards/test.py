#! /usr/bin/env python3
from card import Card
from deck import Deck
from time import sleep
from os import system
import numpy as np

game = True

deck = Deck()

draws = 0

deck.shuffle()
deck.shuffle()

game_result = np.array([])

end = 100000
tries = 0

while(game):
    
    system('clear')


    #print("Draw 1 cards\n")

    deck.draw(1)
    draws += 1

    #print(f"Attempt: {draws}")

    #print(deck.hand())

#    print(deck.inHand())

    #print("Do we got five of a flush?")

    hand = deck.inHand()

    if len(hand) == 51:
        print(game_result)
        exit()

    for suit in hand:
        if hand[suit] == 5:
            #print(f"You've got a flush of {suit} in {draws} draws.")
            tries += 1
            game_result = np.append(game_result, [draws])
            deck.reset()
            draws = 0
    
    if tries == end:
        print(game_result)
        print("Mean:")
        print(game_result.mean())

        unique_elements, counts_elements = np.unique(game_result, return_counts=True)
        print("Frequency of unique values:")
        print(np.asarray((unique_elements, counts_elements)))
        exit()

    #print("Draw another card.")
    #sleep(1)
#    if game:
#        anwser = input("No, not yet. Draw another card? [Y/n]")
#        if "anwser" in globals() and anwser == "n":
#            print("Better luck next time!")
#            game = False
