# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 19:01:04 2022

@author: Tommi
"""

import random
from cards import Card, Ace

#
# Korttipakka, sisältää 4 kpl jokaista 2-9 -korttia, 16 10-korttia ja 4 ässää (1/11).
# Kortteja siis yhteensä 52 kpl.
#

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        
    def build(self):
        #for s in ["Ruutu", "Hertta", "Pata", "Risti"]:
        for i in range(4):
            self.cards.append(Ace())
            for v in range(2,11):
                self.cards.append(Card(v))
                
        for j in range(12):
            self.cards.append(Card(10))
                
    def show(self):
       for c in self.cards:
           c.show()
    
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
            
    def drawCard(self):
        return self.cards.pop()