import os
from flask import Flask

app = Flask(__name__)

#CONFIG
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = './static/media'
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'database.db')))

if __name__ == "__main__":
    app.run(debug=True)
