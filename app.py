"""Flask app for Cupcakes"""

from flask import Flask, request, render_template, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy
from models import * 


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes' #use this for production
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes-test' #use this for testing
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


app.config['SECRET_KEY'] = 'chickenzarcool21837'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

@app.route('/api/cupcakes')
def get_allcc_data():
    selection = Cupcake.query.all()
    return {"cupcakes" : [cc.asJSON() for cc in selection]}

@app.route('/api/cupcakes/<int:ccid>')
def get_a_cupcake(ccid):
    selection = Cupcake.query.get_or_404(ccid)
    return selection.asJSON()

@app.route('/api/cupcakes', methods = ["POST"])
def createcc():
    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image']

    new1 = Cupcake(flavor = flavor, size = size, rating = rating, image = image or None)
    db.session.add(new1)
    db.session.commit()

    return new1.asJSON()

@app.route('/api/cupcakes/<int:id>', methods = ["DELETE"])
def deletecc(id):
    Cupcake.query.get_or_404(id)
    Cupcake.query.filter_by(id = id).delete()
    db.session.commit()

    return {"message-status" : "Deleted"}

@app.route('/api/cupcakes/<int:id>', methods = ["PATCH"])
def updatecc(id):
    changed = Cupcake.query.get(id)
    if request.json['flavor']:
        changed.flavor = request.json['flavor']
    if request.json['size']:
        changed.size = request.json['size']
    if request.json['rating']:
        changed.rating = request.json['rating']
    if request.json['image']:
        changed.image = request.json['image']

    db.session.commit()

    return changed.asJSON()

@app.route("/")
def show_home():
    print("n\n\n\n\n\n\n begin here\n")
    return render_template("home.html")
