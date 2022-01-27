# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 19:05:03 2022

@author: Tommi
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
    
    def resetHand(self):
        self.hand = []
    
    def showHandBeginning(self):
        print("(Piilotettu kortti)")
        self.hand[1].show()
            
    def showHand(self):
        for card in self.hand:
            card.show()
        print("=")
        print(self.countTotal())
    
    def countTotal(self):
        total = [0,0]
        for card in self.hand:
            total[0] += card.value[0]
            total[1] += card.value[1]
            
        return total