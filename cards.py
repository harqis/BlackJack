# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 19:01:03 2022

@author: Tommi
"""

#
# Kortti, arvoltaan 2-10
#

class Card:
    def __init__(self, val):
        #self.suit = suit
        self.value = [val, val]
        
    def show(self):
        print(self.value[0])
        
#
# Ässä. Erikoistapaus, on arvoltaan 1 tai 11
#

class Ace:
    def __init__(self):
        self.value = [1,11]
        
    def show(self):
        print(f"{self.value[0]} / {self.value[1]}")