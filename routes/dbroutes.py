from config import app,db
from flask import jsonify,request
from models import people,DbPerson

@app.route("/dbpeople")
def getDbPeople():
    listp=DbPerson.query.all()
    result = [x.serialize() for x in listp]
    return jsonify(result)

