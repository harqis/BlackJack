# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 19:05:26 2022

@author: Tommi Kivinen
"""

from deck import Deck


#
# Peli.
#

def blackjackgame(player, dealer, bet):
    # Did player lose?
    playerlost = False
    dealerbusted = False

    # Reset hands
    player.resethand()
    dealer.resethand()

    # Create deck and shuffle it
    deck = Deck()
    deck.shuffle()

    # Dealer draws two
    dealer.draw(deck)
    dealer.draw(deck)

    # Player draws two
    player.draw(deck)
    player.draw(deck)

    # Show hands
    print("Jakajan käsi:")
    dealer.showhand_beginning()

    print("Kätesi:")
    player.showhand()

    # If player gets 21, skip turn
    playergot21 = bool(player.count_total()[1] == 21)

    if playergot21 is False:

        #
        # Player's turn (if no 21)
        #

        player_continues = True
        while player_continues:
            print("Haluatko nostaa (y) vai jäädä tähän (n)")
            answer = input()

            # Player draws
            if answer == 'y':
                print("Valitsit nostaa kortin.")
                player.draw(deck)
                player.showhand()

                playerhand_total = player.count_total()

                # If over 21, player busts and loses
                if min(playerhand_total) > 21:
                    player_continues = False
                    print("Kätesi on yli 21. Hävisit.")
                    bet = bet - 2 * bet
                    player.editbank(bet)

                    playerlost = True

            # decided to stay
            else:
                player_continues = False
                print("Valitsit jäädä tähän.")

    else:
        print("BlackJack! Kätesi arvo on 21!")

    if playerlost is False:

        #
        # Dealer's turn
        #

        print("Jakajan vuoro.")
        dealer.showhand()
        dealerhand_total = dealer.count_total()

        dealer_continues = True

        while dealer_continues is True:

            if dealerhand_total[0] < 17 and dealerhand_total[1] < 17:
                print("Jakajan käsi on alle 17, jakaja nostaa.")
                dealer.draw(deck)
                dealer.showhand()

                dealerhand_total = dealer.count_total()

            elif dealerhand_total[0] < 17 and dealerhand_total[1] > 21:
                print("Jakajan käsi on alle 17, jakaja nostaa.")
                dealer.draw(deck)
                dealer.showhand()

                dealerhand_total = dealer.count_total()

            elif min(dealerhand_total) > 21:
                print("Jakajan käsi on yli 21, jakaja bustasi. Voitit!")
                dealer_continues = False

                dealerbusted = True
                player.editbank(bet)

            else:
                dealer_continues = False
                print("Jakajan käsi on yli 16, jakaja jää.")

        #
        # Endgame, decide who won
        # 

        if dealerbusted is False:

            dealerhand_total = dealer.count_total()
            playerhand_total = player.count_total()

            if dealerhand_total[0] > max(playerhand_total) or dealerhand_total[1] > max(playerhand_total):
                print("Kätesi on pienempi kuin jakajalla. Hävisit.")
                bet = bet - 2 * bet
                player.editbank(bet)

            elif dealerhand_total[0] > playerhand_total[0] and playerhand_total[1] > 21:
                print("Kätesi on pienempi kuin jakajalla. Hävisit.")
                bet = bet - 2 * bet
                player.editbank(bet)

            elif dealerhand_total[1] > playerhand_total[0] and playerhand_total[1] > 21:
                print("Kätesi on pienempi kuin jakajalla. Hävisit.")
                bet = bet - 2 * bet
                player.editbank(bet)

            elif dealerhand_total[0] == playerhand_total[0] and playerhand_total[1] > 21:
                print("Pelaajan ja jakajan kädet ovat yhtä arvokkaat. Tasapeli.")

            elif max(dealerhand_total) == max(playerhand_total):
                print("Pelaajan ja jakajan kädet ovat yhtä arvokkaat. Tasapeli.")

            elif (dealerhand_total[0] != 21 or dealerhand_total[1] != 21) and playergot21 is True:
                print("Voitit Blackjackilla! Panoksesi maksetaan 2.5-kertaisena takaisin.")
                bet = 1.5 * bet
                player.editbank(bet)

            else:
                print("Kätesi on suurempi kuin jakajalla. Voitit!")
                player.editbank(bet)
