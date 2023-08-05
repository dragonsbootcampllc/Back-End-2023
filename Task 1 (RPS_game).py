import random

class RockPaperScissors:
    def __init__(self):
        self.options = ['rock', 'paper', 'scissors']
        self.player1_choice = None
        self.player2_choice = None

    def get_human_choice(self):
        while True:
            human_input = input("Enter your choice (rock/paper/scissors): ").lower()
            if human_input in self.options:
                self.player1_choice = human_input
                break
            else:
                print("Invalid choice! Please try again.")

    def select_random_choice(self):
        self.player2_choice = random.choice(self.options)

    def determine_winner(self):
        if self.player1_choice == self.player2_choice:
            return "It's a tie!"
        elif (
            (self.player1_choice == 'rock' and self.player2_choice == 'scissors') or
            (self.player1_choice == 'paper' and self.player2_choice == 'rock') or
            (self.player1_choice == 'scissors' and self.player2_choice == 'paper')
        ):
            return "You win!"
        else:
            return "Computer wins!"

    def display_choices(self):
        print(f"You chose: {self.player1_choice}")
        print(f"Computer chose: {self.player2_choice}")

    def play_game(self):
        self.get_human_choice()
        self.select_random_choice()
        self.display_choices()
        print(self.determine_winner())

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()
