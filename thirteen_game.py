import deck_of_cards

class Thirteen_Game:
    def __init__ (self):
        self.players = []
        self.deck = []
    
    def add_player(self, player_name = 'Default Player'):
        player_name = input("What is your name, player?")
        print (f"Player, {player_name} has joined the game")
        self.deck.append(player_name)
        # self.players.append(Player(player_name))

    #NEED TO TEST
    def find_first_player():
        for i in range(len(players)):
            for card in players[i].hand:
                if (card.value == 3) and (card.suit == "spades"):
                    return i
        return 0  

    #NEED TO TEST
    def find_next_player(current_player):
        if current_player == 3:
            return 0
        return current_player + 1

##FOR THESE BELOW: assume they have access to cur_condition. chosen cards is the list
##returned by your chosen_cards function and the cur_player is the index for the current
    ##player in the player list
    def checkSingle(chosen_cards, cur_player):
        pass

    def checkDouble(chosen_cards, cur_player):
        pass

    def checkTriple(chosen_cards, cur_player):
        pass

    def checkQuad(chosen_cards, cur_player):
        pass

    def checkStraight(chosen_cards, cur_player):
        pass

    def deal():
        pass

    def playerTurn(cur_player):
        valid = False
        chosen_cards = []
        display_last_cards_played()
        #check naming
        cur_player.display_hand()
        if cur_condition == "free_for_all":
            #check naming
            cur_condition= choose_new_condition()
        while(!valid):
            chosen_cards = choose_cards()
            valid = checkValidity(chosen_cards, cur_player)
        if valid == "skip":
            skip_count +=1
            return last_cards_played
        skip_count = 0
        new_last_cards = []
        for hand_index in chosen_cards:
            new_last_cards.append(cur_player.hand(int(hand_index)))
            ##NEED TO ADD REMOVING PLAYER HAND
            
    def checkValidity(chosen_cards, cur_player):
        return conditions[cur_condition](chosen_cards, cur_player)

    def play_game():
        #different patterns user can play
        conditions = {
            "single" : checkSingle,
            "double" : checkDouble,
            "triple" : checkTriple,
            "quad" : checkQuad,
            "straight" : checkStraight,
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
        ccur_player = 0
        cur_condition = "free_for_all"
        
        for i in range(4):
            add_player()
        deal()
        cur_player = find_first_player()
        while(all player hands > 0):
            if skipCount == 3:
                cur_condition = "free_for_all"
                skipCount = 0
            playerTurn(cur_player)
            
testclass = Thirteen_Game()
print(testclass.players)
testclass.add_player()
