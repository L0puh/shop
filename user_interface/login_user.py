from Database import db, User

def login_user(name, email, password, repeat_password):
    if hash(password) == hash(repeat_password):
        try:
            user = User(username=name, email=email, password=hash(password))
            db.session.add(user)
            db.session.commit()
            return True
        except:
            print('smt went wrong')
            return False
