import random

class RockPaperScissors:
    def __init__(self):
        self.objects = ["rock", "paper", "scissors"]
    def get_random_object(self):
        return random.choice(self.objects)
    def compare_objects(self, object1, object2):
        if object1 == object2:
            return "tie"
        elif object1 == "rock" and object2 == "scissors":
            return "player1"
        elif object1 == "scissors" and object2 == "paper":
            return "player1"
        elif object1 == "paper" and object2 == "rock":
            return "player1"
        else:
            return "player2"
def main():
    game = RockPaperScissors()
    player1_object = game.get_random_object()
    player2_object = game.get_random_object()
    result = game.compare_objects(player1_object, player2_object)
    print("Player 1 chose:", player1_object)
    print("Player 2 chose:", player2_object)
    print("The winner is:", result)
if __name__ == "__main__":
    main()
