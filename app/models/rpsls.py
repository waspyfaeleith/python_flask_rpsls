import random

def get_computer_choice():
    options = ["rock", "paper", "scissors", "lizard", "spock"]
    return random.choice(options)


def get_winner(player_1_choice, player_2_choice):
    if player_1_choice == player_2_choice:
        return None
    options = {
        "rock": ["Scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["paper", "spock"],
        "spock": ["rock", "scissors"],
    }
    if player_2_choice in options[player_1_choice]:
        return player_1_choice
    else:
        return player_2_choice

