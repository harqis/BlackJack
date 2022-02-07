# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 19:07:28 2022

@author: Tommi Kivinen
"""

from player import Player
from dealer import Dealer
from game import blackjackgame

# Welcome user
print("Tervetuloa pelaamaan BlackJackia!")

print("Syötä nimesi:")
playerName = input()
    
print(f"Moro {playerName}! Tarvitaan alkusijoitus. Paljonko pelimerkkejä laitetaan?")
startDeposit = int(input())
    
print("Kiitos! Voidaan aloittaa peli.")
player = Player(playerName, startDeposit)
dealer = Dealer()

play = True

while play:
    
    # Betting stage
    print("Aseta panos:")
    bet = int(input())
    bankSituation = player.showbank()
    if bet > bankSituation:
        print("Panoksesi on enemmän kuin mitä sinulla on tilillä.")
        play = False
        break

    blackjackgame(player, dealer, bet)
    bankSituation = player.showbank()
    print(f"Pelimerkkejä jäljellä {bankSituation}.")    
    print("Pelataanko uudelleen (y)?")
    answer = input()
    
    if answer == 'y':
        if bankSituation > 0:
            print("OK! Jaetaan kortit.")
            #play = True
        else:
            print("Pelitilisi on tyhjä, hävisit kaiken. Kasino kiittää!")
            play = False
        
    else:
        print("Kiitos pelaamisesta!")
        print(f"Pelitilillesi jäi {bankSituation} pelimerkkiä.")
        play = False
