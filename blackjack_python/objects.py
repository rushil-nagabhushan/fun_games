import random

suits = ('Spades','Clubs','Hearts','Diamonds')
numbers = ('Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __str__(self):
        return self.number + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for number in numbers:
                self.deck.append(Card(suit,number))

    def __str__(self):
        deck_list = '' 
        for card in self.deck:
            deck_list += '\n' + card.__str__()
        return 'Deck contains cards: ' + deck_list

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        print(single_card)
        print("Cards left in deck: ", len(self.deck))
        return single_card