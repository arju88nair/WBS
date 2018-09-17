import os
import csv
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
import urllib
from flask import send_from_directory
from sqlalchemy import or_


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
    pid = request.args.get("pid")
    blueprints = BluePrint.query.all()
    if pid :
        blueprints = BluePrint.query.filter(or_(BluePrint.parent_id == pid,BluePrint.id == pid))

    return render_template("home.html",blueprints=blueprints)



@app.route('/downloadCsv', methods=["GET", "POST"])
def index():    
    records = BluePrint.query.all()
    with open('vehicle.csv', 'w') as f_handle:
        writer = csv.writer(f_handle)
        # Add the header/column names
        header = ['id','slno','name','start_date','end_date','parent_id']
        writer.writerow(header)
        # Iterate over `data`  and  write to the csv file
        [writer.writerow([getattr(curr, column.name) for column in BluePrint.__mapper__.columns]) for curr in records]
    # return redirect("vehicle.csv", code=302)
    return send_from_directory('',
                               'vehicle.csv', as_attachment=True)





if __name__ == "__main__":
    app.run(debug=True)
