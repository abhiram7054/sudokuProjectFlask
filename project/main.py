from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from .models import User, Game
from . import db
import json
from sqlalchemy import func


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, email=current_user.email)

@main.route('/dashboard')
@login_required
def dashboard():

    print("total number of rows are : ", Game.query.filter_by(email=current_user.email).count())

    # games = len(Game.query.filter((Game.email==current_user.email) & (Game.mode == 0)).all())
    # games = Game.query.with_entities(Game.score).filter((Game.email==current_user.email) & (Game.mode == 1)).order_by(Game.score.asc()).all()
    # print(games)

    totalGamesPlayed = Game.query.filter_by(email=current_user.email).count()

    #================================================================================================

    # for easy mode

    if len(Game.query.filter((Game.email==current_user.email) & (Game.mode == 0)).all()) > 0:
        easySeconds = Game.query.with_entities(Game.score).filter((Game.email==current_user.email) & (Game.mode == 0)).order_by(Game.score.asc()).first()[0]
        if easySeconds >=3600 :
            easyMinutes, easySeconds = divmod(easySeconds, 60)
            easyHours, easyMinutes = divmod(easyMinutes, 60)
            bestScore_easy = str(easyHours) + " Hrs " + str(easyMinutes) + " Mins " + str(easySeconds) + " Secs"
        else:
            bestScore_easy = str(easySeconds//60) + " Mins " + str(easySeconds%60) + " Secs"
        gamesPlayed_easy = len(Game.query.filter((Game.email==current_user.email) & (Game.mode == 0)).all())
    else:
        bestScore_easy = 0
        gamesPlayed_easy = 0

    # for medium mode

    if len(Game.query.filter((Game.email==current_user.email) & (Game.mode == 1)).all()) > 0:
        mediumSeconds = Game.query.with_entities(Game.score).filter((Game.email==current_user.email) & (Game.mode == 1)).order_by(Game.score.asc()).first()[0]
        if mediumSeconds >=3600 :
            mediumMinutes, mediumSeconds = divmod(mediumSeconds, 60)
            mediumHours, mediumMinutes = divmod(mediumMinutes, 60)
            bestScore_medium = str(mediumHours) + " Hrs " + str(mediumMinutes) + " Mins " + str(mediumSeconds) + " Secs"
        else:
            bestScore_medium = str(mediumSeconds//60) + " Mins " + str(mediumSeconds%60) + " Secs"
        gamesPlayed_medium = len(Game.query.filter((Game.email==current_user.email) & (Game.mode == 1)).all())
    else:
        bestScore_medium = 0
        gamesPlayed_medium = 0

    # for hard mode

    if len(Game.query.filter((Game.email==current_user.email) & (Game.mode == 2)).all()) > 0:
        hardSeconds = Game.query.with_entities(Game.score).filter((Game.email==current_user.email) & (Game.mode == 2)).order_by(Game.score.asc()).first()[0]
        if hardSeconds >=3600 :
            hardMinutes, hardSeconds = divmod(hardSeconds, 60)
            hardHours, hardMinutes = divmod(hardMinutes, 60)
            bestScore_hard = str(hardHours) + " Hrs " + str(hardMinutes) + " Mins " + str(hardSeconds) + " Secs"
        else:
            bestScore_hard = str(hardSeconds//60) + " Mins " + str(hardSeconds%60) + " Secs"
        gamesPlayed_hard = len(Game.query.filter((Game.email==current_user.email) & (Game.mode == 2)).all())
    else:
        bestScore_hard = 0
        gamesPlayed_hard = 0

    #================================================================================================

    return render_template('dashboard.html', name=current_user.name, email=current_user.email,bestScoreEasy=bestScore_easy, bestScoreMedium=bestScore_medium, bestScoreHard=bestScore_hard, gamesPlayedEasy=gamesPlayed_easy, gamesPlayedMedium=gamesPlayed_medium, gamesPlayedHard=gamesPlayed_hard, totalGamesPlayed=totalGamesPlayed)


@main.route('/easyStats',  methods=["GET", "POST"])
@login_required
def easyStats():
    # easyTable = Game.query.filter(Game.mode == 0).order_by(Game.score.asc()).all()

    easyQuery = db.session.query(
    Game, 
    func.rank()\
        .over(
            order_by=Game.score.asc()
        )\
        .label('rank')
    )

    easyTable = easyQuery.filter_by(mode=0).all()
    
    print(easyTable)


    if request.method == "GET":
         return render_template("easyStats.html", easyTable = easyTable)

@main.route('/mediumStats',  methods=["GET", "POST"])
@login_required
def mediumStats():

    # mediumTable = Game.query.filter(Game.mode == 1).order_by(Game.score.asc()).all()

    mediumQuery = db.session.query(
    Game, 
    func.rank()\
        .over(
            order_by=Game.score.asc()
        )\
        .label('rank')
    )

    mediumTable = mediumQuery.filter_by(mode=1).all()

    if request.method == "GET":
         return render_template("mediumStats.html", mediumTable = mediumTable)

@main.route('/hardStats',  methods=["GET", "POST"])
@login_required
def hardStats():

    hardTable = Game.query.filter(Game.mode == 2).order_by(Game.score.asc()).all()

    hardQuery = db.session.query(
    Game, 
    func.rank()\
        .over(
            order_by=Game.score.asc()
        )\
        .label('rank')
    )

    hardTable = hardQuery.filter_by(mode=2).all()

    if request.method == "GET":
         return render_template("hardStats.html", hardTable = hardTable)

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
        new_game = Game(email=current_user.email, name=current_user.name, mode= a["level"], score= a["seconds"])
        # new_game = Game(email=current_user.email, mode= a["level"], score= a["seconds"])
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