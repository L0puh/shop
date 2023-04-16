import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from user_interface.user_interface import user_interface
app = Flask(__name__)

#CONFIG
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = './static/media'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'dfdwrlw234hjdfs'
db = SQLAlchemy(app)

app.register_blueprint(user_interface)

if __name__ == "__main__":
    app.run(debug=True)

