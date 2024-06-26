# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 19:01:06 2022


"""


#
# Player class
#

class Player:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.hand = []

    # Draw a card.
    def draw(self, deck):
        self.hand.append(deck.drawcard())
        return self

    # Reset hand to empty list.
    def resethand(self):
        self.hand = []

    # Show player's hand.
    def showhand(self):
        for card in self.hand:
            card.show()
        print("=")

        count = self.count_total()
        if count[0] == count[1]:
            print(count[0])

        else:
            print(self.count_total())

    # Show player's bank account.
    def showbank(self):
        return self.bank

    # Edit player's bank account.
    def editbank(self, bet):
        self.bank = self.bank + bet

    # Count card values together.
    def count_total(self):
        total = [0, 0]
        for card in self.hand:
            total[0] += card.value[0]
            total[1] += card.value[1]

        return total
