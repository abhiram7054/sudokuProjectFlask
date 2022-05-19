from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from .models import User, Game
from . import db
import json


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/dashboard')
@login_required
def dashboard():

    print("total number of rows are : ", Game.query.filter_by(email=current_user.email).count())

    games = Game.query.filter((Game.email==current_user.email) & (Game.mode == 0)).all()
    print(games)

    # if db.session.query(Game).filter_by(email=current_user.email).count() > 1 :
    if Game.query.filter_by(email=current_user.email).count() > 1 :
        bestScore = Game.query.with_entities(Game.score).filter_by(email=current_user.email).order_by(Game.score.asc()).limit(2)[1][0]
        print(bestScore)
    else:
        bestScore = Game.query.with_entities(Game.score).filter_by(email=current_user.email).order_by(Game.score.asc()).first()[0]
        print(bestScore)
    return render_template('dashboard.html', name=current_user.name, bestScore=bestScore)

@main.route('/play')
@login_required
def play():
    return render_template('play.html', name=current_user.name)

#======================================================
@main.route('/gameResults', methods=['GET', 'POST'])
def gameResults():
    if request.method == 'POST':
        print("the final score is : ",request.form.get('finalScore'))
        a = request.form.get('finalScore')
        a = json.loads(a)
        # print("a is :", type(a))
        # print(a["level"])
        new_game = Game(email=current_user.email, mode= a["level"], score= a["seconds"])
        db.session.add(new_game)
        db.session.commit()

    return "OK"

@main.route('/upload', methods=['POST'])
def upload():
    # code to validate and add user to database goes here
    return redirect(url_for('main.dashboard'))

@main.route('/rules')
def rules():
    return render_template('rules.html')