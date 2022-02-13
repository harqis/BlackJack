# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 19:07:28 2022

@author: Tommi Kivinen
"""

from player import Player
from dealer import Dealer
from game import blackjackgame


def main():
    # Welcome user
    print("Tervetuloa pelaamaan BlackJackia!")

    print("Syötä nimesi:")
    player_name = input()

    print(f"Moro {player_name}! Tarvitaan alkusijoitus. Paljonko pelimerkkejä laitetaan?")
    deposit = int(input())

    print("Kiitos! Voidaan aloittaa peli.")
    player = Player(player_name, deposit)
    dealer = Dealer()

    play = True

    while play:

        # Betting stage
        print("Aseta panos:")
        bet = int(input())
        bank_amount = player.showbank()
        if bet > bank_amount:
            print("Panoksesi on enemmän kuin mitä sinulla on tilillä.")
            # play = False
            break

        # run game
        blackjackgame(player, dealer, bet)
        bank_amount = player.showbank()
        print(f"Pelimerkkejä jäljellä {bank_amount}.")
        print("Pelataanko uudelleen (y)?")
        answer = input()

        # user wants to play again
        if answer == 'y':
            if bank_amount > 0:
                print("OK! Jaetaan kortit.")
                # play = True

            # not enough money on bank account
            else:
                print("Pelitilisi on tyhjä, hävisit kaiken. Kasino kiittää!")
                play = False

        # user did not want to play anymore
        else:
            print("Kiitos pelaamisesta!")
            print(f"Pelitilillesi jäi {bank_amount} pelimerkkiä.")
            play = False


if __name__ == "__main__":
    main()
