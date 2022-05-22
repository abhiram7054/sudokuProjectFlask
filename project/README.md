# SUDOKU APPLICATION (Responsive on WEB & Mobile)

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

## Now, we will see what page does what exactly.

**base.html** - This is the base design page that is included in almost every other page. This page contains the logo and header part.

**index.html** - This is the home page for the website.

**login.html & signup.html** - These pages allows user to either create an account (signup.html) or login (login.html) if user has an account already.

**rules.html** - This page describes the rules of the game and how to play guide to the users with proper description and few hints.

**dashboard.html** - This is the main page where this displays the information of the user, and this activities as a player.
