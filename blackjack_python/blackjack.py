import objects
from objects import *

valueRef = objects.values
numPlayers = 0

class Blackjack:

    def __init__(self, player1='player1', player2='player2'):
        self.player1 = player1
        self.player2 = player2
        self.p1 = [] 
        self.p2 = []

    # 1 turn blackjack
    def play(self):

        self.p1 = [] 
        self.p2 = []

        # dealing phase
        deck = Deck()
        deck.shuffle()

        print('Dealer is dealing 2 cards to ', self.player1)
        print('Dealer is dealing 2 cards to ', self.player2)

        self.p1.append(deck.deal())
        self.p1.append(deck.deal())

        self.p2.append(deck.deal())
        self.p2.append(deck.deal())

        # player 1's turn
        print(self.player1 + "'s turn...")

        while True:
            choice = input("Type 'h' for hit, 's' for stand: ")
            if choice == 'h': 
                self.p1.append(deck.deal())
                break
            elif choice == 's': break
            else: print("Please enter valid input")

        # player 2's turn
        print(self.player2 + "'s turn...")

        while True:
            choice = input("Type 'h' for hit, 's' for stand: ")
            if choice == 'h': 
                self.p2.append(deck.deal())
                break
            elif choice == 's': break
            else: print("Please enter valid input")
        
        # calculate the total card value for player 1
        handval1 = 0
        for i in self.p1:
            cardval = str(i).split()[0]
            print(cardval)
            handval1 += objects.values.get(cardval)

        # calculation phase
        handval2 = 0
        for i in self.p2:
            cardval = str(i).split()[0]
            print(cardval)
            handval2 += objects.values.get(cardval)
        
        print("\n", self.player1, "'s hand: ")
        for i in self.p1: print(str(i), "\n")
        print("\n", self.player2, "'s hand: ")
        for i in self.p2: print(str(i), "\n")

        print(self.player1, "'s hand value is ", handval1)
        print(self.player2, "'s hand value is ", handval2)

        # game deciding phase

        if handval1 > 21: print(self.player1, " has bust out... card value over 21.")
        elif handval2 > 21: print(self.player2, " has bust out... card value over 21.")
        elif handval1 > handval2: print(self.player1, " has won the game.")
        elif handval2 > handval1: print(self.player2, " has won the game.")
        else: print("The game has ended in a draw.")


