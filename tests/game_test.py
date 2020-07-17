import unittest
from src.game import *

class TestGame(unittest.TestCase):

    def test_rpsl_rock_paper_paper_wins(self):
        expected = "paper"
        actual = get_winner("rock", "paper")
        self.assertEqual(expected, actual)

    def test_rpsl_rock_scissors_rock_wins(self):
        expected = "rock"
        actual = get_winner("rock", "scissors")
        self.assertEqual(expected, actual)

    def test_rpsl_scissors_paper_wins_scissors_wins(self):
        expected = "scissors"
        actual = get_winner("scissors", "paper")
        self.assertEqual(expected, actual)
