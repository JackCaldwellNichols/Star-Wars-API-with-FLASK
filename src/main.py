"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, json
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, People, Planets, User, Favourite_planet, Favourite_person
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)



@app.route('/people', methods=['GET'])
def get_all_people():
    people = People.query.all()
    all_people = list(map(lambda x: x.serialize(), people))
    return jsonify(all_people), 200

@app.route('/people/<int:id>', methods=['GET'])
def get_individual(id):
    individual = People.query.get(id).serialize()
    return jsonify(individual), 200

@app.route('/planets', methods=['GET'])
def get_all_planets():
    planets = Planets.query.all()
    all_planets = list(map(lambda x: x.serialize(), planets))
    return jsonify(all_planets), 200

@app.route('/planets/<int:id>', methods=['GET'])
def get_individual_planet(id):
    planet = Planets.query.get(id).serialize()
    return jsonify(planet), 200


@app.route('/user', methods=['GET'])
def get_all_users():
    users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), users))
    return jsonify(all_users), 200

@app.route('/favourites/planets', methods=['GET'])
def get_favourite_planet():
    favourites = Favourite_planet.query.filter_by(user_id=1)
    favourites = list(map(lambda favs: favs.serialize(), favourites))
    return jsonify(favourites), 200

@app.route('/favourites/people', methods=['GET'])
def get_favourite_people():
    favourites = Favourite_planet.query.filter_by(user_id=1)
    favourites = list(map(lambda favs: favs.serialize(), favourites))
    return jsonify(favourites), 200


@app.route('/people', methods=['POST'])
def add_character():
    request_body_person = request.get_json()

    character = People(name=request_body_person["name"], height=request_body_person["height"], mass=request_body_person["mass"], gender=request_body_person["gender"])
    db.session.add(character)
    db.session.commit()

    return jsonify(request_body_person)

@app.route('/favourites/people/<int:id>', methods=['POST'])
def add_character_fav(id):
    fav_person = People.query.get(id)
    fav_person = Favourite_person()
    fav_person.user_id = 1
    fav_person.people_id = id
    db.session.add(fav_person)
    db.session.commit()
    return jsonify("Favourite added")

@app.route('/favourites/planets/<int:id>', methods=['POST'])
def add_planet_fav(id):
    fav_planet = Planets.query.get(id)
    fav_planet = Favourite_planet()
    fav_planet.user_id = 1
    fav_planet.planet_id = id
    db.session.add(fav_planet)
    db.session.commit()
    return jsonify("Favourite added")



@app.route('/favourites/planets/<int:planet_id>', methods=['DELETE'])
def del_planet_fav(planet_id):
    planet_fav = Favourite_planet.query.filter_by(planet_id=planet_id, user_id=1).first()
    if planet_fav:
        db.session.delete(planet_fav)
        db.session.commit()
        return jsonify("Deleted")
    else:
        return jsonify("Doesn't exist")
  

@app.route('/favourites/people/<int:people_id>', methods=['DELETE'])
def del_person_fav(people_id):
    people_fav = Favourite_person.query.filter_by(people_id=people_id, user_id=1).first()
    if people_fav:
        db.session.delete(people_fav)
        db.session.commit()
        return jsonify("Deleted")
    

 
# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
