import os
import csv

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
import urllib
from flask import send_from_directory
from sqlalchemy import or_
from random import *
from flask_sqlalchemy import SQLAlchemy
import json

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
    tag='default'
    pid = request.args.get("pid")
    blueprints = BluePrint.query.all()
    if pid :
        tag=pid
        blueprints = BluePrint.query.filter(or_(BluePrint.parent_id == pid,BluePrint.id == pid))
    return render_template("home.html",blueprints=blueprints, tagid=tag)



@app.route('/downloadCsv', methods=["GET", "POST"])
def index():   
    pid = request.args.get("tag") 
    records = db.session.query(BluePrint.slno,BluePrint.name,BluePrint.start_date,BluePrint.end_date).all()

    if pid:
        tag=pid
        records=db.session.query(BluePrint.slno,BluePrint.name,BluePrint.start_date,BluePrint.end_date).filter(or_(BluePrint.parent_id == pid,BluePrint.id == pid))
    
    filename = 'docs/wdsfile'+'_'+str(randint(1,99))+'.csv'
    with open(filename, 'w') as f_handle:
        writer = csv.writer(f_handle)
        # Add the header/column names
        header = ['slno','name','start_date','end_date']
        writer.writerow(header)
        # Iterate over `data`  and  write to the csv file
        for record in records:
            writer.writerow(record)
    return send_from_directory('',
                               filename, as_attachment=True)





if __name__ == "__main__":
    app.run(debug=True)
