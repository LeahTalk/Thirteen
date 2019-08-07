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
    
    # def find_first_player():
    
    # def find_next_player():

    # def get_player_names():

    # def play_game():

testclass = Thirteen_Game()
print(testclass.players)
testclass.add_player()
