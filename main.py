import os
from flask import Flask
import user_interface.user_interface as ui
from Database import db

app = Flask(__name__)
app.register_blueprint(ui.user)

#CONFIG
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = './static/media'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'dfdwrlw234hjdfs'
db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)

