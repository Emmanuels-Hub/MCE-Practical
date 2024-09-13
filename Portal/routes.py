from random import randint
from flask import Blueprint, jsonify, request

from Portal.model import SoilDB
from Portal import db

# Define blueprint
main = Blueprint('main', __name__)

@main.route("/index")
@main.route("/")
def home():
    return "Welcome to our page"

# Fetch temperature
@main.route('/get_temp/', methods=['GET', 'POST'])
def get_temp():
    temp = SoilDB.query.order_by(SoilDB.id.desc()).first()
    js = temp.temperature
    return jsonify({'moisture': js})

# Fetch Moisture
@main.route('/get_moist/', methods=['GET', 'POST'])
def get_moist():
    moist = SoilDB.query.order_by(SoilDB.id.desc()).first()
    js = moist.moisture
    return jsonify({'moisture': js})


@main.route('/get_data/', methods=['GET'])
def get_data():
    data = request.get_json()
    temp = data.get('temperature')
    moist = data.get('moisture')
    
    soil_db = SoilDB(
        moisture = moist,
        temperature = temp
    )
    db.session.add(soil_db)
    db.session.commit()
    return jsonify({'status': 100})


@main.route('/fake_data/', methods=['GET'])
def fake_data():

    temp = randint(10,50)
    moist = randint(10,50)
    
    soil_db = SoilDB(
        moisture = moist,
        temperature = temp
    )
    db.session.add(soil_db)
    db.session.commit()
    return jsonify({'status': 100})
