import random
from enum import Enum

class PlayChoice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class GameManager:

    def __init__(self):
        self.human_score = 0
        self.computer_score = 0

    def get_human_score(self):
        return self.human_score

    def get_computer_score(self):
        return self.computer_score

    def choose_play(self):
        choice_value = random.randrange(1,4)
        return choice_value

    def determine_winner(self, human_play, computer_play):
        if (computer_play + 1) %3 == human_play %3:
            self.human_score = self.human_score + 1
        elif (computer_play - 1) == human_play %3:
            self.computer_score = self.computer_score + 1