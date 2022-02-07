# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 19:05:03 2022

@author: Tommi Kivinen
"""

#
# Jakaja
#

class Dealer:

    def __init__(self):
        self.hand = []
        
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
    
    def resethand(self):
        self.hand = []
    
    def showhand_beginning(self):
        print("(Piilotettu kortti)")
        self.hand[1].show()
            
    def showhand(self):
        for card in self.hand:
            card.show()
        print("=")
        print(self.count_total())
    
    def count_total(self):
        total = [0, 0]
        for card in self.hand:
            total[0] += card.value[0]
            total[1] += card.value[1]
            
        return total