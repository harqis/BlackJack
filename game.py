# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 19:05:26 2022

@author: Tommi Kivinen
"""

from deck import Deck


def blackjackgame(player, dealer, bet):
    """
    Game logic function
    :param player: player
    :param dealer: dealer against player
    :param bet: bet decided by player
    """
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
    print("Dealer's hand:")
    dealer.showhand_beginning()

    print("Your hand:")
    player.showhand()

    # If player gets 21, skip turn
    playergot21 = bool(player.count_total()[1] == 21)

    if playergot21 is False:

        #
        # Player's turn (if no 21)
        #

        player_continues = True
        while player_continues:
            print("Hit (y) or stay (n) ?")
            answer = input()

            # Player draws
            if answer == 'y':
                print("You chose to hit.")
                player.draw(deck)
                player.showhand()

                playerhand_total = player.count_total()

                # If over 21, player busts and loses
                if min(playerhand_total) > 21:
                    player_continues = False
                    print("Your hand is over 21. You lost.")
                    bet = bet - 2 * bet
                    player.editbank(bet)

                    playerlost = True

            # decided to stay
            else:
                player_continues = False
                print("You chose to stay.")

    else:
        print("Blackjack! Your hand is 21!")

    if playerlost is False:

        #
        # Dealer's turn
        #

        print("Dealer's turn.")
        dealer.showhand()
        dealerhand_total = dealer.count_total()

        dealer_continues = True

        while dealer_continues:

            if dealerhand_total[0] < 17 and dealerhand_total[1] < 17:
                print("Dealer's hand is under 17, dealer hits.")
                dealer.draw(deck)
                dealer.showhand()

                dealerhand_total = dealer.count_total()

            elif dealerhand_total[0] < 17 and dealerhand_total[1] > 21:
                print("Dealer's hand is under 17, dealer hits.")
                dealer.draw(deck)
                dealer.showhand()

                dealerhand_total = dealer.count_total()

            elif min(dealerhand_total) > 21:
                print("Dealer's hand is over 21, dealer busted. You won!")
                dealer_continues = False

                dealerbusted = True
                player.editbank(bet)

            else:
                dealer_continues = False
                print("Dealer's hand is over 16, dealer stays.")

        #
        # Endgame, decide who won
        # 

        if dealerbusted is False:

            # get best counts of hands under 22
            dealer_bestcount = max(i for i in dealer.count_total() if i <= 21)
            player_bestcount = max(i for i in player.count_total() if i <= 21)

            # player won
            if player_bestcount > dealer_bestcount:

                # blackjack win
                if player_bestcount == 21:
                    print("You won with Blackjack! You've been paid 2.5 : 1.")
                    bet = 1.5 * bet
                    player.editbank(bet)

                # normal win
                else:
                    print("Your hand is more valuable than dealer's. You won!")
                    player.editbank(bet)

            # player lost
            elif player_bestcount < dealer_bestcount:
                print("Your hand is less valuable than dealer's. You lost.")
                bet = bet - 2 * bet
                player.editbank(bet)

            # draw
            else:
                print("Player's and dealer's hands are equal. Draw.")
