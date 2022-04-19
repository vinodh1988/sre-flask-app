from config import app
from flask import jsonify
from models import people

@app.route("/people")
def getPeople():
    listp=people.getPeople()
    result = [x.serialize() for x in listp]
    return jsonify(result)
    
    
