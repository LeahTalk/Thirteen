from deck_of_cards import Deck
from deck_of_cards import Card
from player import Player

class Thirteen_Game:
    def __init__ (self):
        self.players = []
        self.deck = Deck()
    
    def add_player(self, player_name = 'Default Player'):
        player_name = input("What is your name, player? ")
        print (f"Player, {player_name} has joined the game")
        self.players.append(Player(player_name))

##    #NEED TO TEST
    def find_first_player(self):
        for i in range(len(self.players)):
            for card in self.players[i].hand:
                if (card.value == 3) and (card.suit == "spades"):
                    return i
        return 0  

##    #NEED TO TEST
##    def find_next_player(current_player):
##        if current_player == 3:
##            return 0
##        return current_player + 1

##FOR THESE BELOW: assume they have access to cur_condition. chosen cards is the list
##returned by your chosen_cards function and the cur_player is the index for the current
    ##player in the player list
    def checkSingle(self, chosen_cards, cur_player):
        pass

    def checkDouble(self, chosen_cards, cur_player):
        pass

    def checkTriple(self, chosen_cards, cur_player):
        pass

    def checkQuad(self, chosen_cards, cur_player):
        pass

    def checkStraight(self, chosen_cards, cur_player):
        pass

    def deal(self):
        card_index = 0
        player_index = 0
        while card_index < 52:
            if(player_index > 3):
                player_index = 0
            print(str(card_index))
            print(str(player_index))
            self.players[player_index].hand.append(self.deck.deck[card_index])
            player_index += 1
            card_index += 1
            
##
##    def removeChosenCards(cur_player, chosen_cards):
##        pass
    
    def choose_new_condition(self, the_condition = 'Not valid'):
        the_condition = input("Choose a condition for your move, single, double, triple, four, or straight: ")
        if the_condition == 'single' or the_condition == 'double' or the_condition == 'triple' or the_condition == 'four' or the_condition == 'straight':
            print (f"You are playing the {the_condition} condition.")
            return the_condition
        else:
            print("Sorry, please choose a valid condition")
            self.choose_new_condition()

    #function play turn return skip, list
    def chooseCards(self, the_cards="Not valid"):
        the_cards = input("Choose your cards or skip: ")
        if the_cards == 'skip':
            return 'skip'
        listed_cards = the_cards.split(',')
        print(f"You are playing: {listed_cards}")
    
##    def playerTurn(cur_player):
##        valid = False
##        chosen_cards = []
##        display_last_cards_played()
##        #check naming
##        cur_player.display_hand()
##        if cur_condition == "free_for_all":
##            #check naming
##            cur_condition= choose_new_condition()
##        while(not valid):
##            chosen_cards = choose_cards()
##            valid = checkValidity(chosen_cards, cur_player)
##        if valid == "skip":
##            skip_count +=1
##            return last_cards_played
##        skip_count = 0
##        new_last_cards = []
##        for hand_index in chosen_cards:
##            new_last_cards.append(cur_player.hand(int(hand_index)))
##        removeChosenCards(cur_player, chosen_cards)
##        return new_last_cards
##            
##    def checkValidity(chosen_cards, cur_player):
##        return conditions[cur_condition](chosen_cards, cur_player)
##
##    def displayWinner():
##        pass
##
##    def checkWinner():
##        for player in self.players:
##            if(len(player.hand) == 0):
##                return true
##        return false

    def play_game(self):

        self.deck.build_deck()
        self.deck.shuffle()
        #different patterns user can play
        conditions = {
            "single" : self.checkSingle,
            "double" : self.checkDouble,
            "triple" : self.checkTriple,
            "quad" : self.checkQuad,
            "straight" : self.checkStraight,
            "free_for_all" : 1
        }
        #suit hierarchy 
        suit_values = {
            "spades" : 0,
            "clubs" : 1,
            "diamonds" : 2,
            "hearts" : 3
        }

        #initial variables
        last_cards_played = []
        skip_count = 0
        cur_player = 0
        cur_condition = "free_for_all"
        
        for i in range(4):
            self.add_player()
        self.deal()
        cur_player = self.find_first_player()
        #while(!self.checkWinner()):
         #   if skipCount == 3:
          #      cur_condition = "free_for_all"
           #     skipCount = 0
            #last_cards_played = self.playerTurn(cur_player)
        #self.displayWinner()
            
testclass = Thirteen_Game()
testclass.play_game()
for player in testclass.players:
    player.display_hand()
print(testclass.find_first_player())

