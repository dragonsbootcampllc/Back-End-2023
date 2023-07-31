
#Task 2 Rock, Paper, Scissors Game
import random

class Rock:
    def __init__(self):
       self.pieceName = "Rock"

class Paper:
   def __init__(self):
       self.pieceName = "Paper"

class Scissors:
   def __init__(self):
       self.pieceName = "Scissors"

class Player:
    def __init__(self,playerName):
        self.playerName = playerName
        self.piece = None

class Game:
    def __init__(self,player1Name,player2Name):
        self.player1 = Player(player1Name)
        self.player2 = Player(player2Name)
        self.allPieces = [Rock(),Paper(),Scissors()]
    def random_pieces(self):
         self.player1.piece = random.choice(self.allPieces)
         self.player2.piece = random.choice(self.allPieces)
    def win_piece(self):
        print(self.player1.piece.pieceName,"VS",self.player2.piece.pieceName)
        # ROCK VS PAPER
        if(self.player1.piece.pieceName == "Rock" and self.player2.piece.pieceName == "Paper"):
            return self.player2.playerName
        elif(self.player1.piece.pieceName == "Paper" and self.player2.piece.pieceName == "Rock"):
            return self.player1.playerName
            
        # ROCK VS Scissors
        elif(self.player1.piece.pieceName == "Rock" and self.player2.piece.pieceName == "Scissors"):
            return self.player1.playerName
        elif(self.player1.piece.pieceName == "Scissors" and self.player2.piece.pieceName == "Rock"):
            return self.player2.playerName
            
        # Paper VS Scissors
        elif(self.player1.piece.pieceName == "Scissors" and self.player2.piece.pieceName == "Paper"):
            return self.player1.playerName
        elif(self.player1.piece.pieceName == "Paper" and self.player2.piece.pieceName == "Scissors"):
            return self.player2.playerName
            
        # TIE No one win
        else:
            return "Tie"
def main():
    player1Name = input("Enter player 1 name: ")
    player2Name = input("Enter player 2 name: ")
    game = Game(player1Name, player2Name)
    game.random_pieces()
    winner = game.win_piece()
    if winner == "Tie":
        print("It's a tie!")
    else:
        print(f"{winner} wins!")

if __name__ == "__main__":
    main()
