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
            "four" : self.checkQuad,
            "straight" : self.checkStraight,
            "free_for_all" : 1
        }
        self.turn_count = 0
        self.winners = []
    
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
        if current_player == len(self.players) - 1:
            return 0
        return current_player + 1

##Change value and add dictionary for best values
    def isGreaterThan(self, chosen_cards, last_cards_played, condition=''):
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
        ###
        #NOTE: If user does not enter straight in chronological order (e.g. 4,8,5,3,7,6) this will break the program.
        #      Consider sorting the arrays somewhere, possibly before we enter this function? Same with check_straight
        ###
        #adding to check last value when we are checking for straits
        if condition == 'straight':
            if card_values[str(chosen_cards[0][len(chosen_cards[0])-1].value)] < card_values[str(last_cards_played[len(last_cards_played)-1].value)]:
                return False
            elif card_values[str(chosen_cards[0][len(chosen_cards[0])-1].value)] == card_values[str(last_cards_played[len(last_cards_played)-1].value)]:
                return self.compareSuit([chosen_cards[0][len(chosen_cards[0])-1]], [last_cards_played[len(last_cards_played)-1]])
            else:
                return True
        #end of addittion:
        if card_values[str(chosen_cards[0][0].value)] < card_values[str(last_cards_played[0].value)]:
            return False
        if card_values[str(chosen_cards[0][0].value)] == card_values[str(last_cards_played[0].value)]:
            return self.compareSuit(chosen_cards[0], last_cards_played)
        return True

    def compareSuit(self, chosen_cards, last_cards_played):
        suit_values = {
            "spades" : 0,
            "clubs" : 1,
            "diamonds" : 2,
            "hearts" : 3
        }
        chosen_cards_suits = []
        last_cards_played_suits = []
        for card in chosen_cards:
            chosen_cards_suits.append(suit_values[card.suit])
        for card in last_cards_played:
            last_cards_played_suits.append(suit_values[card.suit])
        return max(chosen_cards_suits) > max(last_cards_played_suits)
        

    def check_equality(self, chosen_cards):
        cur_card_value = chosen_cards[0][0].value
        for x in range(1, len(chosen_cards[0])):
            if chosen_cards[0][x].value != cur_card_value:
                return False
            cur_card_value = chosen_cards[0][x].value
        return True

    def is_strait_correct(self, chosen_cards):
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
        print("Wow! A straight has been played!")
        hold_length = len(chosen_cards[0])
        for x in range(0,hold_length-1,1):
            if card_values[str(chosen_cards[0][x].value)] + 1 != card_values[str(chosen_cards[0][x+1].value)]:
                print("Is not correct straight")
                return False
        return True

    def check_three_consecutive_pairs(self, chosen_cards):
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
        hold_length = len(chosen_cards)
        if hold_length != 6:
            return False
        #Make sure that we have three pairs
        for x in range(0,hold_length-1,2):
            if card_values[str(chosen_cards[x].value)] != card_values[str(chosen_cards[x+1].value)]:
                return False
        #Make sure that the pairs are consecutive
        if ((card_values[str(chosen_cards[0].value)] + 1) != (card_values[str(chosen_cards[2].value)]) or
            (card_values[str(chosen_cards[2].value)] + 1) != (card_values[str(chosen_cards[4].value)])):
                return False
        return True

    def checkBomb(self, chosen_cards, last_cards_played):
        #Return false if user tries to play bomb on a card other than 2
        if last_cards_played[0].value != 2:
            return False
        #Check if bomb is four of a king
        if (len(chosen_cards[0]) == 4) and (self.checkEquality(chosen_cards)):
            return True
        if self.check_three_consecutive_pairs(chosen_cards[0]):
            return True
        return False
        
    def checkSingle(self, chosen_cards, last_cards_played):
        if len(last_cards_played) == 0:
            if len(chosen_cards[0]) == 1:
                return True
            return False
        if len(chosen_cards[0]) == 1 and self.isGreaterThan(chosen_cards, last_cards_played):
            return True
        if len(chosen_cards[0]) > 1:
            return self.checkBomb(chosen_cards, last_cards_played)
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
        condition = 'straight'
        if len(last_cards_played) == 0:
            if (len(chosen_cards[0]) >= 3) and self.is_strait_correct(chosen_cards):
                return True
            return False
        if (len(chosen_cards[0]) == len(last_cards_played)) and self.is_strait_correct(chosen_cards) and self.isGreaterThan(chosen_cards, last_cards_played, condition):
            return True
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
        chosen_cards = list(map(int, chosen_cards))
        chosen_cards.sort(reverse=True)
        print(f"The player has removed these cards {chosen_cards}")
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

    def displayWinners(self):
        winPhrase = {
            "0": "1st",
            "1": "2nd",
            "2": "3rd",
            "3": "4th"
        }
        print("Final Rankings:")
        for i in range(len(self.winners)):
            print(f"{winPhrase[str(i)]} place: {self.winners[i].name}")

    def checkWinner(self):
        for player in self.players:
            if(len(player.hand) == 0):
                print(f"{player.name} is out of cards!")
                print("")
                return True
        return False

    def removeWinner(self):
        for i in range(len(self.players)):
            if len(self.players[i].hand) == 0:
               self.winners.append(self.players.pop(i))
               break

    #Function for testing purposes
    def test_deal(self):
        for player in self.players:
            player.hand.append(Card("spades",1))
            player.hand.append(Card("spades",2))
            player.hand.append(Card("spades",3))
            player.hand.append(Card("spades",4))
            player.hand.append(Card("spades",5))
            player.hand.append(Card("spades",6))
            player.hand.append(Card("spades",7))
            player.hand.append(Card("spades",8))
            player.hand.append(Card("spades",9))
            player.hand.append(Card("spades",10))
            player.hand.append(Card("spades",11))
            player.hand.append(Card("spades",12))
            player.hand.append(Card("spades",13))

    def play_game(self):

        self.deck.build_deck()
        self.deck.shuffle()
        #different patterns user can play
        #suit hierarchy 
        #initial variables
        last_cards_played = []
        cur_player = 0
        for i in range(4):
            self.add_player()
        self.deal()
        #use below function when testing 
        #self.test_deal() 
        cur_player = self.find_first_player()
        while len(self.players) > 1:
            if self.skip_count == len(self.players) - 1:
                self.cur_condition = "free_for_all"
                self.skip_count = 0
                last_cards_played = []
            last_cards_played = self.playerTurn(cur_player, last_cards_played)
            if self.checkWinner():
                if cur_player == len(self.players) - 1:
                  cur_player = 0
                self.removeWinner()      
            else:
                cur_player = self.find_next_player(cur_player)
        self.winners.append(self.players.pop(0))
        self.displayWinners()
            
testclass = Thirteen_Game()
testclass.play_game()

