# SUDOKU APPLICATION (Responsive on WEB & Mobile)

### Authors: Xiaoyu (21982644) & Abhirama Satya Sai Pavan Gunisetty (23005869)

In this project, we have created an user interface with authentication pages which allows users to create their own account and play sudoku. This also stores their results and display their statistics when compared to other players and also their ranks.

Let us see how do we run the project.

### Create a new folder with somename

`mkdir sudoku`

Now unzip ourfiles and transfer them to this folder. And then enter into this folder with `cd sudoku`

### Create a virtual environment

`python3 -m venv auth`

This will create the python virtual environment named "auth"

### Activate the virtual environment.

`.\auth\Scripts\activate`

This is the code to activate the virtual env and this might chnage with respect to OS. Please check.

### Install required libraries and create required environment

Example: `pip install flask flask-sqlalchemy flask-login`

Install all the libraries and modules mentioned in the requirements.txt file using pip install. this will help you create desired environment to run the app.

### Set the FLASK_APP and FLASK_DEBUG values.

`export FLASK_APP=project export FLASK_DEBUG=1`

In windows, instead of export, we will have to use **set**.

**We have also included sample database "db.sqlite" for testing purposes.**

### Run the app

`flask run`

The above command will compile and runs the application on a locl host server. If it compiles successfully, the please redirect to the addres that is given as the localhost. That will run the application.

## Now, we will see the usage and descripti of every page.

Inside the project folder, you can find all the .py, .html, .css and .js files which are the most important files of this application.

**base.html** - This is the base design page that is included in almost every other page. This page contains the logo and header part.

**index.html** - This is the home page for the website.

**login.html & signup.html** - These pages allows user to either create an account (signup.html) or login (login.html) if user has an account already.

**rules.html** - This page describes the rules of the game and how to play guide to the users with proper description and few hints.

**dashboard.html** - This is the main page where this displays the information of the user, and this activities as a player. In this page, user can see the total number of games he played, his best scores in each mode of the game and also, this page has got the buttons that will let user to **play game** or **View Statistics** of other players such as ranks and best scores in every mode.

**play.html** - This page is where the user will play the game.

**easyStats.html, mediumStats.html, hardStats.html** - These are the pages for three different modes and will display the statistics for each mode. This has got the game performance details of every player and also the ranks and best scores.

All the above pages other than _play.html_ takes the styling in **base.css** and _play.html_ takes the styling in **play.css**.

**const.js, game.js, play.js** are the javascript files used to create the sudoku game experience where in **base.js & somepart of play.js** are used to create the best user experience with javascript.

**db.sqlite** is the database that we have and we have two tables in it. One is **User** that stores the details of the users and another one is **Game** that will store theresults of the games played by each player.

**auth.py & main.py** are python files which will help us to do the backend things like querying the tables, filtering out the details with respect to the user and many more.

## How to run the tests

After coming out of the project folder, you will see the tests folder. That has got the .py files which are used for testing and a sample database that is used for testing.

To run these files, we need to navigate back to the main folder and now we can see tests folder and other folders.
Now, run these in the terminal

`python -W ignore -m tests.unit_test` <br>
`python -W ignore -m tests.basic`

This will run the tests and will give the desired test results.

**Also, while validating html and css, our html files are giving the errors for using the flask related syntax in the html documents. We couldn't find other alternative to get rid of those errors**
