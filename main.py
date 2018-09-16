import os

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file= 'mysql://root:@127.0.0.1/wds'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_file

db = SQLAlchemy(app)

class BluePrint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slno = db.Column(db.String(45))
    name = db.Column(db.String(255))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    parent_id = db.Column(db.Integer)

   

@app.route('/', methods=["GET", "POST"])
def home():
    blueprints = BluePrint.query.all()
    return render_template("home.html",blueprints=blueprints)

if __name__ == "__main__":
    app.run(debug=True)
