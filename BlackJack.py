# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 16:56:36 2021

@author: Tommi Kivinen
github: @harqis
"""

import random

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

#
# Pelaaja
#

class Player: 
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.hand = []
        
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
    
    def resetHand(self):
        self.hand = []
    
    def showHand(self):
        for card in self.hand:
            card.show()
        print("=")
        print(self.countTotal())
            
    def showBank(self):
        return self.bank
    
    def editBank(self, bet):
        self.bank = self.bank + bet
            
    def countTotal(self):
        total = [0,0]
        for card in self.hand:
            total[0] += card.value[0]
            total[1] += card.value[1]
            
        return total

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


"""
deck = Deck()
deck.shuffle()
deck.show()
        
card = deck.drawCard()
card.show()
"""    

#
# Peli.
#

def BlackJackGame(player, dealer, bet):
    
    # Totuusarvo, hävisikö pelaaja.
    playerLost = False
    dealerBusted = False
    
    # Nollataan kädet.
    player.resetHand()
    dealer.resetHand()
    
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
    dealer.showHandBeginning()
    
    print("Kätesi:")
    player.showHand()

    # Jos pelaaja saa blackjackin, skipataan pelaajan vuoro.    
    playerGot21 = bool(player.countTotal()[1] == 21)
    
    if playerGot21 is False:
        
        #
        # Pelaajan vuoro, jos ei blackjackia.
        #
        
        playerCont = True
        while playerCont is True:
            print("Haluatko nostaa (y) vai jäädä tähän (n)")
            answer = input()
            
            # Pelaaja nostaa.
            if answer == 'y':
                print("Valitsit nostaa kortin.")
                player.draw(deck)
                player.showHand()
    
                playerHandTotal = player.countTotal()
                
                # Jos pelaaja bustaa, hän häviää.
                if min(playerHandTotal) > 21:
                    playerCont = False
                    print("Kätesi on yli 21. Hävisit.")
                    bet = bet - 2*bet
                    player.editBank(bet)
                    
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
        dealer.showHand()
        dealerHandTotal = dealer.countTotal()
        
        dealerCont = True
        
        while dealerCont is True:

            if  dealerHandTotal[0] < 17 and dealerHandTotal[1] < 17:
                print("Jakajan käsi on alle 17, jakaja nostaa.")
                dealer.draw(deck)
                dealer.showHand()

                dealerHandTotal = dealer.countTotal()
                
            elif  dealerHandTotal[0] < 17 and dealerHandTotal[1] > 21:
                print("Jakajan käsi on alle 17, jakaja nostaa.")
                dealer.draw(deck)
                dealer.showHand()

                dealerHandTotal = dealer.countTotal()
            
            elif min(dealerHandTotal) > 21:
                print("Jakajan käsi on yli 21, jakaja bustasi. Voitit!")
                dealerCont = False
                
                dealerBusted = True
                player.editBank(bet)
            
            else:                
                dealerCont = False
                print("Jakajan käsi on yli 16, jakaja jää.")
                       
        #
        # Pelin loppuvaihe.
        # 
        
        if dealerBusted is False:
        
            dealerHandTotal = dealer.countTotal()
            playerHandTotal = player.countTotal()            
            
            if dealerHandTotal[0] > max(playerHandTotal) or dealerHandTotal[1] > max(playerHandTotal):
                print("Kätesi on pienempi kuin jakajalla. Hävisit.")
                bet = bet - 2*bet
                player.editBank(bet)
                
            elif dealerHandTotal[0] > playerHandTotal[0] and playerHandTotal[1] > 21:
                print("Kätesi on pienempi kuin jakajalla. Hävisit.")
                bet = bet - 2*bet
                player.editBank(bet)
            
            elif dealerHandTotal[1] > playerHandTotal[0] and playerHandTotal[1] > 21:
                print("Kätesi on pienempi kuin jakajalla. Hävisit.")
                bet = bet - 2*bet
                player.editBank(bet)
            
            elif dealerHandTotal[0] == playerHandTotal[0] and playerHandTotal[1] > 21:
                print("Pelaajan ja jakajan kädet ovat yhtä arvokkaat. Tasapeli.")
            
            elif max(dealerHandTotal) == max(playerHandTotal):
                print("Pelaajan ja jakajan kädet ovat yhtä arvokkaat. Tasapeli.")
            
            elif (dealerHandTotal[0] != 21 or dealerHandTotal[1] != 21) and playerGot21 is True:
                print("Voitit Blackjackilla! Panoksesi maksetaan 2.5-kertaisena takaisin.")
                bet = 1.5 * bet
                player.editBank(bet)    
            
            else:
                print("Kätesi on suurempi kuin jakajalla. Voitit!")
                player.editBank(bet)
        
        

# Tervehditään käyttäjää ja aloitetaan peli,
# jos käyttäjä niin haluaa.
print("Tervetuloa pelaamaan BlackJackia!")

print("Syötä nimesi:")
playerName = input()
    
print(f"Moro {playerName}! Tarvitaan alkusijoitus. Paljonko pelimerkkejä laitetaan?")
startDeposit = int(input())
    
print("Kiitos! Voidaan aloittaa peli.")
player = Player(playerName, startDeposit)
dealer = Dealer()

play = True

while play is True:
    
    # Panostus.
    print("Aseta panos:")
    bet = int(input())
    bankSituation = player.showBank()
    if bet > bankSituation:
        print("Panoksesi on enemmän kuin mitä sinulla on tilillä.")
        play = False
        break
    
    BlackJackGame(player, dealer, bet)
    bankSituation = player.showBank()
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
