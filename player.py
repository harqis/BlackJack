# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 19:01:06 2022

@author: Tommi
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
        self.hand.append(deck.drawCard())
        return self

    # Reset hand to empty list.
    def resetHand(self):
        self.hand = []

    # Show player's hand.
    def showHand(self):
        for card in self.hand:
            card.show()
        print("=")
        print(self.countTotal())

    # Show player's bank account.
    def showBank(self):
        return self.bank

    # Edit player's bank account.
    def editBank(self, bet):
        self.bank = self.bank + bet

    # Count card values together.
    def countTotal(self):
        total = [0,0]
        for card in self.hand:
            total[0] += card.value[0]
            total[1] += card.value[1]
            
        return total