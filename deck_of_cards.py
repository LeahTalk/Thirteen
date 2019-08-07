import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return str(self.value) + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []

    def build_deck(self):
        suits = ['hearts', 'clubs', 'spades', 'diamonds']
        values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        for suit in suits:
            for value in values:
                self.deck.append(Card(suit, value))
    
    def shuffle(self):
        for i in range(52):
            randomIndex = round(random.random() * (51 - i) + i)
            self.deck[i], self.deck[randomIndex] = self.deck[randomIndex], self.deck[i]

#d1 = Deck()
#d1.build_deck()
#d1.shuffle()
#for card in d1.deck:
    #print(str(card.value) + card.suit)
    
