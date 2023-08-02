class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def start_game(self):
        for player in self.players:
            player.score = 10 

    def get_winner(self):
        max_score = -1
        winner = None
        for player in self.players:
            if player.score > max_score:
                max_score = player.score
                winner = player
        return winner

def main():
    game = Game()

    player1 = Player(input())
    player2 = Player(input())
    player3 = Player(input())

    game.add_player(player1)
    game.add_player(player2)
    game.add_player(player3)

    game.start_game()

    winner = game.get_winner()
    if winner:
        print("The winner is:", winner.name)
    else:
        print("No winner found.")

if __name__ == "__main__":
    main()