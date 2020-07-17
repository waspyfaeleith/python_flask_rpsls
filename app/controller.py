from flask import render_template, request
from app import app
from app.models.rpsls import *

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/new_game')
def new_game():
    return render_template('game.html', title='Play')

@app.route('/play/<user>')
def play(user):
    computer = get_computer_choice();
    winning_choice = get_winner(user, computer)
    if (winning_choice == user):
        winner = "User"
    else:
        winner = "Computer"
    return render_template('result.html', title='Result', user=user, computer=computer, winner=winner, winning_choice=winning_choice)