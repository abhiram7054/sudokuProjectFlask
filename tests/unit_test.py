import unittest, os
from project import db
from project.models import User, Game
from project import create_app
from werkzeug.security import generate_password_hash, check_password_hash
# from app import app 

app = create_app()
app.app_context().push()

class ModelTest(unittest.TestCase):
    # executed prior to each test
    def setUp(self):

        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
        app.config['TESTING'] = True
            
        self.app = app.test_client()

        db.create_all()

        user1 = User(email = "1234@gmail.com", password = "1234", name="1234")
        user2 = User(email = "12345@gmail.com", password = "1234", name="1234")
        game1 = Game(email = "1234@gmail.com", mode = '3', score = 300)
        game2 = Game(email = "1234@gmail.com", mode ='2', score = 200)
        
        db.session.add(user1)
        db.session.add(user2)
        
        db.session.add(game1)
        db.session.add(game2)
        db.session.commit()
   
    # executed after each test
    def tearDown(self):
        db.session.remove()
        with app.app_context():
            db.drop_all()

    def set_password(password):
        return generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

    def test_password_hashing(self):
        u = User.query.filter_by(email="1234@gmail.com").first()
        u.password = generate_password_hash('test')
        self.assertFalse(check_password_hash(u.password, "case"))
        self.assertTrue(check_password_hash(u.password, "test"))
        self.assertEqual(u.name, "1234")
        self.assertNotEqual(u.name, "12345")
    
    def test_game_model(self):
        u = Game.query.filter_by(email="1234@gmail.com").first()
        self.assertEqual(u.mode, "3")
        self.assertNotEqual(u.mode, "4")

        self.assertEqual(u.score, 300)
        self.assertNotEqual(u.score, 400)

if __name__ == "__main__":
    unittest.main(verbosity=2)