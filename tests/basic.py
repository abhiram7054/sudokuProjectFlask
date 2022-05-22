import unittest
from project import db
from project import create_app
from project.models import User, Game

app = create_app(testing=True)
app.app_context().push()

class BasicTests(unittest.TestCase):
    # executed prior to each test
    def setUp(self):

        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        
        self.app = app.test_client()

        db.drop_all()
        db.create_all()

    # executed after each test
    def tearDown(self):
        pass

    '''
    HTML pages 
    '''
    # test home page
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

     # test rule page
    def test_rule_page(self):
        response = self.app.get('/rules', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # signup page
    def test_signup_page(self):
        response = self.app.get('/signup', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    # login page
    def test_signup_page(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    # logout 
    def test_signup_page(self):
        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    '''
    pages cannot be accessed without auth
    '''
    # profile
    def test_profile_page_invalid(self):
        response = self.app.get('/profile', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)
        assert response.request.path == "/login"

    # dashboard
    def test_dashboard_page_invalid(self):
        response = self.app.get('/dashboard', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)
        assert response.request.path == "/login"
    
    # play page
    def test_play_page_invalid(self):
        response = self.app.get('/play', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)
        assert response.request.path == "/login"

    # stats page
    def test_stats_page_invalid(self):
        response = self.app.get('/stats', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)
        assert response.request.path == "/login"

    '''
    Authentication
    '''
    # helper methods for authentication
    def register(self, email, password, name):
        return self.app.post('/signup',data=dict(email=email, password=password, name=name),
        follow_redirects=True)
        
    def login(self, email, password):
        return self.app.post('/login',data=dict(email=email, password=password),
        follow_redirects=True)
        
    def logout(self):
        return self.app.get('/logout',follow_redirects=True)
    
    # test login 
    def test_valid_login(self):
        response_r = self.register('1234@gmail.com',"1234","1234")
        self.assertEqual(response_r.status_code, 200)
        response= self.login("1234@gmail.com", "1234")
        self.assertEqual(response.status_code, 200)
        assert response.request.path == "/dashboard"

    def test_invalid_password(self):
        response_r = self.register('1234@gmail.com',"1234","1234")
        self.assertEqual(response_r.status_code, 200)
        response= self.login('1234@gmail.com','12345678')
        self.assertIn(b'Please check your login details and try again.', response.data)
        assert response.request.path == "/login"

    def test_invalid_email(self):
        response_r = self.register('1234@gmail.com',"1234","1234")
        self.assertEqual(response_r.status_code, 200)
        response= self.login('12345@gmail.com','1234')
        self.assertIn(b'Please check your login details and try again.', response.data)
        assert response.request.path == "/login"

    # test sign up 
    def test_valid_signup(self):
        response = self.register('sudoku@gmail.com', 'sudoku', 'sudoku')
        self.assertEqual(response.status_code, 200)
        assert response.request.path == "/login"
    
    def test_invalid_signup_duplicate_email(self):
        response = self.register('sudoku@gmail.com', 'sudoku', 'sudoku')
        self.assertEqual(response.status_code, 200)
        response = self.register('sudoku@gmail.com', 'sudoku2', 'sudoku2')
        self.assertIn(b'Email address already exists', response.data)
        assert response.request.path == "/signup"

    '''
    GameResults and game table
    '''
    # test save game data to db
    def test_game_success(self):
        response_r = self.register('1234@gmail.com',"1234","1234")
        self.assertEqual(response_r.status_code, 200)
        response = self.login("1234@gmail.com", "1234")
        self.assertEqual(response.status_code, 200)

        info = '{"level": 2, "seconds": 406}'

        self.app.post('/gameResults', data = dict(finalScore=info))
        
        u = Game.query.filter_by(email="1234@gmail.com").first()

        self.assertEqual(u.score, 406)
        self.assertEqual(u.mode, '2')

        self.assertNotEqual(u.score, 0)
        self.assertNotEqual(u.mode, 2)

    # play page
    def test_play_page_valid(self):
        response_r = self.register('1234@gmail.com',"1234","1234")
        self.assertEqual(response_r.status_code, 200)
        response_l = self.login("1234@gmail.com", "1234")
        self.assertEqual(response_l.status_code, 200)    
        assert response_l.request.path == "/dashboard"

        response = self.app.get('/play')
        self.assertIn(b'<div class="btn btn-blue" id="btn-play">New game</div>', response.data)

    '''
    check user data in dashboard page 
    username, games played and best score for each game mode 
    ''' 
    def test_user_dashboard(self):
        response_r = self.register('1234@gmail.com',"1234","1234")
        self.assertEqual(response_r.status_code, 200)
        response_l = self.login("1234@gmail.com", "1234")
        self.assertEqual(response_l.status_code, 200)
        assert response_l.request.path == "/dashboard"

        easy =   '{"level": 0, "seconds": 406}'
        easy2 =   '{"level": 0, "seconds": 500}'
        easy3 =   '{"level": 0, "seconds": 500}'

        medium = '{"level": 1, "seconds": 400}'
        hard =   '{"level": 2, "seconds": 3600}'

        self.app.post('/gameResults', data = dict(finalScore=easy))
        self.app.post('/gameResults', data = dict(finalScore=easy2))
        self.app.post('/gameResults', data = dict(finalScore=easy3))

        self.app.post('/gameResults', data = dict(finalScore=medium))
        self.app.post('/gameResults', data = dict(finalScore=hard))
        
        '<p class="bestScore">BEST SCORE : <span> 6 Mins 46 Secs</span> <br> GAMES PLAYED : <span>1</span></p>'

        response_dash = self.app.get('/dashboard') 
        
        html = response_dash.get_data(as_text=True)

        assert '6 Mins 46 Secs' in html
        assert '6 Mins 40 Secs' in html
        assert '1 Hrs 0 Mins 0 Secs' in html

        assert 'GAMES PLAYED : <span>3</span>' in html
        assert 'GAMES PLAYED : <span>1</span>' in html

        assert '1234' in html
        assert 'Total Games Played : 5' in html 

if __name__ == "__main__":
    unittest.main(verbosity=2)

