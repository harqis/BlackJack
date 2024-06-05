# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 19:07:28 2022

"""

from player import Player
from dealer import Dealer
from game import blackjackgame


def main():
    # Welcome user
    print("Welcome to play Blackjack!")

    print("Please, enter your name:")
    player_name = input()

    print(f"Hi {player_name}! You need to make a deposit to play. How many chips do you want?")
    deposit = int(input())

    print("Thank you. Let's begin!")
    player = Player(player_name, deposit)
    dealer = Dealer()

    play = True

    while play:

        # Betting stage
        print("Please, set your bet:")
        bet = int(input())
        bank_amount = player.showbank()
        if bet > bank_amount:
            print("You don't have enough chips!")
            # play = False
            break

        # run game
        blackjackgame(player, dealer, bet)
        bank_amount = player.showbank()
        print(f"You have {bank_amount} chips left.")
        print("Play again? (y)?")
        answer = input()

        # user wants to play again
        if answer == 'y':
            if bank_amount > 0:
                print("OK! Let's deal the cards.")
                # play = True

            # not enough money on bank account
            else:
                print("You ran out of chips. Thank you for playing, come again!")
                play = False

        # user did not want to play anymore
        else:
            print("Thank you for playing!")
            print(f"You left with {bank_amount} chips.")
            play = False


if __name__ == "__main__":
    main()
