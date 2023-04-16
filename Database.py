from main import db, app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String)

with app.app_context():
    db.create_all()
    print('+ created db')

#ADD: class cart (id_user and product?), class product, class reviews 

