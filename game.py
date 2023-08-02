import random
class Computer:
    def __init__(self, name):
        self.name = name

    def choose(self):
        self.choice = random.choice(['rock', 'paper', 'scissors'])
class Player:
    def __init__(self, name):
        self.name = name

    def choose(self):
        self.choice = input('Choose (rock, paper, scissors): ').lower()
        while self.choice not in ['rock', 'paper', 'scissors']:
            self.choose()
class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.keep_play = True
    
    def play(self):
        self.player1.choose()
        self.player2.choose()
        print(f'{self.player1.name} chooses {self.player1.choice}')
        print(f'{self.player2.name} chooses {self.player2.choice}')

        if(self.player1.choice == self.player2.choice):
            print('Draw')

        elif(self.player1.choice , self.player2.choice) in [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]:
            print(f'{self.player1.name} wins')
        else:
            print(f'{self.player2.name} wins')
        
        keep =input('Do you want to play again (y/n)?').lower()
        while keep not in ['y','n']:
            keep =input('Do you want to play again (y/n)?').lower()
        
        self.keep_play = (keep == 'y')
        
def main():
    player = Player(input('Enter your name: '))
    computer = Computer("Computer")
    game = Game(player, computer)
    while game.keep_play:
        game.play()
if __name__ == "__main__":
    main()
