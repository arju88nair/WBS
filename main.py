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


"""
ORM MODEL

Defined the main columns and their attributes
"""

class BluePrint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slno = db.Column(db.String(45))
    name = db.Column(db.String(255))
    start_date = db.Column(db.String(45))
    end_date = db.Column(db.String(255))
    parent_id = db.Column(db.Integer)

   
"""
Main Route for the home page

Same route for the whole blue print and filtered activities view.
Depends on the parent id (pid)


Returns:
    template
"""

@app.route('/', methods=["GET", "POST"])
def home():
    tag='default'
    pid = request.args.get("pid")
    blueprints = BluePrint.query.all()
    if pid :
        tag=pid
        blueprints = BluePrint.query.filter(or_(BluePrint.parent_id == pid,BluePrint.id == pid))
    return render_template("home.html",blueprints=blueprints, tagid=tag)



"""
CSV downlaoding
 Categorized between sorting 

 Arguments:

 tag -- Default view and pid based for the activities
 mode -- Sort mode

Returns:
    File download MIME type
"""

@app.route('/downloadCsv', methods=["GET", "POST"])
def index():   
    pid = request.args.get("tag") 
    mode = request.args.get("mode") 
    column="slno"
    if mode == "start":
        column="start_date"

    records = db.session.query(BluePrint.slno,BluePrint.name,BluePrint.start_date,BluePrint.end_date).order_by(getattr(BluePrint, column).desc()).all()

    if pid != "default":       
        tag=pid
        records=db.session.query(BluePrint.slno,BluePrint.name,BluePrint.start_date,BluePrint.end_date).filter(or_(BluePrint.parent_id == pid,BluePrint.id == pid)).order_by(getattr(BluePrint, column).desc())
    
    filename = 'docs/wdsfile'+'_'+str(randint(1,99))+'.csv'
    writeToCsv(records,filename)
    return send_from_directory('',
                               filename, as_attachment=True)


"""
CSV generation method

Arguments :
data -- Data to write
filename -- To save

"""

def writeToCsv(data,filename):
    with open(filename, 'w') as theFile:
        headersList = ['slno','name','start_date','end_date']
        headers = ",".join(headersList)
        theFile.write(headers+'\n')
        test=[]
        for record in data:
            commaSeperated=None
            commaSeperated = ','.join(map(str, record)) 
            theFile.write(commaSeperated+'\n')


if __name__ == "__main__":
    app.run(debug=True)
