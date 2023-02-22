"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    def connect_db(app):
        db.app = app
        db.init_app(app)

    __tablename__= "cupcakes"

    def __repr__(self):
        return "Some description"

    id = db.Column(db.Integer, nullable = False, unique = True, autoincrement = True, primary_key=True )
    flavor = db.Column(db.String(31), nullable = False)
    size = db.Column(db.String(15), nullable = False)
    rating = db.Column(db.Float, nullable = False)
    image = db.Column(db.String(2048), nullable = False, default = 'https://tinyurl.com/demo-cupcake')

    def asJSON(cupcake): 
        """self-reminder: I used 'cupcake' instead of self.  Don't freakout.  
        Remember you can name your own 'this' keyword in python. It reads nicer this way"""
        return {'id' : cupcake.id, 'flavor' : cupcake.flavor, 'size' : cupcake.size, 'rating' : cupcake.rating, 'image' : cupcake.image}
    