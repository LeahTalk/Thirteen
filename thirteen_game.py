from deck_of_cards import Deck
from deck_of_cards import Card
from player import Player

class Thirteen_Game:
    def __init__ (self):
        self.players = []
        self.deck = Deck()
        self.cur_condition = "free_for_all"
        self.skip_count = 0
        self.conditions = {
            "single" : self.checkSingle,
            "double" : self.checkDouble,
            "triple" : self.checkTriple,
            "quad" : self.checkQuad,
            "straight" : self.checkStraight,
            "free_for_all" : 1
        }
        self.turn_count = 0
    
    def add_player(self, player_name = 'Default Player'):
        player_name = input("What is your name, player? ")
        print (f"Player, {player_name} has joined the game")
        self.players.append(Player(player_name))

    def find_first_player(self):
        for i in range(len(self.players)):
            for card in self.players[i].hand:
                if (card.value == 3) and (card.suit == "spades"):
                    return i
        return 0  

    def find_next_player(self, current_player):
        if current_player == 3:
            return 0
        return current_player + 1

##Change value and add dictionary for best values
    def isGreaterThan(self, chosen_cards, last_cards_played):
        card_values = {
            "3":0,
            "4":1,
            "5":2,
            "6":3,
            "7":4,
            "8":5,
            "9":6,
            "10":7,
            "11":8,
            "12":9,
            "13":10,
            "1":11,
            "2":12
        }
        
        for x in range(0, len(chosen_cards[0]), 1):
            if card_values[str(chosen_cards[0][x].value)] < card_values[str(last_cards_played[x].value)]:
                return False
        return True

    def check_equality(self, chosen_cards):
        cur_card_value = chosen_cards[0][0].value
        for x in range(1, len(chosen_cards[0])):
            if chosen_cards[0][x].value != cur_card_value:
                return False
            cur_card_value = chosen_cards[0][x].value
        return True
    
    def checkSingle(self, chosen_cards, last_cards_played):
        if len(last_cards_played) == 0:
            if len(chosen_cards[0]) == 1:
                return True
            return False
        if len(chosen_cards[0]) == 1 and self.isGreaterThan(chosen_cards, last_cards_played):
            return True
        return False

    def checkDouble(self, chosen_cards, last_cards_played):
        if len(last_cards_played) == 0:
            if (len(chosen_cards[0]) == 2) and self.check_equality(chosen_cards):
                return True
            return False
        if (len(chosen_cards[0]) == 2) and self.check_equality(chosen_cards) and self.isGreaterThan(chosen_cards, last_cards_played):
            return True
        return False

    def checkTriple(self, chosen_cards, last_cards_played):
        if len(last_cards_played) == 0:
            if (len(chosen_cards[0]) == 3) and self.check_equality(chosen_cards):
                return True
            return False
        if (len(chosen_cards[0]) == 3) and self.check_equality(chosen_cards) and self.isGreaterThan(chosen_cards, last_cards_played):
            return True
        return False

    def checkQuad(self, chosen_cards, last_cards_played):
        if len(last_cards_played) == 0:
            if (len(chosen_cards[0]) == 4) and self.check_equality(chosen_cards):
                return True
            return False
        if (len(chosen_cards[0]) == 4) and self.check_equality(chosen_cards) and self.isGreaterThan(chosen_cards, last_cards_played):
            return True
        return False

    def checkStraight(self, chosen_cards, last_cards_played):
        if len(chosen_cards) == len(last_played):
            return True
        else:
            return False

    def deal(self):
        card_index = 0
        player_index = 0
        while card_index < 52:
            if(player_index > 3):
                player_index = 0
            self.players[player_index].hand.append(self.deck.deck[card_index])
            player_index += 1
            card_index += 1
            
    #Need to remove -1 whatever is in chosen cards
    def removeChosenCards(self, cur_player, chosen_cards):
        chosen_cards.sort(reverse=True)
        for char in chosen_cards:
            self.players[cur_player].hand.pop(int(char) - 1)
    
    def choose_new_condition(self, the_condition = 'Not valid'):
        the_condition = input("Choose a condition for your move, single, double, triple, four, or straight: ")
        while the_condition != 'single' and the_condition != 'double' and the_condition != 'triple' and the_condition != 'four' and the_condition != 'straight':
            print("Sorry, please choose a valid condition")
            the_condition = input("Choose a condition for your move, single, double, triple, four, or straight: ")
        print (f"You are playing the {the_condition} condition.")
        return the_condition

    def check_three_of_spades(self, cur_player, listed_cards):
        print(listed_cards)
        for index in listed_cards:
            card = self.players[cur_player].hand[int(index) - 1]
            print(listed_cards)
            print(card.value)
            print(card.suit)
            if (card.value == 3) and (card.suit == "spades"):
                self.turn_count += 1
                return True
        return False

    def chooseCards(self, cur_player, the_cards="Not valid"):
        testlist = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
        the_cards = input("Choose your cards or skip: ")
        if the_cards == 'skip':
            if self.turn_count == 0:
                while the_cards == 'skip':
                    print("You cannot skip on the first turn!")
                    the_cards = ''
                    the_cards = input("Choose your cards or skip: ")
            else:
                return 'skip'
        listed_cards = the_cards.split(',')
        if self.turn_count == 0:
            while(not self.check_three_of_spades(cur_player, listed_cards)):
                print("You must play the three of spades on the first turn!")
                the_cards = ''
                the_cards = input("Choose your cards or skip: ")
                listed_cards = the_cards.split(',')
        for char in listed_cards:
            if char in testlist:
                print(f"You are playing: {listed_cards}")
                listed_card_objects = []
                for char in listed_cards:
                    listed_card_objects.append(self.players[cur_player].hand[int(char) - 1])
                return [listed_card_objects, listed_cards]
        
    def display_last_cards_played(self, last_cards_played):
        print("")
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
            "13": "King"
        }
        if len(last_cards_played) != 0:
            print("Last cards played: ")
            for card in last_cards_played:
                print(str(cards[str(card.value)]) + " of " + card.suit)
        print("")
    
    def playerTurn(self, cur_player, last_cards_played):
        valid = False
        chosen_cards = []
        self.display_last_cards_played(last_cards_played)
        print("")
        self.players[cur_player].display_hand()
        print("")
        if self.cur_condition == "free_for_all":
            self.cur_condition = self.choose_new_condition()
        while(not valid):
            chosen_cards = self.chooseCards(cur_player)
            if chosen_cards == "skip":
                self.skip_count += 1
                return last_cards_played
            valid = self.checkValidity(chosen_cards, last_cards_played)
            if(not valid):
                print("Your cards do not match the pattern, or your card is too low")
        self.skip_count = 0 
        new_last_cards = []
        self.removeChosenCards(cur_player, chosen_cards[1])
        return chosen_cards[0]
        
    def checkValidity(self, chosen_cards, last_cards_played):
        return self.conditions[self.cur_condition](chosen_cards, last_cards_played)

    def displayWinner(self):
        for player in self.players:
            if(len(player.hand) == 0):
                print(player.name + " won!")

    def checkWinner(self):
        for player in self.players:
            if(len(player.hand) == 0):
                return True
        return False

    def play_game(self):

        self.deck.build_deck()
        self.deck.shuffle()
        #different patterns user can play
        #suit hierarchy 
        suit_values = {
            "spades" : 0,
            "clubs" : 1,
            "diamonds" : 2,
            "hearts" : 3
        }
        #initial variables
        last_cards_played = []
        cur_player = 0
        for i in range(4):
            self.add_player()
        self.deal()
        cur_player = self.find_first_player()
        while(not self.checkWinner()):
            if self.skip_count == 3:
                self.cur_condition = "free_for_all"
                self.skip_count = 0
                last_cards_played = []
            last_cards_played = self.playerTurn(cur_player, last_cards_played)
            cur_player = self.find_next_player(cur_player)
        self.displayWinner()
            
testclass = Thirteen_Game()
testclass.play_game()

