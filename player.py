from deck_of_cards import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def display_hand(self):
        print(f"{self.name}'s hand:")
        cards = {
        "1": "Ace",
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "11": "Jack",
        "12": "Queen",
        "13": "King",
        }

        for i in range(len(self.hand)):
            print(str(i + 1) + '. ' + str(cards[str(self.hand[i].value)]) + " of " + self.hand[i].suit)

#player = Player("name")
#card1 = Card("hearts", 1)
#card2 = Card("clubs", 2)

#player.hand.append(card1)
#player.hand.append(card2)
#player.display_hand()
