# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 19:05:26 2022

@author: Tommi
"""

from deck import Deck

#
# Peli.
#

def BlackJackGame(player, dealer, bet):
    
    # Totuusarvo, hävisikö pelaaja.
    playerLost = False
    dealerBusted = False
    
    # Nollataan kädet.
    player.resethand()
    dealer.resethand()
    
    # Luodaan pakka ja sekoitetaan kortit.
    deck = Deck()
    deck.shuffle()
    
    # Jakaja nostaa kaksi korttia.
    dealer.draw(deck)
    dealer.draw(deck)
    
    # Pelaaja nostaa kaksi korttia.
    player.draw(deck)
    player.draw(deck)
    
    # Näytetään kortit.
    print("Jakajan käsi:")
    dealer.showhand_beginning()
    
    print("Kätesi:")
    player.showhand()

    # Jos pelaaja saa blackjackin, skipataan pelaajan vuoro.    
    playerGot21 = bool(player.count_total()[1] == 21)
    
    if playerGot21 is False:
        
        #
        # Pelaajan vuoro, jos ei blackjackia.
        #
        
        playerCont = True
        while playerCont:
            print("Haluatko nostaa (y) vai jäädä tähän (n)")
            answer = input()
            
            # Pelaaja nostaa.
            if answer == 'y':
                print("Valitsit nostaa kortin.")
                player.draw(deck)
                player.showhand()
    
                playerHandTotal = player.count_total()
                
                # Jos pelaaja bustaa, hän häviää.
                if min(playerHandTotal) > 21:
                    playerCont = False
                    print("Kätesi on yli 21. Hävisit.")
                    bet = bet - 2*bet
                    player.editbank(bet)
                    
                    playerLost = True
                 
            # Pelaaja päätti jäädä.
            else:
                playerCont = False
                print("Valitsit jäädä tähän.")
                
    else:
        print("BlackJack! Kätesi arvo on 21!")
    
    if playerLost is False:
        
        #
        # Jakajan vuoro, jos pelaaja ei bustannut.
        #
        
        print("Jakajan vuoro.")
        dealer.showhand()
        dealerHandTotal = dealer.count_total()
        
        dealerCont = True
        
        while dealerCont is True:

            if  dealerHandTotal[0] < 17 and dealerHandTotal[1] < 17:
                print("Jakajan käsi on alle 17, jakaja nostaa.")
                dealer.draw(deck)
                dealer.showhand()

                dealerHandTotal = dealer.count_total()
                
            elif  dealerHandTotal[0] < 17 and dealerHandTotal[1] > 21:
                print("Jakajan käsi on alle 17, jakaja nostaa.")
                dealer.draw(deck)
                dealer.showhand()

                dealerHandTotal = dealer.count_total()
            
            elif min(dealerHandTotal) > 21:
                print("Jakajan käsi on yli 21, jakaja bustasi. Voitit!")
                dealerCont = False
                
                dealerBusted = True
                player.editbank(bet)
            
            else:                
                dealerCont = False
                print("Jakajan käsi on yli 16, jakaja jää.")
                       
        #
        # Pelin loppuvaihe.
        # 
        
        if dealerBusted is False:
        
            dealerHandTotal = dealer.count_total()
            playerHandTotal = player.count_total()
            
            if dealerHandTotal[0] > max(playerHandTotal) or dealerHandTotal[1] > max(playerHandTotal):
                print("Kätesi on pienempi kuin jakajalla. Hävisit.")
                bet = bet - 2*bet
                player.editbank(bet)
                
            elif dealerHandTotal[0] > playerHandTotal[0] and playerHandTotal[1] > 21:
                print("Kätesi on pienempi kuin jakajalla. Hävisit.")
                bet = bet - 2*bet
                player.editbank(bet)
            
            elif dealerHandTotal[1] > playerHandTotal[0] and playerHandTotal[1] > 21:
                print("Kätesi on pienempi kuin jakajalla. Hävisit.")
                bet = bet - 2*bet
                player.editbank(bet)
            
            elif dealerHandTotal[0] == playerHandTotal[0] and playerHandTotal[1] > 21:
                print("Pelaajan ja jakajan kädet ovat yhtä arvokkaat. Tasapeli.")
            
            elif max(dealerHandTotal) == max(playerHandTotal):
                print("Pelaajan ja jakajan kädet ovat yhtä arvokkaat. Tasapeli.")
            
            elif (dealerHandTotal[0] != 21 or dealerHandTotal[1] != 21) and playerGot21 is True:
                print("Voitit Blackjackilla! Panoksesi maksetaan 2.5-kertaisena takaisin.")
                bet = 1.5 * bet
                player.editbank(bet)
            
            else:
                print("Kätesi on suurempi kuin jakajalla. Voitit!")
                player.editbank(bet)