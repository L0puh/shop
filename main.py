import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#CONFIG
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = './static/media'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)

